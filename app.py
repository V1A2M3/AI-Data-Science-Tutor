import streamlit as st
from ai_tutor.model import get_ai_response

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🤖", layout="wide")

# ---- CHAT HISTORY STATE ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- USER INPUT ----
user_input = st.text_input("Ask a Data Science question:", placeholder="e.g., What is linear regression?", key="user_input")

if user_input:
    # Get AI response instantly
    response = get_ai_response(user_input)

    # Save to chat history
    st.session_state.chat_history.append(("👨‍💻 You", user_input))
    st.session_state.chat_history.append(("🤖 AI", response))

    # Clear input box after sending message
    st.session_state.user_input = ""

# ---- DISPLAY CHAT HISTORY ----
st.subheader("📜 Chat History")
for role, message in st.session_state.chat_history:
    st.write(f"**{role}:** {message}")
