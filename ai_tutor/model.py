import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_ai_response(user_input):
    api_key = os.getenv("GOOGLE_API_KEY")  # Store API key securely
    if not api_key:
        raise ValueError("Missing Google API Key. Set GOOGLE_API_KEY as an environment variable.")
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=AIzaSyAPECPvgOQcYhZ4-Ch-mt17y4f4Xax7u4I)
    
    # Handle chart requests
    if "plot" in user_input.lower() or "graph" in user_input.lower():
        return """```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.show()
```"""
    
    return llm.invoke(user_input)


