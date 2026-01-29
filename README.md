# 🚀 Smart ATS Resume Ranker

A smart Application Tracking System (ATS) that optimizes resumes using Large Language Models (LLMs). This tool evaluates resumes against specific Job Descriptions (JD), providing a match percentage, identifying missing keywords, and offering a professional profile summary.

Built with **Python**, **Streamlit**, and **Groq (Llama-3.3)**.

🔗 **Live Repo:** [https://github.com/Officialhimanshu710/Smart-ATS-Ranker](https://github.com/Officialhimanshu710/Smart-ATS-Ranker)

---

## 📸 Demo

<img width="2126" height="1250" alt="image" src="https://github.com/user-attachments/assets/3482eefa-ef09-4037-8a35-aaa2ae10f42c" />

---

## ✨ Features

- **📊 Match Percentage Score:** Instantly calculates how well the resume matches the JD (0-100%).
- **🔴 Missing Keywords:** Identifies critical technical skills and keywords missing from the resume.
- **📝 Profile Summary:** Generates or refines a professional summary tailored to the job role.
- **📄 PDF Support:** specific parsing logic for PDF documents.
- **⚡ Fast & Free:** Powered by the Groq API for lightning-fast inference.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM:** Llama-3.3-70b-versatile (via Groq API)
- **PDF Processing:** PyPDF (pypdf)
- **Environment Management:** Python-dotenv

---

## 🚀 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/Officialhimanshu710/Smart-ATS-Ranker.git](https://github.com/Officialhimanshu710/Smart-ATS-Ranker.git)
cd Smart-ATS-Ranker
```

2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

5. Set up Environment Variables
Create a .env file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
(You can get a free key from Groq Console)
```

🏃‍♂️ Usage
Run the Streamlit app:

```
streamlit run main.py
```

The app will open in your browser at ```http://localhost:8501.```

1. Paste the Job Description in the text area.

2. Upload your Resume (PDF).

3. Click "Analyze Resume".

📂 Project Structure
```
Smart-ATS-Ranker/
│
├── .env                # API keys (Not uploaded to GitHub)
├── .gitignore          # Files to ignore
├── main.py             # Main application logic (Streamlit + Logic)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the prompt engineering or UI.
