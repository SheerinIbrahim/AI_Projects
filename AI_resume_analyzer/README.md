# 🧠 Resume Analyzer + Job Match Scorer

A smart NLP tool that compares a resume with a job description and returns a match score based on semantic similarity. Great for job seekers who want to tailor their resume for specific roles.

---

## 🚀 Features

- 📄 Upload your resume (PDF format)
- 📝 Paste a job description
- 🧠 Uses NLP (BERT embeddings) to compute match score
- 🔍 Highlights skill alignment potential

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **NLP**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Frontend**: Simple HTML + JavaScript
- **PDF Parsing**: PyMuPDF (`fitz`)
