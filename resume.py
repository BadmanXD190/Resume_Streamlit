
import streamlit as st

st.set_page_config(page_title="Ng Poh Siang — Resume", page_icon="📄", layout="centered")

# Header
st.title("Ng Poh Siang")
st.caption("Motivated IT student specializing in Artificial Intelligence, passionate about solving real world problems with AI.")

# Contact
with st.container():
    st.subheader("Contact")
    left, right = st.columns(2)
    with left:
        st.write("Johor Bahru, Malaysia")
        st.write("Phone 010-3944463")
    with right:
        st.write("Email ngpohsiang0955@gmail.com")
        st.write("[LinkedIn](https://www.linkedin.com/in/ng-poh-siang-19b339253)")

st.divider()

# Summary
st.subheader("Summary")
st.write(
    "Information Technology student majoring in Artificial Intelligence. Strong foundations in machine learning, "
    "data analysis and software development. Eager to contribute to innovative projects in dynamic environments."
)

st.divider()

# Education
st.subheader("Education")
st.markdown("**Bachelor of Information Technology with Honours, Artificial Intelligence**")
st.write("Universiti Malaysia Kelantan (UMK)")
st.write("September 2022 to September 2026")
st.write("Current CGPA 3.99")

st.markdown("**STPM**")
st.write("SMK Taman Johor Jaya 1")
st.write("January 2020 to July 2022")
st.write("CGPA 3.67, MUET Band 4")

st.divider()

# Certifications
st.subheader("Certifications")
st.write("- Microsoft Certified Power BI Data Analyst Associate")
st.write("- Microsoft Certified Azure AI Engineer Associate")
st.write("- Microsoft Certified Azure AI Fundamentals")
st.write("- Huawei HCIA Security Certification")

st.divider()

# Skills
st.subheader("Skills")
s1, s2 = st.columns(2)
with s1:
    st.markdown("**Programming and Development**")
    st.write("Python, Java, Flutter, Dart")
    st.markdown("**AI and Data Technologies**")
    st.write("Machine Learning basics, Data Analysis")
    st.markdown("**Database and Backend**")
    st.write("Firebase Authentication, Firestore, Realtime Database")
with s2:
    st.markdown("**Tools and Platforms**")
    st.write("Git, Android Studio, Visual Studio Code")
    st.markdown("**Soft Skills**")
    st.write("Leadership, Communication, Problem Solving, Team Management")

st.divider()

# Projects
st.subheader("Projects")
st.markdown("**Wasteless — Food Waste Reduction Mobile App**")
st.write(
    "- Built a cross platform app connecting users with restaurants offering surplus food at discounted prices.\n"
    "- Implemented user authentication, product browsing, real time notifications and order management using Firebase backend.\n"
    "- Promoted environmental sustainability through technology driven solutions."
)

st.divider()

# Awards
st.subheader("Awards and Achievements")
st.write("- Gold Medal, International Research and Information Science Expo 2025 for Wasteless")
st.write("- Silver Medal, Virtual Innovation Competition 2024 for Wasteless")
st.write("- Third Place, Sidang Inovasi Belia Peringkat Kebangsaan 2023")
