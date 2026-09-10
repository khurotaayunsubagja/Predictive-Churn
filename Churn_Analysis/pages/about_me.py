import streamlit as st
from pathlib import Path

from forms.contact import contact_form


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="About Me",
    page_icon="👤",
)


# ============================================================
# PATH CONFIG
# ============================================================

# Lokasi folder utama project
BASE_DIR = Path(__file__).resolve().parent.parent

# Lokasi profile picture
PROFILE_IMAGE = BASE_DIR / "picture" / "profile7.png"


# ============================================================
# CONTACT FORM
# ============================================================

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# ============================================================
# HERO SECTION
# ============================================================

col1, col2 = st.columns(
    2,
    gap="small",
    vertical_alignment="center"
)

with col1:
    if PROFILE_IMAGE.exists():
        st.image(PROFILE_IMAGE, width=400)
    else:
        st.error(f"Profile image not found: {PROFILE_IMAGE}")


with col2:

    st.title(
        "Khurotaayun Pesona Subagja",
        anchor=False
    )

    st.write(
        "Data Enthusiast | Data Analyst | "
        "Business Statistics Graduate | "
        "Seeking Data Analytics Opportunities"
    )

    if st.button("📩 Contact Me!"):
        show_contact_form()


# ============================================================
# EXPERIENCE & QUALIFICATIONS
# ============================================================

st.write("\n")

st.subheader(
    "💼 Experience & Qualifications",
    anchor=False
)

st.write(
    """
    - Teaching Assistant for Database Management course, mentoring students in database concepts and SQL.
    - Developed a Tourism Dashboard 2024 for the Department of Culture and Tourism of East Java Province.
    - Built a Driver Drowsiness Detection System using computer vision (YOLO) to enhance road safety.
    - Proficient in Python, SQL, Excel, and data visualization tools (Power BI, Tableau, Plotly).
    - Strong foundation in statistical principles, predictive modeling, and effective teamwork.
    """
)


# ============================================================
# HARD SKILLS
# ============================================================

st.write("\n")

st.subheader(
    "🛠️ Hard Skills",
    anchor=False
)

st.write(
    """
    - 💻 **Programming:** Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 **Data Visualization:** Power BI, Tableau, Looker Studio
    - 🎛️ **Modelling:** Logistic Regression, Linear Regression, Decision Trees
    - 🗄️ **Databases:** PostgreSQL, MySQL
    - 📈 **Statistical Analysis:** Hypothesis Testing, Regression, Data Cleaning
    """
)
