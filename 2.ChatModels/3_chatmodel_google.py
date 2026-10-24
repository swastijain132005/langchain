from langchain_google_genai import chatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=chatGoogleGenerativeAI(model='gemini-pro',temperature=0.9,max_tokens=100)

result=model.invoke("Write a poem about the beauty of nature.")

print(result.content)