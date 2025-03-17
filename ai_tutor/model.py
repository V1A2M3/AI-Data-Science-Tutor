from langchain_google_genai import ChatGoogleGenerativeAI

def get_ai_response(user_input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    return llm.predict(user_input)
