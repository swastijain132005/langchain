
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a poem about the beauty of nature.")

print(result.content)
