from langchain_openai import chatOpenAi
from dotenv import load_dotenv

load_dotenv()

model=chatOpenAI(model='gpt-3.5-turbo-instruct',temperature=0.9,max_tokens=100)

result=model.invoke("Write a poem about the beauty of nature.")

print(result.content)