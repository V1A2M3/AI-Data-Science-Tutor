from langchain.chat_models import ChatGoogleGenerativeAI
from ai_tutor.memory import memory

def get_ai_response(user_input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    return llm.predict(user_input)
