import streamlit as st
import subprocess
from ai_tutor.model import get_ai_response

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🤖", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
    body { background-color: #f5f5f5; }
    .user-bubble { background-color: #1E88E5; color: white; padding: 10px; border-radius: 10px; width: fit-content; }
    .ai-bubble { background-color: #f1f1f1; color: black; padding: 10px; border-radius: 10px; width: fit-content; }
    .chat-container { display: flex; flex-direction: column; align-items: flex-start; }
    .chat-right { align-self: flex-end; }
    </style>
""", unsafe_allow_html=True)

# ---- APP TITLE ----
st.title("🤖 AI Data Science Tutor")

# ---- THEME TOGGLE ----
theme = st.radio("Choose Theme:", ["🌞 Light", "🌙 Dark"])
if theme == "🌙 Dark":
    st.markdown("""
        <style>
        body { background-color: #121212; color: white; }
        .user-bubble { background-color: #1E88E5; color: white; }
        .ai-bubble { background-color: #333; color: white; }
        </style>
    """, unsafe_allow_html=True)

# ---- AI PERSONALITY SELECTION ----
personality = st.selectbox("Choose AI Personality:", ["🎓 Professor", "😃 Friendly", "📈 Business"])

# ---- CHAT HISTORY STATE ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- CODE EXECUTION FUNCTION ----
def execute_code(code):
    try:
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return str(e)

# ---- USER INPUT ----
user_input = st.text_input("Ask a Data Science question:", placeholder="e.g., What is linear regression?")

if user_input:
    # Apply personality
    if personality == "🎓 Professor":
        prompt = "Explain like a university professor: " + user_input
    elif personality == "😃 Friendly":
        prompt = "Explain in a fun and simple way: " + user_input
    else:
        prompt = "Explain in a professional and business-oriented style: " + user_input

    # Show user message in chat bubble instantly
    st.markdown(f'<div class="chat-container"><div class="user-bubble chat-right">👨‍💻 You: {user_input}</div></div>', unsafe_allow_html=True)
    
    # Get AI response instantly
    response = get_ai_response(prompt)
    
    # Show AI message in chat bubble instantly
    st.markdown(f'<div class="chat-container"><div class="ai-bubble">🤖 AI: {response}</div></div>', unsafe_allow_html=True)

    # Save chat history
    st.session_state.chat_history.append(("👨‍💻 You", user_input))
    st.session_state.chat_history.append(("🤖 AI", response))

    # Execute Python Code if AI Generates It
    if "```python" in response:
        code_block = response.split("```python")[1].split("```")[0]
        execution_result = execute_code(code_block)
        st.code(code_block, language="python")
        st.success(f"Execution Output:\n{execution_result}")

# ---- DISPLAY CHAT HISTORY ----
st.subheader("📜 Chat History")
for role, message in st.session_state.chat_history:
    if role == "👨‍💻 You":
        st.markdown(f'<div class="chat-container"><div class="user-bubble chat-right">{role}: {message}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-container"><div class="ai-bubble">{role}: {message}</div></div>', unsafe_allow_html=True)
