from langchain_openai import OpenAIEmbeddings
from sklearn.metrices.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)


documents=["delhi is the capital of india","delhi is the capital of xyz"]

query="delhi is the capital of india"

doc_embeddings=embedding.embed_documents(documents)

query_embedding=embedding.embed_query(query)

result=cosine_similarity(doc_embeddings, [query_embedding])[0]



index,score=sorted(list(enumerate(result)),key=lambda x:x[1],reverse=True)

print(documents[index])