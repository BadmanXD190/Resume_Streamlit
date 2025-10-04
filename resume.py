
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Ng Poh Siang - Portfolio Resume",
    page_icon="🧭",
    layout="wide"
)

# ---------- Helper: locate resume PDF or URL ----------
def get_resume_bytes_or_url():
    candidates = [Path("assets/resume.pdf"), Path("resume.pdf")]
    for p in candidates:
        if p.exists() and p.is_file():
            return p.read_bytes(), None
    resume_url = st.secrets.get("RESUME_URL") if hasattr(st, "secrets") else None
    if resume_url:
        return None, str(resume_url)
    return None, None

# ---------- Styles ----------
st.markdown(
    """
    <style>
    .pill {
        display:inline-block; padding:6px 10px; border-radius:999px;
        border:1px solid rgba(120,120,120,.25); margin:4px 6px 0 0;
        font-size:0.90rem
    }
    .section-title {
        font-weight:700; font-size:1.25rem; margin: 0.5rem 0 0.75rem 0;
    }
    .card {
        border:1px solid rgba(120,120,120,.25);
        border-radius:16px; padding:1rem; margin-bottom:0.75rem;
        background: rgba(250,250,250,.6);
    }
    .muted { color: #6c757d; }
    .hero h1 { margin-bottom: .25rem; }
    .hero-sub { font-size: 1.05rem; }
    .metricbox {
        border-radius: 14px; padding:.75rem 1rem; border:1px solid rgba(120,120,120,.2);
    }
    .grid-2 { display: grid; gap: 12px; grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .grid-3 { display: grid; gap: 12px; grid-template-columns: repeat(3, minmax(0, 1fr)); }
    @media (max-width: 900px) {
        .grid-2, .grid-3 { grid-template-columns: 1fr; }
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
        st.markdown(
            '<div class="hero-sub muted">AI and IoT enthusiast - IT undergraduate - Sustainable tech innovator</div>',
            unsafe_allow_html=True
        )

        resume_bytes, resume_url = get_resume_bytes_or_url()
        c1, c2, c3, c4 = st.columns([1.1,1,1,1.4])
        with c1:
            st.link_button("LinkedIn", "https://www.linkedin.com/in/ng-poh-siang-19b339253")
        with c2:
            st.link_button("GitHub", "https://github.com/")
        with c3:
            st.link_button("Email", "mailto:ngpohsiang0955@gmail.com")
        with c4:
            if resume_bytes:
                st.download_button("Download Resume", data=resume_bytes, file_name="Ng_Poh_Siang_Resume.pdf")
            elif resume_url:
                st.link_button("View Resume", resume_url)
            else:
                st.caption("Add assets/resume.pdf or set RESUME_URL in Secrets to enable resume button.")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="metricbox">', unsafe_allow_html=True)
        st.caption("At a glance")
        m1, m2 = st.columns(2)
        with m1:
            st.metric("CGPA", "3.99")
        with m2:
            st.metric("Awards", "3+")
        mc1, mc2 = st.columns(2)
        with mc1:
            st.metric("Projects", "10+")
        with mc2:
            st.metric("Certs", "5+")
        st.write("Johor Bahru, Malaysia")
        st.write("010-394 4463")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ---------- Summary ----------
st.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)
st.write(
    "Motivated IT student specializing in Artificial Intelligence with strong foundations in machine learning, data analysis and mobile development. "
    "Comfortable building end-to-end solutions that combine Flutter front ends, Firebase back ends and data-driven logic. "
    "Experienced in innovation competitions with multiple awards. Keen to contribute to projects with real impact."
)

# ---------- Skills ----------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("Programming")
    st.markdown(" ".join([
        '<span class="pill">Python</span>',
        '<span class="pill">Java</span>',
        '<span class="pill">Flutter</span>',
        '<span class="pill">Dart</span>',
        '<span class="pill">SQL</span>',
    ]), unsafe_allow_html=True)
    st.caption("Tools")
    st.markdown(" ".join([
        '<span class="pill">Git</span>',
        '<span class="pill">Android Studio</span>',
        '<span class="pill">VS Code</span>',
        '<span class="pill">Figma</span>',
        '<span class="pill">Canva</span>',
        '<span class="pill">CapCut</span>',
    ]), unsafe_allow_html=True)

with col2:
    st.caption("AI and Data")
    st.markdown(" ".join([
        '<span class="pill">Machine Learning</span>',
        '<span class="pill">Data Analysis</span>',
        '<span class="pill">Forecasting</span>',
        '<span class="pill">Computer Vision</span>',
        '<span class="pill">Model Evaluation</span>',
    ]), unsafe_allow_html=True)
    st.caption("Cloud and Backend")
    st.markdown(" ".join([
        '<span class="pill">Firebase Auth</span>',
        '<span class="pill">Firestore</span>',
        '<span class="pill">Realtime Database</span>',
        '<span class="pill">Google APIs</span>',
    ]), unsafe_allow_html=True)

with col3:
    st.caption("IoT and Hardware")
    st.markdown(" ".join([
        '<span class="pill">Arduino</span>',
        '<span class="pill">ESP32</span>',
        '<span class="pill">Sensors</span>',
        '<span class="pill">Actuators</span>',
    ]), unsafe_allow_html=True)
    st.caption("Soft Skills")
    st.markdown(" ".join([
        '<span class="pill">Leadership</span>',
        '<span class="pill">Public Speaking</span>',
        '<span class="pill">Teamwork</span>',
        '<span class="pill">Problem Solving</span>',
    ]), unsafe_allow_html=True)

st.divider()

# ---------- Projects (Cards) ----------
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

st.markdown('<div class="grid-2">', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  <h4>Wasteless - Food Waste Reduction App</h4>
  <p class="muted">Cross platform mobile app</p>
  <ul>
    <li>Connects users with restaurants offering surplus food at discounted prices.</li>
    <li>Built with Flutter and Firebase for auth, browsing, notifications and orders.</li>
    <li>Focus on impact through reduced food wastage and budget friendly meals.</li>
  </ul>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  <h4>NestWorks - Automated Poultry Management</h4>
  <p class="muted">IoT system</p>
  <ul>
    <li>Smart feeding silo using load cells, motors and Firebase dashboard.</li>
    <li>Tracks feed levels and poultry weight automatically to reduce waste.</li>
    <li>Aligned with UMK entrepreneurial programs.</li>
  </ul>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  <h4>EcoWatch - AI Water Quality Monitoring</h4>
  <p class="muted">ML + IoT + dashboard</p>
  <ul>
    <li>Predicts Water Quality Index using pH, turbidity and TDS sensors.</li>
    <li>Provides real time monitoring and forecasting dashboards.</li>
    <li>Represented UMK in Huawei ICT competition.</li>
  </ul>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  <h4>Rebooted - Digital Habit Reset and Tasks</h4>
  <p class="muted">FYP mobile app</p>
  <ul>
    <li>Screen time tracking, app blocking and reward system for better habits.</li>
    <li>Task breakdown and progress tracking flow.</li>
    <li>Built with FlutterFlow and Firebase.</li>
  </ul>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  <h4>PlayMasjid - Smart Prayer Companion</h4>
  <p class="muted">Android app</p>
  <ul>
    <li>Prayer times homepage, Qibla, Al Quran audio and nearby mosque finder.</li>
    <li>Uses geolocation and public APIs where available.</li>
    <li>Designed for clarity and reliability on mobile devices.</li>
  </ul>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ---------- Experience and Leadership (Cards) ----------
st.markdown('<div class="section-title">Experience and Leadership</div>', unsafe_allow_html=True)
st.markdown('''
<div class="grid-2">
  <div class="card">
    <h4>Innovation and Entrepreneurship</h4>
    <ul>
      <li>Competed in Huawei ICT, MRANTI Future Mobility, Lion's Lair and Trailblazer Cup at FSDK.</li>
      <li>Led and coordinated project teams across AI, IoT and app development tracks.</li>
      <li>Delivered pitches, demos and documentation aligned to judging rubrics.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Student Projects and Collaboration</h4>
    <ul>
      <li>Worked on ML projects like breast cancer detection and FBMKLCI forecasting.</li>
      <li>Practiced Agile with Scrum, including sprint planning and Gantt timelines.</li>
      <li>Built dashboards and prototypes with Firebase and Streamlit.</li>
    </ul>
  </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ---------- Education (Cards) ----------
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
st.markdown('''
<div class="grid-2">
  <div class="card">
    <h4>Universiti Malaysia Kelantan - Bachelor of Information Technology, Artificial Intelligence</h4>
    <p class="muted">Sept 2022 - Sept 2026</p>
    <p>Current CGPA 3.99</p>
  </div>
  <div class="card">
    <h4>SMK Taman Johor Jaya 1 - STPM</h4>
    <p class="muted">Jan 2020 - Jul 2022</p>
    <p>CGPA 3.67, MUET Band 4</p>
  </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ---------- Certifications (Cards) ----------
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
st.markdown('''
<div class="grid-2">
  <div class="card">
    <ul>
      <li>Microsoft Certified Power BI Data Analyst Associate</li>
      <li>Microsoft Certified Azure AI Engineer Associate</li>
    </ul>
  </div>
  <div class="card">
    <ul>
      <li>Microsoft Certified Azure AI Fundamentals</li>
      <li>Huawei HCIA Security</li>
    </ul>
  </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ---------- Awards (Cards) ----------
st.markdown('<div class="section-title">Awards</div>', unsafe_allow_html=True)
st.markdown('''
<div class="grid-2">
  <div class="card">
    <ul>
      <li>Gold medal - International Research and Information Science Expo 2025 for Wasteless</li>
      <li>Silver medal - Virtual Innovation Competition 2024 for Wasteless</li>
    </ul>
  </div>
  <div class="card">
    <ul>
      <li>Third place - Sidang Inovasi Belia Peringkat Kebangsaan 2023</li>
      <li>Represented UMK at Trailblazer Cup at FSDK 2025</li>
    </ul>
  </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ---------- Languages and Hobbies ----------
st.markdown('<div class="section-title">Languages</div>', unsafe_allow_html=True)
st.markdown(" ".join([
    '<span class="pill">Mandarin - Native</span>',
    '<span class="pill">English - Fluent</span>',
    '<span class="pill">Malay - Fluent</span>',
    '<span class="pill">Japanese - Basic</span>',
]), unsafe_allow_html=True)

st.markdown('<div class="section-title">Hobbies</div>', unsafe_allow_html=True)
st.markdown(" ".join([
    '<span class="pill">Coding</span>',
    '<span class="pill">Gaming</span>',
    '<span class="pill">Digital Content Creation</span>',
    '<span class="pill">Japanese Language and Culture</span>',
]), unsafe_allow_html=True)

st.divider()

# ---------- Footer ----------
st.caption("© 2025  Ng Poh Siang")
