import streamlit as st
from ai_tutor.model import get_ai_response

st.set_page_config(page_title="📊 AI Data Science Tutor", page_icon="🤖", layout="wide")
st.title("📊 AI Data Science Tutor")

# ---- Initialize Chat History ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- Display Answers First ----
st.subheader("📝 Chat History")
for user_query, ai_response in reversed(st.session_state.chat_history):  
    st.write(f"**👨‍💻 You:** {user_query}")
    st.write(f"**🤖 AI:** {ai_response}")
    st.markdown("---")

# ---- User Input at Bottom with Form ----
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask me a Data Science question:", key="user_input")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    response = get_ai_response(user_input)
    st.session_state.chat_history.append(("👨‍💻 You", user_input))
    st.session_state.chat_history.append(("🤖 AI", response))

    # Rerun app to refresh chat
    st.rerun()
