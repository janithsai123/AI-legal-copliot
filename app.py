import streamlit as st

st.title("⚖️ AI Legal Copilot")

user_input = st.text_input("Enter your legal query:")

if st.button("Run"):
    if user_input:
        response = f"""
Task Type: SMART_AGENT

Action:
Processing using AI Legal Agent

Response:
This request has been processed by the AI Legal Copilot system.

(User Query): {user_input}
        """
        st.text(response)