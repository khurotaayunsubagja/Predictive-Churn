import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Churn Analysis",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# PATH SETUP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "picture" / "profile.png"


# ============================================================
# LOGO
# ============================================================

if LOGO_PATH.exists():
    st.logo(LOGO_PATH)
else:
    st.sidebar.warning("Logo image not found.")


# ============================================================
# PAGE SETUP
# ============================================================

page_1 = st.Page(
    page="pages/home.py",
    title="Home",
    icon="🏚️",
    default=True,
)

page_2 = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)

page_3 = st.Page(
    page="pages/predict.py",
    title="Predict It!",
    icon="🧮",
)


# ============================================================
# NAVIGATION SETUP
# ============================================================

pg = st.navigation(
    {
        "Home": [page_1],
        "Info": [page_2],
        "Statistics Do": [page_3],
    }
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.text("Made With ❤️ by Ayun")


# ============================================================
# RUN NAVIGATION
# ============================================================

pg.run()
