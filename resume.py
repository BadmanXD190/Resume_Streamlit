
import streamlit as st
from pathlib import Path
from base64 import b64encode

st.set_page_config(
    page_title="Ng Poh Siang — Portfolio Resume",
    page_icon="🧭",
    layout="wide"
)

# -------------------- Sidebar: Theme, Accent, Print --------------------
st.sidebar.header("Appearance")
theme = st.sidebar.radio("Theme", ["Light", "Dark"], index=0, horizontal=True)
accent = st.sidebar.selectbox("Accent", ["UMK Blue", "Royal Purple", "Emerald", "Sunset Orange"], index=0)
print_view = st.sidebar.toggle("Print-friendly view", value=st.session_state.get("print_view", False))
st.session_state["print_view"] = print_view

ACCENTS = {"UMK Blue":"#006ccd","Royal Purple":"#6f42c1","Emerald":"#2ecc71","Sunset Orange":"#ff7a00"}
accent_hex = ACCENTS.get(accent, "#006ccd")
is_dark = theme == "Dark"

# -------------------- Helper: resume + profile --------------------
def get_resume_bytes_or_url():
    for p in [Path("assets/resume.pdf"), Path("resume.pdf")]:
        if p.exists() and p.is_file():
            return p.read_bytes(), None
    resume_url = st.secrets.get("RESUME_URL") if hasattr(st, "secrets") else None
    if resume_url:
        return None, str(resume_url)
    return None, None

def get_profile_bytes():
    for name in ["assets/profile.jpg","assets/profile.png","profile.jpg","profile.png"]:
        p = Path(name)
        if p.exists() and p.is_file():
            return p.read_bytes()
    return None

# -------------------- Styles --------------------
if print_view:
    bg = "#ffffff"; surface = "#ffffff"; muted = "#4b5563"; text = "#111827"; border = "rgba(0,0,0,.18)"
    accent_hex = "#111827"  # neutral for print
else:
    bg = "#0f1116" if is_dark else "#f8fafc"
    surface = "#161a22" if is_dark else "#ffffff"
    muted = "#a7b0bd" if is_dark else "#6c757d"
    text = "#e6e9ef" if is_dark else "#1f2937"
    border = "rgba(255,255,255,.12)" if is_dark else "rgba(120,120,120,.25)"

css = f"""
<style>
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}
:root {{ --bg:{bg}; --surface:{surface}; --muted:{muted}; --text:{text}; --border:{border}; --accent:{accent_hex}; }}
.block-container {{ background: var(--bg); padding-top: 1.0rem; }}
h1,h2,h3,h4,h5,p,span,li,div,small {{ color: var(--text); }}
.section-title {{ font-weight: 800; font-size: 1.25rem; margin: .25rem 0 .75rem; letter-spacing:.2px; }}
.pill {{ display:inline-block; padding:7px 11px; border-radius:999px; border:1px solid var(--border); margin:4px 6px 0 0; font-size:.92rem; background:transparent; }}
.card {{ border:1px solid var(--border); border-radius:18px; padding:1rem; margin-bottom:.9rem; background: var(--surface); }}
.card-accent {{ border-left: 5px solid var(--accent); }}
.hero {{ border-radius: 18px; padding: 1.25rem 1.25rem; background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 16%, var(--surface)), var(--surface)); border: 1px solid var(--border); margin-bottom: .75rem; }}
.hero h1 {{ margin: 0; }}
.hero-sub {{ color: var(--muted); font-size: 1.05rem; margin-top: .35rem; }}
.metricbox {{ border-radius: 14px; padding:.9rem 1rem; border:1px solid var(--border); background: var(--surface); }}
.btn-row .stButton>button, .stLinkButton>button {{ border-radius: 999px; padding:.5rem .9rem; border:1px solid var(--border); }}
.grid-2 {{ display:grid; gap:14px; grid-template-columns: repeat(2, minmax(0, 1fr)); }}
.grid-3 {{ display:grid; gap:14px; grid-template-columns: repeat(3, minmax(0, 1fr)); }}
/* Foldable (collapsible) cards using <details> */
.fold-card {{ border:1px solid var(--border); border-left:5px solid var(--accent); border-radius:14px; background: var(--surface); margin-bottom:12px; }}
.fold-card summary {{ list-style:none; cursor:pointer; padding: .85rem 1rem; }}
.fold-card summary::-webkit-details-marker {{ display:none; }}
.fold-header {{ display:flex; flex-direction:column; gap:.15rem; }}
.fold-title {{ font-weight:700; }}
.fold-sub {{ color: var(--muted); font-size:.95rem; }}
.fold-body {{ padding: .35rem 1rem 1rem 1rem; }}
/* Print view overrides */
@media print {{
  .sidebar, .stSidebar {{ display:none !important; }}
  .grid-2, .grid-3 {{ grid-template-columns: 1fr !important; gap:10px; }}
  .btn-row, .metricbox {{ display:none !important; }}
}}
{'.grid-2, .grid-3 { grid-template-columns: 1fr !important; gap:10px; }' if print_view else ''}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# -------------------- Hero --------------------
with st.container():
    l, r = st.columns([3, 1], gap="large")
    with l:
        if print_view:
            st.subheader("Ng Poh Siang")
        else:
            st.markdown('<div class="hero">', unsafe_allow_html=True)
            a1, a2 = st.columns([1, 3], vertical_alignment="center")
            with a1:
                pb = get_profile_bytes()
                if pb:
                    st.markdown(f'<img style="width:110px;height:110px;border-radius:999px;border:2px solid var(--border);object-fit:cover;" src="data:image/png;base64,{b64encode(pb).decode()}">', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="display:flex;align-items:center;justify-content:center;width:110px;height:110px;border-radius:999px;border:2px solid var(--border);background:var(--surface);font-size:2.2rem;">NP</div>', unsafe_allow_html=True)
            with a2:
                st.header("Ng Poh Siang")
                st.markdown('<div class="hero-sub">AI & IoT enthusiast. IT undergraduate. Sustainable tech innovator.</div>', unsafe_allow_html=True)
                st.markdown('<div class="btn-row">', unsafe_allow_html=True)
                c1, c2, c3, c4 = st.columns([1.1,1,1,1.4])
                with c1: st.link_button("LinkedIn", "https://www.linkedin.com/in/ng-poh-siang-19b339253")
                with c2: st.link_button("GitHub", "https://github.com/BadmanXD190")
                with c3: st.link_button("Email", "mailto:ngpohsiang0955@gmail.com")
                with c4:
                    resume_bytes, resume_url = get_resume_bytes_or_url()
                    if resume_bytes: st.download_button("Download Resume", data=resume_bytes, file_name="Ng_Poh_Siang_Resume.pdf")
                    elif resume_url: st.link_button("View Resume", resume_url)
                    else: st.caption("Add assets/resume.pdf or set RESUME_URL in Secrets to enable resume button.")
                st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with r:
        if not print_view:
            st.markdown('<div class="metricbox">', unsafe_allow_html=True)
            st.caption("At a glance")
            m1, m2 = st.columns(2)
            with m1: st.metric("CGPA", "3.99")
            with m2: st.metric("Awards", "3+")
            m3, m4 = st.columns(2)
            with m3: st.metric("Projects", "10+")
            with m4: st.metric("Certs", "5+")
            st.markdown('<hr/>', unsafe_allow_html=True)
            st.write("📍 Johor Bahru, Malaysia")
            st.write("📱 010-394 4463")
            st.markdown('</div>', unsafe_allow_html=True)

if print_view:
    st.info("Print-friendly view is ON. Use your browser's **Print** then **Save as PDF** to export.")

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Summary --------------------
st.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)
st.write(
    "Motivated IT student specializing in Artificial Intelligence with strong foundations in machine learning, data analysis and mobile development. "
    "Comfortable building end-to-end solutions that combine Flutter front ends, Firebase back ends and data-driven logic. "
    "Experienced in innovation competitions with multiple awards and leadership roles. Keen to contribute to projects with real impact."
)

# -------------------- Skills --------------------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
sk1, sk2, sk3 = st.columns(3)
with sk1:
    st.caption("Programming")
    st.markdown(" ".join(['<span class="pill">Python</span>','<span class="pill">Java</span>','<span class="pill">Flutter</span>','<span class="pill">Dart</span>','<span class="pill">SQL</span>']), unsafe_allow_html=True)
    st.caption("Tools")
    st.markdown(" ".join(['<span class="pill">Git</span>','<span class="pill">Android Studio</span>','<span class="pill">VS Code</span>','<span class="pill">Figma</span>','<span class="pill">Canva</span>','<span class="pill">CapCut</span>']), unsafe_allow_html=True)
with sk2:
    st.caption("AI & Data")
    st.markdown(" ".join(['<span class="pill">Machine Learning</span>','<span class="pill">Data Analysis</span>','<span class="pill">Forecasting</span>','<span class="pill">Computer Vision</span>','<span class="pill">Model Evaluation</span>']), unsafe_allow_html=True)
    st.caption("Cloud & Backend")
    st.markdown(" ".join(['<span class="pill">Firebase Auth</span>','<span class="pill">Firestore</span>','<span class="pill">Realtime DB</span>','<span class="pill">Google APIs</span>']), unsafe_allow_html=True)
with sk3:
    st.caption("IoT & Hardware")
    st.markdown(" ".join(['<span class="pill">Arduino</span>','<span class="pill">ESP32</span>','<span class="pill">Sensors</span>','<span class="pill">Actuators</span>']), unsafe_allow_html=True)
    st.caption("Soft Skills")
    st.markdown(" ".join(['<span class="pill">Leadership</span>','<span class="pill">Public Speaking</span>','<span class="pill">Teamwork</span>','<span class="pill">Problem Solving</span>']), unsafe_allow_html=True)

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Projects: Foldable Cards --------------------
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

def fold_card(title:str, subtitle:str, points:list, open_default:bool=False):
    items = "".join([f"<li>{p}</li>" for p in points])
    st.markdown(f'''
<details class="fold-card" {'open' if open_default else ''}>
  <summary>
    <div class="fold-header">
      <div class="fold-title">{title}</div>
      <div class="fold-sub">{subtitle}</div>
    </div>
  </summary>
  <div class="fold-body">
    <ul>{items}</ul>
  </div>
</details>
''', unsafe_allow_html=True)

fold_card("Wasteless — Food Waste Reduction App", "Cross platform mobile app", [
    "Connects users with restaurants offering surplus food at discounted prices.",
    "Built with Flutter and Firebase for auth, browsing, notifications and orders.",
    "Focus on measurable impact by reducing food wastage."
], open_default=print_view)

fold_card("NestWorks — Automated Poultry Management", "IoT system", [
    "Smart feeding silo with load cells, motors and Firebase dashboard.",
    "Tracks feed levels and poultry weight to reduce waste and improve yield.",
    "Aligned with UMK entrepreneurial programs."
], open_default=print_view)

fold_card("EcoWatch — AI Water Quality Monitoring", "ML + IoT + dashboard", [
    "Predicts Water Quality Index using pH, turbidity and TDS sensors.",
    "Provides real time monitoring and forecasting dashboards.",
    "Represented UMK in Huawei ICT competition."
], open_default=print_view)

fold_card("Rebooted — Digital Habit Reset and Tasks", "FYP mobile app", [
    "Screen time tracking, app blocking and reward system for better habits.",
    "Task breakdown and progress tracking flow.",
    "Built with FlutterFlow and Firebase."
], open_default=print_view)

fold_card("PlayMasjid — Smart Prayer Companion", "Android app", [
    "Prayer times homepage, Qibla, Al-Qur’an audio and nearby mosque finder.",
    "Uses geolocation and public APIs where available.",
    "Designed for reliable mobile UX."
], open_default=print_view)

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Experience & Leadership --------------------
st.markdown('<div class="section-title">Experience & Leadership</div>', unsafe_allow_html=True)
fold_card("Innovation & Entrepreneurship", "Competitions & showcases", [
    "Huawei ICT, MRANTI Future Mobility, Lion’s Lair and Trailblazer Cup at FSDK.",
    "Led and coordinated teams across AI, IoT and app development tracks.",
    "Delivered pitches, demos and documentation aligned with judging rubrics."
], open_default=print_view)

fold_card("Student Projects & Collaboration", "Team-based delivery", [
    "ML projects including breast cancer detection and FBMKLCI forecasting.",
    "Agile with Scrum, sprint planning and Gantt timelines.",
    "Built dashboards and prototypes with Firebase and Streamlit."
], open_default=print_view)

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Education --------------------
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
fold_card("Universiti Malaysia Kelantan", "Bachelor of Information Technology (AI) — Sept 2022 to Sept 2026", [
    "Current CGPA 3.99."
], open_default=print_view)
fold_card("SMK Taman Johor Jaya 1", "STPM — Jan 2020 to Jul 2022", [
    "CGPA 3.67, MUET Band 4."
], open_default=print_view)

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Certifications --------------------
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
fold_card("Microsoft Certifications", "Power BI Data Analyst Associate; Azure AI Engineer Associate", [], open_default=print_view)
fold_card("More Certifications", "Azure AI Fundamentals; Huawei HCIA Security", [], open_default=print_view)

st.markdown('<hr/>', unsafe_allow_html=True)

# -------------------- Awards --------------------
st.markdown('<div class="section-title">Awards</div>', unsafe_allow_html=True)
fold_card("Major Awards", "Highlights", [
    "🥇 Gold — International Research and Information Science Expo 2025 (Wasteless).",
    "🥈 Silver — Virtual Innovation Competition 2024 (Wasteless)."
], open_default=print_view)
fold_card("More Achievements", "Leadership & representation", [
    "🥉 Third Place — Sidang Inovasi Belia Peringkat Kebangsaan 2023.",
    "Represented UMK at Trailblazer Cup @ FSDK 2025."
], open_default=print_view)

# -------------------- Languages & Hobbies --------------------
st.markdown('<hr/>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Languages</div>', unsafe_allow_html=True)
st.markdown(" ".join([
    '<span class="pill">Mandarin — Native</span>',
    '<span class="pill">English — Fluent</span>',
    '<span class="pill">Malay — Fluent</span>',
    '<span class="pill">Japanese — Basic</span>',
]), unsafe_allow_html=True)

st.markdown('<div class="section-title">Hobbies</div>', unsafe_allow_html=True)
st.markdown(" ".join([
    '<span class="pill">Coding</span>',
    '<span class="pill">Gaming</span>',
    '<span class="pill">Digital Content Creation</span>',
    '<span class="pill">Japanese Language & Culture</span>',
]), unsafe_allow_html=True)

st.caption("© 2025  Ng Poh Siang")
