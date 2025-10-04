
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Ng Poh Siang — Portfolio Resume",
    page_icon="🧭",
    layout="wide"
)

# ---------- Helper styles ----------
st.markdown(
    """
    <style>
    .pill {
        display:inline-block; padding:6px 10px; border-radius:999px;
        border:1px solid rgba(120,120,120,.25); margin:4px 6px 0 0;
        font-size:0.90rem
    }
    .section-title {
        font-weight:700; font-size:1.3rem; margin: 0.25rem 0 0.5rem 0;
    }
    .card {
        border:1px solid rgba(120,120,120,.25);
        border-radius:16px; padding:1rem; margin-bottom:0.75rem;
    }
    .muted { color: #6c757d; }
    .tight p { margin: .25rem 0; }
    .hero h1 { margin-bottom: .25rem; }
    .hero-sub { font-size: 1.05rem; }
    .metricbox {
        border-radius: 14px; padding:.75rem 1rem; border:1px solid rgba(120,120,120,.2);
    }
    </style>
    """
    , unsafe_allow_html=True
)

# ---------- Hero ----------
with st.container():
    left, right = st.columns([3, 1])
    with left:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.title("Ng Poh Siang")
        st.markdown('<div class="hero-sub muted">Information Technology student majoring in Artificial Intelligence. Passionate about using AI to solve real-world problems.</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1.2,1,1.4])
        with c1:
            st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/ng-poh-siang-19b339253")
        with c2:
            st.link_button("✉️ Email", "mailto:ngpohsiang0955@gmail.com")
        with c3:
            st.download_button('📄 Download Resume', data=Path('/mnt/data/NG POH SIANG (5).pdf').read_bytes(), file_name='Ng_Poh_Siang_Resume.pdf')
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="metricbox">', unsafe_allow_html=True)
        st.caption("At a glance")
        m1, m2 = st.columns(2)
        with m1:
            st.metric("CGPA", "3.99")
        with m2:
            st.metric("MUET", "Band 4")
        st.write("📍 Johor Bahru, Malaysia")
        st.write("📱 010‑394 4463")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ---------- Summary ----------
st.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)
st.write(
    "Motivated IT undergraduate specializing in Artificial Intelligence with strong foundations in machine learning, "
    "data analysis and mobile development. Quick to learn new tools, comfortable collaborating in teams, and driven to deliver practical solutions."
)

# ---------- Skills ----------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.caption("Programming and Development")
    st.markdown(
        " ".join([
            '<span class="pill">Python</span>',
            '<span class="pill">Java</span>',
            '<span class="pill">Flutter</span>',
            '<span class="pill">Dart</span>',
        ]),
        unsafe_allow_html=True,
    )
    st.caption("Tools")
    st.markdown(
        " ".join([
            '<span class="pill">Git</span>',
            '<span class="pill">Android Studio</span>',
            '<span class="pill">VS Code</span>',
        ]),
        unsafe_allow_html=True,
    )
with col2:
    st.caption("AI and Data")
    st.markdown(
        " ".join([
            '<span class="pill">Machine Learning</span>',
            '<span class="pill">Data Analysis</span>',
            '<span class="pill">Model Evaluation</span>',
        ]),
        unsafe_allow_html=True,
    )
    st.caption("Backend and Cloud")
    st.markdown(
        " ".join([
            '<span class="pill">Firebase Auth</span>',
            '<span class="pill">Firestore</span>',
            '<span class="pill">Realtime Database</span>',
        ]),
        unsafe_allow_html=True,
    )
with col3:
    st.caption("Soft Skills")
    st.markdown(
        " ".join([
            '<span class="pill">Leadership</span>',
            '<span class="pill">Communication</span>',
            '<span class="pill">Problem Solving</span>',
            '<span class="pill">Teamwork</span>',
        ]),
        unsafe_allow_html=True,
    )

st.divider()

# ---------- Projects ----------
st.markdown('<div class="section-title">Selected Project</div>', unsafe_allow_html=True)

pc1, pc2 = st.columns([1,2])
with pc1:
    st.markdown("**Wasteless — Food Waste Reduction App**")
    st.caption("Cross-platform mobile app")
with pc2:
    st.markdown(
        """
        - Built an application connecting users with restaurants offering surplus food at discounted prices.
        - Implemented user authentication, browsing, notifications and order management using Firebase.
        - Focused on measurable impact through reduced food wastage and budget-friendly meals.
        """
    )

st.divider()

# ---------- Education ----------
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

ed1, ed2 = st.columns(2)
with ed1:
    st.markdown("**Universiti Malaysia Kelantan (UMK)**")
    st.write("Bachelor of Information Technology with Honours, Artificial Intelligence")
    st.caption("Sept 2022 — Sept 2026")
    st.write("Current CGPA 3.99")
with ed2:
    st.markdown("**SMK Taman Johor Jaya 1**")
    st.write("STPM")
    st.caption("Jan 2020 — Jul 2022")
    st.write("CGPA 3.67, MUET Band 4")

st.divider()

# ---------- Certifications ----------
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
st.markdown(
    """
- Microsoft Certified **Power BI Data Analyst Associate**
- Microsoft Certified **Azure AI Engineer Associate**
- Microsoft Certified **Azure AI Fundamentals**
- Huawei **HCIA Security**
    """
)

# ---------- Awards ----------
st.markdown('<div class="section-title">Awards and Achievements</div>', unsafe_allow_html=True)
st.markdown(
    """
- Gold Medal — International Research and Information Science Expo 2025 for Wasteless
- Silver Medal — Virtual Innovation Competition 2024 for Wasteless
- Third Place — Sidang Inovasi Belia Peringkat Kebangsaan 2023
    """
)

st.divider()

# ---------- Footer ----------
st.caption("© 2025  Ng Poh Siang")
