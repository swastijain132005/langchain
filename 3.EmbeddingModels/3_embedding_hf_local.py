from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_id="sentence-transformers/all-MiniLM-L6-v2")

text="delhi is the capital of india"
result=embedding.embed_query(text)
print(str(result))