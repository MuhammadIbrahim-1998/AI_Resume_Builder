# 🧠 AI-Powered Resume Builder

Welcome to the **AI-Powered Resume Builder**, a smart web application that analyzes resumes using Natural Language Processing (NLP) and extracts useful information such as **Name**, **Email**, **Phone Number**, and **Skills** from uploaded `.pdf`, `.doc`, or `.docx` files.

## 🚀 Features

- ✅ Upload resumes directly through the browser
- ✅ Extract structured data using `spaCy`, `NLTK`, and `pdfminer.six`
- ✅ Clean and responsive user interface
- ✅ Built using **Flask** (Python) and **Vanilla HTML/CSS/JS**
- ✅ Basic file validation and error handling
- ✅ Easily extendable for further resume insights (experience, education, etc.)

---



---

## 🛠️ Tech Stack

| Frontend              | Backend         | AI & NLP Tools       |
|-----------------------|------------------|------------------------|
| HTML, CSS, JavaScript | Flask (Python)   | spaCy, NLTK, pdfminer.six |

---

## 📂 Project Structure

AI_Powered_Resume_Builder/
│
├── client/ # Frontend files
│ ├── index.html # Main UI
│ └── static/
│ ├── css/style.css # Styling
│ └── js/script.js # JS logic
│
├── server/ # Backend files
│ ├── app.py # Flask server
│ ├── resume_parser.py # NLP Resume Parsing
│ └── utils.py # Helper functions
│
├── templates/ # Flask templates (optional)
│ └── index.html
├── .gitignore
├── requirements.txt
└── README.md



---

## 🔧 Setup Instructions

1. **Clone this repository:**

   
   git clone https://github.com/MuhammadIbrahim-1998/AI_Resume_Builder.git
   cd AI_Resume_Builder


2. **Create and activate a virtual environment:**

   python -m venv venv
   venv\Scripts\activate    # On Windows

3. **Install dependencies:**

   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

4. **Run the application:**

   cd server
   python app.py

5. **Visit in browser:**

   http://localhost:5000

📤 How It Works

Upload your resume in PDF/DOC/DOCX format

Backend reads and parses the resume text using pdfminer and docx

spaCy & NLTK analyze the content to extract key fields

Parsed data is shown in JSON format

📌 Limitations

Current version extracts only: Name, Email, Phone, Skills

Performance may vary with poorly formatted documents

Can be extended with ML models to extract education, experience, projects, etc.

✨ Future Improvements

Add PDF preview

Add frontend resume builder (from scratch)

Enhance extraction with AI models (GPT, BERT)

Export parsed data to JSON, CSV, or DOCX

🧠 Contributors

Muhammad Ibrahim – Developer & Project Owner
GitHub: MuhammadIbrahim-1998




   


