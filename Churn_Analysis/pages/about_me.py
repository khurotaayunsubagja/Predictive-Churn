import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

st.set_page_config(
    page_title="About Me",
    page_icon="👤",
)

#----Hero Section----
col1,col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./picture/profile7.png", width=400)

with col2:
    st.title("Khurotaayun Pesona Subagja", anchor=False)
    st.write(
        "Data Enthusiast | Data Analyst | Undergradate Business Statistic | Seeking for internship opportunity"
    )

    if st.button("📩 Contact Me!"):
        show_contact_form()

#---Experience & Qualifications---
st.write("\n")
st.subheader("💼 Experience & Qualifications", anchor=False)
st.write(
    """
    - Teaching Assistant for Database Management course, mentoring students in database concepts and SQL.
    - Developed a Tourism Dashboard 2024 for the Department of Culture and Tourism of East Java Province.
    - Built a Driver Drowsiness Detection System using computer vision (YOLO) to enhance road safety.
    - Proficient in Python, SQL, Excel, and data visualization tools (Power BI, Tableau, Plotly).
    - Strong foundation in statistical principles, predictive modeling, and effective teamwork.
      """
)

#---Skills---
st.write("\n")
st.subheader("🛠️ Hard Skills", anchor=False)
st.write(
    """
    - 💻 Programming : Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visualization : Power Bi, Tableau, Looker Studio
    - 🎛️  Modelling : Logistic Regression, Linear Regression, Decision Trees
    - 🗄️ Databases : Postgres, MySQL
    - 📈 Statistical Analysis: Hypothesis Testing, Regression, Data Cleaning
    """

)
