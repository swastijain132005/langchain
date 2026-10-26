from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)

documents=["delhi is the capital of india","delhi is the capital of xyz"]
result=embedding.embed_documents(documents)
print(str(result))