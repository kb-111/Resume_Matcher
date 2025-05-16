import streamlit as st
from model.file_parser import extract_text_from_file
from model.nlp_utils import extract_cgpa, clean_text, bert_similarity, suggest_keywords
from model.keyword_highlighter import highlight_keywords

st.title("📄 Resume Keyword Matcher")

# Step 1: Upload resume or paste manually
uploaded_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])
resume_text = ""

if uploaded_file:
    resume_text = extract_text_from_file(uploaded_file)
else:
    resume_text = st.text_area("Or paste your Resume text")

# Step 2: Get job description
job_desc = st.text_area("Paste Job Description")

# Step 3: Ask for required CGPA
required_cgpa = st.number_input("Minimum CGPA required (from job description)", min_value=0.0, max_value=10.0, step=0.01)

# Step 4: Proceed only if resume and job description are provided
if resume_text and job_desc:

    # Step 4.1: Extract CGPA from resume
    extracted_cgpa = extract_cgpa(resume_text)

    if extracted_cgpa is None:
        st.warning("❗ Could not detect CGPA in your resume. Please ensure it's clearly mentioned.")
    elif extracted_cgpa < required_cgpa:
        st.warning(f"📉 Your CGPA ({extracted_cgpa}) is below the required minimum ({required_cgpa}). Matching skipped.")
    else:
        # Step 5: Check match if button is clicked
        if st.button("Check Match"):
            clean_resume = clean_text(resume_text)
            clean_jd = clean_text(job_desc)

            similarity = bert_similarity(clean_resume, clean_jd)
            st.success(f"✅ Match Score: {similarity:.2f}%")

            # Highlight keywords
            st.markdown("### 📌 Highlighted Resume")
            st.markdown(highlight_keywords(resume_text, job_desc), unsafe_allow_html=True)

            # Suggested keywords
            st.markdown("### 💡 Suggested Keywords to Include")
            suggestions = suggest_keywords(resume_text, job_desc)
            if suggestions:
                st.write(", ".join(suggestions))
            else:
                st.write("Your resume already includes most of the key terms!")
else:
    st.info("Please upload a resume and job description to begin.")
   