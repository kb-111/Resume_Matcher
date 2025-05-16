import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_cgpa(text):
    
    text = text.lower()
    
    # Common patterns for CGPA
    patterns = [
        r'cgpa\s*[:=\-]?\s*(\d\.\d+)',         # CGPA: 8.5
        r'c\.g\.p\.a\s*[:=\-]?\s*(\d\.\d+)',   # C.G.P.A: 9.0
        r'gpa\s*[:=\-]?\s*(\d\.\d+)',          # GPA: 3.7
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue
    return None

def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def bert_similarity(resume, job_desc):
    embeddings = model.encode([resume, job_desc])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return score * 100

def suggest_keywords(resume, job_desc, top_n=10):
    resume_words = set(clean_text(resume).split())
    jd_words = clean_text(job_desc).split()
    freq = {}
    for word in jd_words:
        if word not in resume_words:
            freq[word] = freq.get(word, 0) + 1
    sorted_kw = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw for kw, _ in sorted_kw[:top_n]]
