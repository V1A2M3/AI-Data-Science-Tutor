from langchain_google_genai import ChatGoogleGenerativeAI

def get_ai_response(user_input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key="AIzaSyAPECPvgOQcYhZ4-Ch-mt17y4f4Xax7u4I")
    return llm.invoke(user_input)

