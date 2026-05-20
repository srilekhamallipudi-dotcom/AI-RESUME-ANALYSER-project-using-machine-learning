import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# 🌈 Background CSS
page_bg = """
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
    url("https://images.unsplash.com/photo-1522202176988-66273c2fd55f");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

h1, h2, h3, p, .stMarkdown {
    color: white !important;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Main title
st.title("📄 AI Resume Analyzer")

# Welcome text
st.markdown(
    """
    ## Welcome 😄
    
    This AI-based application analyzes resumes  
    and generates ATS scores based on skills.
    
    ### Features
    
    - Resume Upload
    - Skill Detection
    - ATS Score
    - Missing Skills
    - Resume Feedback
    
    👉 Open the sidebar to navigate between pages.
    """
)

# Image
st.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=250
)

# Success message
st.success("Project Ready 🚀")

# Footer
st.markdown("---")
st.caption("Developed by Srilekha 😄")