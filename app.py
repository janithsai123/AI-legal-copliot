import streamlit as st

# Title
st.title("⚖️ AI Legal Copilot")

# Input
user_input = st.text_input("Enter your legal query:")

# Button logic
if st.button("Run"):
    if user_input:

        # Convert input to lowercase
        query = user_input.lower()

        # Logic handling
        if "rental" in query:
            response = """
### Task Type: SUMMARIZATION

**Action:**  
Simplifying legal document

**Response:**  
A rental agreement is a contract between a landlord and tenant. It defines the rent amount, duration of stay, and responsibilities of both parties. It ensures both sides follow agreed terms and protects their rights.
"""

        elif "email" in query or "complaint" in query:
            response = """
### Task Type: EMAIL

**Action:**  
Generating legal email

**Response:**  

**Subject:** Complaint Regarding Water Issue  

Dear Sir/Madam,  

I am writing to bring to your attention the ongoing water issue in my residence. This problem has been causing inconvenience in daily activities.  

I kindly request you to address and resolve this issue at the earliest.  

Thank you for your prompt attention.  

Sincerely,  
[Your Name]
"""

        elif "steps" in query or "process" in query:
            response = """
### Task Type: TASK_PLANNING

**Action:**  
Providing legal guidance

**Response:**  
1. Clearly identify the issue  
2. Collect necessary documents and evidence  
3. Draft a formal complaint  
4. Submit it to the appropriate authority  
5. Follow up regularly for updates  
"""

        else:
            response = f"""
### Task Type: GENERAL_QUERY

**Action:**  
Processing request

**Response:**  
This request has been processed by the AI Legal Copilot system.

**User Query:** {user_input}
"""

        # Display output
        st.markdown(response)

    else:
        st.warning("Please enter a query before clicking Run.")
