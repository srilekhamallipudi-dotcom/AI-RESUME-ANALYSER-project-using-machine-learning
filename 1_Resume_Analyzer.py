import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from fpdf import FPDF

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Custom CSS Styling
st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            to right,
            #141e30,
            #243b55
        );
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    .stButton>button {
        background-color: #00c6ff;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        border: none;
        font-size: 18px;
    }

    .stDownloadButton>button {
        background-color: #11998e;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        border: none;
        font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("📊 AI Resume Analyzer")

st.write("Upload your resume and get ATS score instantly 🚀")

# Job Role Selection
job_role = st.selectbox(
    "Select Job Role",
    [
        "Data Analyst",
        "Machine Learning Engineer",
        "Web Developer"
    ]
)

# Required skills based on role
if job_role == "Data Analyst":

    required_skills = [
        "python",
        "sql",
        "excel",
        "power bi",
        "communication"
    ]

elif job_role == "Machine Learning Engineer":

    required_skills = [
        "python",
        "machine learning",
        "pandas",
        "numpy",
        "git"
    ]

else:

    required_skills = [
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ]

# Upload PDF Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# Process Resume
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    text = ""

    # Extract text from pages
    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    # Convert to lowercase
    text = text.lower()

    # Matched skills
    matched_skills = []

    for skill in required_skills:

        if skill in text:
            matched_skills.append(skill)

    # ATS Score
    score = (len(matched_skills) / len(required_skills)) * 100

    # Missing skills
    missing_skills = []

    for skill in required_skills:

        if skill not in matched_skills:
            missing_skills.append(skill)

    # ATS Score Section
    st.subheader("📈 ATS Score")

    st.progress(int(score))

    st.metric(
        label="Resume Score",
        value=f"{score:.0f}%"
    )

    # Matched Skills
    st.subheader("✅ Matched Skills")

    if matched_skills:

        for skill in matched_skills:
            st.success(skill.upper())

    else:
        st.warning("No matched skills found.")

    # Missing Skills
    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.error(skill.upper())

    else:
        st.success("No missing skills!")

    # Skill Recommendations
    st.subheader("📚 Recommended Skills To Learn")

    recommendations = {

        "python": "Learn Python for programming and automation.",

        "sql": "Learn SQL for database management.",

        "excel": "Practice Excel for data analysis.",

        "power bi": "Learn Power BI for dashboards and visualization.",

        "communication": "Improve communication and presentation skills.",

        "machine learning": "Study ML algorithms and projects.",

        "pandas": "Learn Pandas for data handling.",

        "numpy": "Learn NumPy for numerical computing.",

        "git": "Learn Git and GitHub for version control.",

        "html": "Learn HTML for webpage structure.",

        "css": "Learn CSS for webpage styling.",

        "javascript": "Learn JavaScript for frontend development.",

        "react": "Learn React for modern web applications."
    }

    for skill in missing_skills:

        if skill in recommendations:
            st.info(recommendations[skill])

    # Pie Chart
    st.subheader("📊 Skills Analysis")

    matched_count = len(matched_skills)
    missing_count = len(missing_skills)

    labels = ["Matched", "Missing"]

    sizes = [matched_count, missing_count]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.axis("equal")

    st.pyplot(fig)

    # Feedback Section
    st.subheader("💡 Resume Feedback")

    if score >= 80:

        st.success(
            "Excellent Resume! Your resume matches most required skills."
        )

        st.balloons()

    elif score >= 50:

        st.warning(
            "Good Resume! Add more skills to improve ATS score."
        )

    else:

        st.error(
            "Your resume needs improvement."
        )

    # PDF Report Generation
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(
        200,
        10,
        txt="AI Resume Analyzer Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.cell(
        200,
        10,
        txt=f"ATS Score: {score:.0f}%",
        ln=True
    )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        txt="Matched Skills:",
        ln=True
    )

    for skill in matched_skills:

        pdf.cell(
            200,
            10,
            txt=f"- {skill}",
            ln=True
        )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        txt="Missing Skills:",
        ln=True
    )

    for skill in missing_skills:

        pdf.cell(
            200,
            10,
            txt=f"- {skill}",
            ln=True
        )

    # Save PDF
    pdf.output("resume_report.pdf")

    # Download Button
    with open("resume_report.pdf", "rb") as file:

        st.download_button(
            label="📥 Download Report",
            data=file,
            file_name="resume_report.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown("---")

st.caption("Developed by Srilekha 😄")