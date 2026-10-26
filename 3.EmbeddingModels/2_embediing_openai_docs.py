from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)

result=embedding.embed_documents(["delhi is the capital of india"])
print(str(result))