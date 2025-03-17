import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_ai_response(user_input):
    api_key = os.getenv("GOOGLE_API_KEY")  
    if not api_key:
        raise ValueError("Missing Google API Key. Set GOOGLE_API_KEY as an environment variable.")
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=AIzaSyAPECPvgOQcYhZ4-Ch-mt17y4f4Xax7u4I, streaming=True)
    
    return llm.invoke(user_input)
