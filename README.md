📊 AI Data Science Tutor
A Conversational AI Data Science Tutor built using Google Gemini 1.5 Pro, LangChain, and Streamlit. This application provides interactive AI-powered explanations for data science topics while remembering past conversations.



🚀 Features
✅ Conversational AI for Data Science Questions
✅ Memory to remember past interactions
✅ Uses Google Gemini AI for responses
✅ Streamlit UI for an interactive chat experience
✅ Easy to Deploy on GitHub, Streamlit Cloud, or Hugging Face


🛠 Tech Stack
🤖 LLM: Google Gemini 1.5 Pro
🧠 Memory: LangChain's ConversationBufferMemory
📡 API Integration: Google Generative AI API
🎨 UI: Streamlit
📂 Vector DB (optional): FAISS
📂 Folder Structure
bash
Copy
Edit
AI-Data-Science-Tutor/
│── ai_tutor/             
│   ├── __init__.py        # Package initializer
│   ├── model.py           # AI model using Google Gemini
│   ├── memory.py          # LangChain memory for chat history
│── app.py                 # Streamlit app
│── requirements.txt       # Dependencies
│── README.md              # Documentation


📦 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Data-Science-Tutor.git
cd AI-Data-Science-Tutor

2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🏃 Run the AI Tutor
bash
Copy
Edit
streamlit run app.py
Then, open http://localhost:8501 in your browser.

🌍 Deploy on Streamlit Cloud
Push your code to GitHub
Go to Streamlit Cloud
Click "New App"
Select your GitHub repo
Click "Deploy" 🚀
🛠 API Configuration
This project uses Google Generative AI API.
🔹 Get your API key from Google AI Studio
🔹 Store it in an environment variable:

bash
Copy
Edit
export GOOGLE_API_KEY="your-api-key-here"
🛠 Contributing
💡 Contributions are welcome!

Fork the repo
Create a branch (git checkout -b feature-xyz)
Commit changes (git commit -m "Added feature XYZ")
Push to GitHub (git push origin feature-xyz)
Create a Pull Request
📜 License
This project is MIT Licensed. Feel free to use and modify it.
