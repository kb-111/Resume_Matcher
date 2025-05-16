# 📄 Resume Keyword Matcher

An intelligent web app that compares a resume with a job description and returns a match score based on keyword and semantic similarity. Designed to help job seekers optimize their resumes for better chances of shortlisting.

---

## 🚀 Features

- 🔍 **Semantic Matching**: Uses BERT embeddings to calculate similarity between resume and job description.
- 📄 **Resume Parsing**: Supports `.pdf` and `.docx` uploads, or manual text input.
- 🎯 **Keyword Highlighting**: Highlights overlapping terms between resume and job description.
- 📈 **Match Score**: Displays a match percentage based on semantic and keyword relevance.
- 🧠 **Tailored Suggestions**: Suggests missing keywords to improve your resume.
- ✅ **CGPA Filtering**: Automatically extracts CGPA from resume and filters based on user-specified threshold.

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – for the web UI
- **BERT (via SentenceTransformers)** – for semantic similarity
- **Regex** – for extracting CGPA and basic text processing
- **docx2txt, PyMuPDF** – for parsing `.docx` and `.pdf` files
- **NLTK / Scikit-learn (optional)** – for basic keyword extraction

---

## 🧪 Sample Usage
- Upload your resume (PDF or DOCX).
- Paste the job description.
- Enter the minimum CGPA requirement.
- View:
  - Your match score
  - Highlighted overlaps
  - Suggested keywords to improve
