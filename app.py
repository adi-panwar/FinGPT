import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Page config
st.set_page_config(
    page_title="Financial AI Assistant",
    page_icon="💰",
    layout="centered"
)

# Load environment variables
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Title and description
st.title("💰 Financial AI Assistant")
st.markdown("""
This AI assistant specializes in providing accurate and insightful responses to your financial questions.
Ask anything about finance, investments, markets, or personal finance!
""")

# Create a text input for the user's question
user_question = st.text_area("What would you like to know about finance?", 
                            placeholder="e.g., What are the best investment strategies for beginners?")

# Add a submit button
if st.button("Get Answer"):
    if user_question:
        with st.spinner("Thinking..."):
            # Prepare the prompt
            prompt = f"if you are a financial expert AI assistant. your task is to provide accurate and insightful response to the following user query related to finance: {user_question}. for any other topic, respond with i don't know"
            
            # Get the response from Groq
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            
            # Display the response
            st.markdown("### Answer:")
            st.write(chat_completion.choices[0].message.content)
    else:
        st.warning("Please enter a question first!")

# Add some helpful tips
with st.expander("💡 Tips for better results"):
    st.markdown("""
    - Be specific in your questions
    - Include relevant context when needed
    - Ask about specific financial topics like:
        - Investment strategies
        - Market analysis
        - Personal finance
        - Banking
        - Taxes
        - Retirement planning
    """) 