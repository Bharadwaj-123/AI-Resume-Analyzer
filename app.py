import streamlit as st
from resume_parser import extract_text
from analyzer import analyze_resume
import time
from streamlit_extras.metric_cards import style_metric_cards
from report_generator import generate_report
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0F172A,#1E293B);
}

/* Main Title */

.title{
    font-size:48px;
    font-weight:700;
    color:white;
    text-align:center;
}

.subtitle{
    color:#CBD5E1;
    text-align:center;
    font-size:20px;
}

/* Cards */

.card h3{
    color:white !important;
    font-size:30px !important;
    font-weight:700;
}

.card p,
.card li{
    color:#F8FAFC !important;
    font-size:19px !important;
}

/* Metric Card */

.metric{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:25px;
    border-radius:18px;
    color:white;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    box-shadow:0 10px 20px rgba(0,0,0,.35);
    transition:0.3s;
}

.metric:hover{
    transform:translateY(-6px);
}

/* Skill Tags */

.skill{
    display:inline-block;
    background:linear-gradient(90deg,#16A34A,#22C55E);
    color:white;
    padding:12px 20px;
    border-radius:30px;
    margin:8px;
    font-size:19px;
    font-weight:700;
    box-shadow:0 4px 12px rgba(0,0,0,.3);
}

.missing{
    display:inline-block;
    background:linear-gradient(90deg,#DC2626,#EF4444);
    color:white;
    padding:12px 20px;
    border-radius:30px;
    margin:8px;
    font-size:19px;
    font-weight:700;
    box-shadow:0 4px 12px rgba(0,0,0,.3);
}

.job{
    background:linear-gradient(90deg,#2563EB,#3B82F6);
    color:white;
    padding:18px;
    border-radius:12px;
    margin:10px 0;
    font-size:22px;
    font-weight:bold;
    text-align:center;
    box-shadow:0 4px 10px rgba(0,0,0,.3);
}
            /* General Text */

p,
li,
span,
label,
div,
h1,
h2,
h3,
h4,
h5,
h6{
    color:#F8FAFC !important;
}
            /* -------- File Uploader -------- */

/* Upload label */
[data-testid="stFileUploader"] label{
    color:white !important;
    font-weight:600;
}

/* Uploaded filename */
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p{
    color:#FFFFFF !important;
    font-weight:600;
}

/* File uploader box */
[data-testid="stFileUploader"]{
    color:white !important;
}

/* Browse/Upload button */
[data-testid="stFileUploader"] button{
    color:white !important;
    background:#2563EB !important;
    border-radius:10px;
}

/* Uploaded file name */
section[data-testid="stFileUploaderDropzone"]{
    color:white !important;
}
            /* Force uploaded filename to white */

.stFileUploader *{
    color:#FFFFFF !important;
}
            /* Upload helper text */
[data-testid="stFileUploader"] small {
    color: #E2E8F0 !important;
    opacity: 1 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Streamlit uploader text */
[data-testid="stFileUploader"] div {
    color: #E2E8F0 !important;
}

/* Specifically the "200MB per file • PDF, DOCX" text */
[data-testid="stFileUploaderDropzoneInstructions"] {
    color: #E2E8F0 !important;
    opacity: 1 !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] * {
    color: #E2E8F0 !important;
    opacity: 1 !important;
}
            /* Hide default upload helper text */
[data-testid="stFileUploaderDropzoneInstructions"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------

st.markdown(
"""
<div class='title'>📄 AI Resume Analyzer</div>

<div class='subtitle'>
Analyze your resume, calculate ATS score and get professional suggestions.
</div>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- Upload ----------------

uploaded_file = st.file_uploader(
    "📂 Upload Resume",
    type=["pdf", "docx"]
)
st.markdown(
    """
    <div style="
        color:#E2E8F0;
        font-size:18px;
        margin-top:-8px;
        margin-bottom:18px;
        font-weight:500;">
        📄 Supported Formats: <b>PDF</b>, <b>DOCX</b> &nbsp;&nbsp;|&nbsp;&nbsp;
        Maximum File Size: <b>200 MB</b>
    </div>
    """,
    unsafe_allow_html=True
)

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Resume uploaded successfully!")

    progress = st.progress(0)
    status = st.empty()

    status.info("📄 Reading Resume...")

    for i in range(30):
        progress.progress(i + 1)
        time.sleep(0.02)

    resume_text = extract_text(uploaded_file)

    status.info("🤖 Analyzing Resume...")

    for i in range(30, 70):
        progress.progress(i + 1)
        time.sleep(0.02)

    result = analyze_resume(resume_text)

    status.info("📊 Generating Report...")

    for i in range(70, 100):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.success("✅ Analysis Complete!")
    left_col, right_col = st.columns([1, 1.4], gap="large")
    st.markdown("## 📊 Resume Analysis Dashboard")

    st.write("")

    # =============================
    # SCORE CARDS
    # =============================

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            label="📄 Resume Score",
            value=f"{result['score']}/100",
            delta="Good"
        )

    with c2:
        st.metric(
            label="🎯 ATS Score",
            value=f"{result['ats']}%",
            delta="Optimized"
        )

    style_metric_cards(
        background_color="#2563EB",
        border_left_color="#22C55E",
        border_size_px=0,
        border_radius_px=18,
    )
        # =============================
    # RESUME STRENGTH
    # =============================

    st.write("")

    if result["score"] >= 85:

        st.success("🟢 Excellent Resume — Ready for AI/ML & Software Engineering roles.")

    elif result["score"] >= 70:

        st.info("🔵 Good Resume — A few improvements can make it even stronger.")

    elif result["score"] >= 50:

        st.warning("🟡 Average Resume — Improve your technical skills and resume content.")

    else:

        st.error("🔴 Needs Improvement — Add more projects, skills and achievements.")

    st.write("")

    # =============================
    # ATS KEYWORD MATCH
    # =============================

    st.markdown(
    """
    <h2 style='color:white;'>
    🎯 ATS Keyword Match
    </h2>
    """,
    unsafe_allow_html=True
    )

    st.progress(result["ats"] / 100)

    st.markdown(
    f"""
    <div style='
    color:#E2E8F0;
    font-size:20px;
    font-weight:600;
    margin-top:8px;
    margin-bottom:20px;'>

    <b>{result["ats"]}%</b> of important resume keywords matched with ATS expectations.

    </div>
    """,
    unsafe_allow_html=True
    )

    st.write("")

    # =============================
    # SKILLS
    # =============================

    left, right = st.columns(2)

    with left:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
"""
<h2 style='color:white;'>
✅ Skills Found
</h2>
""",
unsafe_allow_html=True
)

        if result["found"]:

            for skill in result["found"]:

                st.markdown(
                    f"<div class='skill'>{skill}</div>",
                    unsafe_allow_html=True
                )

        else:

            st.warning("No skills detected.")

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
"""
<h2 style='color:white;'>
❌ Missing Skills
</h2>
""",
unsafe_allow_html=True
)

        if result["missing"]:

            for skill in result["missing"]:

                st.markdown(
                    f"<div class='missing'>{skill}</div>",
                    unsafe_allow_html=True
                )

        else:

            st.success("Excellent! No missing skills detected.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # =============================
    # SUGGESTIONS & JOB ROLES
    # =============================

    left, right = st.columns(2)

    with left:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
"""
<h2 style='color:white;'>
💡 Suggestions
</h2>
""",
unsafe_allow_html=True
)

        if "GitHub" not in result["found"]:
            st.markdown("### ✅ Add your GitHub Profile")

        if "Communication" not in result["found"]:
            st.markdown("### ✅ Mention Communication Skills")

        if "Docker" in result["missing"]:
            st.markdown("### ✅ Learn Docker")

        if "AWS" in result["missing"]:
            st.markdown("### ✅ Learn AWS")

        if result["score"] < 60:
            st.markdown("### ✅ Add More Technical Skills")

        st.markdown("### ✅ Keep Resume to One Page")

        st.markdown("### ✅ Add Quantified Achievements")

    with right:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
"""
<h2 style='color:white;'>
💼 Recommended Roles
</h2>
""",
unsafe_allow_html=True
)

        roles = []

        if "Python" in result["found"]:
            roles.append("Python Developer")

        if "Machine Learning" in result["found"]:
            roles.append("Machine Learning Engineer")

        if "Artificial Intelligence" in result["found"]:
            roles.append("AI Engineer")

        if "SQL" in result["found"]:
            roles.append("Data Analyst")

        if len(roles) == 0:
            roles.append("Software Developer")

        for role in roles:

            st.markdown(
                f"<div class='job'>{role}</div>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)
        pdf_file = generate_report(result)

        with open(pdf_file, "rb") as file:

            st.download_button(

                "📥 Download Analysis Report",

                data=file,

                file_name="Resume_Analysis_Report.pdf",

                mime="application/pdf",

                use_container_width=True

            )

st.write("")
st.markdown("---")
st.markdown("---")

st.markdown(
"""
<div style='text-align:center;
color:#94A3B8;
font-size:17px;
padding:15px;'>

🚀 Built with Python • Streamlit • NLP • Resume Parsing • ATS Analysis

</div>
""",
unsafe_allow_html=True
)