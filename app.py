import streamlit as st
from customer_support_agent import CustomerSupportAgent, KNOWLEDGE_BASE, INTENT_KEYWORDS

st.title("🤖 Customer Support Agent")

st.write("Ask your customer support question below.")

agent = CustomerSupportAgent(KNOWLEDGE_BASE, INTENT_KEYWORDS)

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question:
        intent = agent.classify_intent(question)
        response = agent.generate_response(intent)

        st.write("### Detected Intent")
        st.info(intent)

        st.write("### Agent Response")
        st.success(response)
    else:
        st.warning("Please enter a question.")
