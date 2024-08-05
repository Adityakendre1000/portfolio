import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key = "contact_form"):
    user_email = st.text_input("Your email address")
    user_messgae = st.text_area("Message")
    button = st.form_submit_button("Submit")

    if button:
        message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_messgae}
"""
        send_email(message)
        st.info("Email was sent successfully!🎉🎉")