import streamlit as st


#----PAGE SETUP----

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

#---NAVIGATION SETUP----
pg = st.navigation(
    {
        "Home" : [page_1],
        "Info" : [page_2],
        "Statistics Do" : [page_3],
        }
    )

#----RUN NAVIGATION----
pg.run()

st.logo("picture/profile.png")
st.sidebar.text("Made With ❤️ by Ayun")