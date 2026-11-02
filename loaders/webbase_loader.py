from langchain_community.document_loaders import webBaseLoader

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import strOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template="You are a helpful assistant that summarizes text. Please summarize the following text:\n\n{text}\n\nSummary:",
    input_variables=["text"])

parser=strOutputParser()


url="https://www.example.com"

loader=webBaseLoader(url)

docs=loader.load()

chain=prompt|model|parser

chain.invoke({"text": docs[0].page_content})
print(docs)

print(docs[0].page_content)
