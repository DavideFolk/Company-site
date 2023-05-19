import streamlit as st
from send_email import send_email

with st.form(key='email_forms', clear_on_submit=True):
    user_email = st.text_input('Your email address')
    user_topic = st.selectbox('What topic do you want to discuss?', ('Job inquiries', 'Project Proposal', 'Other'))
    message = st.text_area('Text')
    message_final = f"""\
        Subject: New mail from {user_email}

        From: {user_email}
        Topic {user_topic}
        {message}
        """
    button = st.form_submit_button()
    if button:
        if not user_email:
            st.error('Email is required')
        elif not message:
            st.error('Text is required')
        else:
            send_email(message_final)
            st.info('Your email was sent successfully')