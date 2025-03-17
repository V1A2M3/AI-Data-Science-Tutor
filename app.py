import streamlit as st
from ai_tutor.model import get_ai_response
from ai_tutor.memory import memory

# ---- PAGE CONFIG ----
st.set_page_config(page_title="📊 AI Data Science Tutor", page_icon="🤖", layout="wide")

st.title("📊 AI Data Science Tutor")

# ---- CHAT HISTORY STATE ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- DISPLAY ANSWERS FIRST ----
st.subheader("📝 Chat History")
for user_query, ai_response in reversed(st.session_state.chat_history):  # Reverse order
    st.write(f"**👨‍💻 You:** {user_query}")
    st.write(f"**🤖 AI:** {ai_response}")
    st.markdown("---")  # Separator for better readability

# ---- QUESTION INPUT AT BOTTOM ----
user_input = st.text_input("Ask me a Data Science question:", key="user_input")

if user_input:
    response = get_ai_response(user_input)
    st.session_state.chat_history.append((user_input, response))
    
    # Clear input box after sending message
    st.experimental_rerun()
