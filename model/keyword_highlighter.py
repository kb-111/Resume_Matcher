# def highlight_keywords(resume, job_desc):
#     resume_words = set(resume.lower().split())
#     jd_words = set(job_desc.lower().split())
#     common = resume_words.intersection(jd_words)
#     highlighted = []
#     for word in resume.split():
#         if word.lower() in common:
#             highlighted.append(f"**:green[{word}]**")
#         else:
#             highlighted.append(word)
#     return " ".join(highlighted)
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def highlight_keywords(resume, job_desc):
    resume_words = set(resume.lower().split()) - stop_words
    jd_words = set(job_desc.lower().split()) - stop_words
    common = resume_words.intersection(jd_words)
    
    highlighted = []
    for word in resume.split():
        if word.lower() in common:
            highlighted.append(f"**:green[{word}]**")
        else:
            highlighted.append(word)
    return " ".join(highlighted)
