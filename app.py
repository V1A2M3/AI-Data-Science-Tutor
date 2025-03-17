import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ai_tutor.model import get_ai_response

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🎓", layout="wide")

# ---- Apply Custom CSS for Black Text ----
st.markdown(
    """
    <style>
    body { color: black !important; }
    .stTextInput, .stButton>button { color: black !important; }
    .stMarkdown { color: black !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📊 AI Data Science Tutor")

# ---- Initialize Chat History ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- Display Chat History (AI Answers on Top) ----
st.subheader("📜 Chat History")
for user_query, ai_response in reversed(st.session_state.chat_history):
    st.write(f"**You:** {user_query}")
    st.write(ai_response)
    st.write("---")

# ---- User Input at Bottom ----
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask a Data Science question:", key="user_input")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    response = get_ai_response(user_input)  # AI generates response

    # ---- Check for Python Code and Display it ----
    if "```python" in response:
        code_block = response.split("```python")[1].split("```")[0]
        st.code(code_block, language="python")

    # ---- Check for Table Data ----
    if "|" in response:  # If response contains table-like data
        try:
            table_data = [row.split("|") for row in response.split("\n") if "|" in row]
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            st.dataframe(df)
        except Exception:
            pass  # Ignore if the table format is incorrect

    # ---- Check for Graph Requests ----
    if "plot" in user_input.lower() or "graph" in user_input.lower():
        fig, ax = plt.subplots()
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 30, 40, 50]
        ax.plot(x, y, marker='o', linestyle='-', color='b')
        ax.set_title("Sample AI-Generated Plot")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        st.pyplot(fig)

    # ---- Store Chat in History ----
    st.session_state.chat_history.append((user_input, response))

    # ---- Rerun to Refresh UI ----
    st.rerun()
