import streamlit as st
import subprocess
from ai_tutor.model import get_ai_response
from ai_tutor.memory import memory
import time

# Page layout
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🤖", layout="wide")

# Custom chat styles
st.markdown("""
    <style>
    .user-message { background-color: #1E88E5; padding: 10px; border-radius: 10px; color: white; margin-bottom: 10px; }
    .bot-message { background-color: #f1f1f1; padding: 10px; border-radius: 10px; color: black; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Data Science Tutor")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Dark Mode Toggle
theme = st.radio("Choose Theme:", ["🌞 Light", "🌙 Dark"])
if theme == "🌙 Dark":
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: white; }
        .user-message { background-color: #1E88E5; color: white; }
        .bot-message { background-color: #333; color: white; }
        </style>
        """, unsafe_allow_html=True)

# AI Personality Selection
personality = st.selectbox("Choose AI Personality:", ["🎓 Professor", "😃 Friendly", "📈 Business"])

# User input
user_input = st.text_input("Ask a Data Science question:", placeholder="e.g., What is linear regression?")

if user_input:
    # Apply personality
    if personality == "🎓 Professor":
        prompt = "Explain like a university professor: " + user_input
    elif personality == "😃 Friendly":
        prompt = "Explain in a fun and simple way: " + user_input
    else:
        prompt = "Explain in a professional and business-oriented style: " + user_input

    # Show user message
    st.markdown(f'<div class="user-message">👨‍💻 You: {user_input}</div>', unsafe_allow_html=True)
    
    # Simulate typing effect
    with st.spinner("Thinking..."):
        time.sleep(2)
        response = get_ai_response(prompt)
    
    # Display AI response
    st.markdown(f'<div class="bot-message">🤖 AI: {response}</div>', unsafe_allow_html=True)

    # Save chat history
    st.session_state.chat_history.append(("👨‍💻 You", user_input))
    st.session_state.chat_history.append(("🤖 AI", response))

# Display chat history
st.subheader("Chat History 📜")
for role, message in st.session_state.chat_history:
    st.markdown(f'<div class="{ "user-message" if role == "👨‍💻 You" else "bot-message" }">{role}: {message}</div>', unsafe_allow_html=True)

