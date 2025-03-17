import streamlit as st
from .ai_tutor.model import get_ai_response
from ai_tutor.memory import memory

st.title("📊 AI Data Science Tutor")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me a Data Science question:")

if user_input:
    response = get_ai_response(user_input)
    st.session_state.chat_history.append((user_input, response))

for user_query, ai_response in st.session_state.chat_history:
    st.write(f"**You:** {user_query}")
    st.write(f"**AI:** {ai_response}")
