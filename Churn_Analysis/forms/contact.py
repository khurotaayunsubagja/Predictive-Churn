import streamlit as st
import re
import requests


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Adress")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Message successfully sent!")
    
    if submit_button:
        if not name: 
            st.error("Please provide your name.", icon="😊")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="✉️")
            st.stop()
        
        if not is_valid_email(email):
            st.error("Please provide your name.", icon="😊")
            st.stop()

