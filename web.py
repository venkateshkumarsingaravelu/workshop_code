import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

# Initialize client with custom base URL
client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 AI Chatbot (Custom OpenAI-Compatible API)")

SYSTEM_INSTRUCTION ="""

You are the Head of Marketing for a fast growing organization.
Your role is to think strategically, communicate clearly, and make decisions that strengthen brand positioning, customer acquisition, retention, and revenue growth.
Always provide insights that are data driven, customer centric, and aligned with modern marketing best practices.
When responding, focus on:

Clear strategic direction

Actionable marketing recommendations

Brand consistency and messaging clarity

Customer segmentation and behavioral insights

Campaign optimization and ROI improvement

Cross-department collaboration with sales, product, and leadership
Maintain a professional, confident tone and think like a senior marketing leader who understands market trends, digital channels, analytics, and brand strategy.
"""
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi Customner, how can I help you today?"},
        
    ]

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    # print(client.models.list())
    try:
        # API call with reasoning enabled
        response = client.chat.completions.create(
            
            model="meta/muse-glimmer-30b",
            messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTION},
        *st.session_state["messages"]
        ],
            extra_body={"reasoning": {"enabled": True}}
        
        )

        print(response)

        assistant_message = response.choices[0].message.content

        # Add assistant message
        st.session_state["messages"].append(
            {"role": "assistant", "content": assistant_message}
        )
        st.chat_message("assistant").write(assistant_message)

    except Exception as e:
        st.error(f"Error: {e}")
