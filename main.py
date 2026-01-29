import streamlit as st
import os
import json
from dotenv import load_dotenv
from pypdf import PdfReader
from groq import Groq
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# extract text from pdf
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# logic
def get_groq_response(jd_text, resume_text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    input_prompt = """
    Act as an expert Applicant Tracking System (ATS). 
    Your task is to evaluate the resume against the job description.

    1. Assign a Match Percentage (0-100%).
    2. List Missing Keywords that are critical for the role.
    3. Profile Summary: If the resume has a summary, refine it. If it DOES NOT have a summary, GENERATE a strong, professional profile summary (3-4 lines) based on the candidate's skills and projects.

Output strictly in this JSON format:
{"JD Match": "85%", "MissingKeywords": ["keyword1", "keyword2"], "Profile Summary": "Candidate is a..."}
"""
    formatted_prompt = f"{input_prompt}\n\nJob Description: {jd_text}\n\nResume: {resume_text}"

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_prompt
            }
        ],
        model="llama-3.3-70b-versatile", 
    )
    
    return completion.choices[0].message.content

# ui design
def main():
    st.set_page_config(page_title="Smart ATS", page_icon="🚀", layout="wide")
    st.title("🚀 Smart ATS Resume Ranker")
    st.subheader("Optimize your resume for the Application Tracking System")
    
    # Input Section
    col1, col2 = st.columns(2)
    
    with col1:
        jd = st.text_area("Paste the Job Description (JD)", height=300)
    
    with col2:
        uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"], help="Please upload a PDF file only")
        submit = st.button("Analyze Resume", type="primary") # 'primary' makes it red/highlighted

    if submit:
        if uploaded_file is not None and jd:
            with st.spinner('Analyzing Resume...'):
                resume_text = extract_text_from_pdf(uploaded_file)
                response = get_groq_response(jd, resume_text)
                
                try:
                    parsed_response = json.loads(response)
                    
                    # --- Result Section ---
                    st.divider() # Creates a nice horizontal line
                    
                    # Create 3 columns: Score, Summary, Keywords
                    c1, c2 = st.columns([1, 2])
                    
                    with c1:
                        # 1. The Score Card
                        match_str = parsed_response["JD Match"].replace("%", "")
                        match_score = int(match_str)
                        
                        st.metric("ATS Match Score", f"{match_score}%")
                        st.progress(match_score / 100)
                        
                        # Simple logic for color feedback
                        if match_score >= 80:
                            st.success("Great Match!")
                        elif match_score >= 50:
                            st.warning("Average Match")
                        else:
                            st.error("Low Match")

                    with c2:
                        # 2. The Summary (Native 'Info' box looks like a card)
                        st.subheader("Profile Summary")
                        st.info(parsed_response["Profile Summary"])
                    
                    # 3. Missing Keywords (Using native Markdown for "Tag" look)
                    st.subheader("Missing Critical Keywords")
                    if parsed_response["MissingKeywords"]:
                        # Convert list ['Python', 'SQL'] -> string "`Python`  `SQL`"
                        # This creates the grey pill look natively
                        formatted_keywords = "  ".join([f"`{kw}`" for kw in parsed_response["MissingKeywords"]])
                        st.write(formatted_keywords)
                        st.caption("Tip: Add these keywords to your resume to boost your score.")
                    else:
                        st.balloons()
                        st.success("✅ No critical keywords missing!")

                    # Raw Data (Hidden inside an expander)
                    with st.expander("View Full Analysis Data"):
                        st.json(parsed_response)

                except json.JSONDecodeError:
                    st.error("Error parsing response. Please try again.")
                    st.write(response)
        elif not uploaded_file:
            st.warning("Please upload a resume PDF.")
        elif not jd:
            st.warning("Please paste a Job Description.")

if __name__ == "__main__":
    main()

