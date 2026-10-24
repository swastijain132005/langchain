from langchain_anthropic import chatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=chatAnthropic(model='claude-3-5-sonnet-20241022',temperature=0.9,max_tokens=100)

result=model.invoke("Write a poem about the beauty of nature.")

print(result.content)