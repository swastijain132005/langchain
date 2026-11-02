from lanchain_community.document_loaders import TextLoader 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import strOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template="You are a helpful assistant that summarizes text. Please summarize the following text:\n\n{text}\n\nSummary:",
    input_variables=["text"])

parser=strOutputParser()

loader=TextLoader("path/to/your/textfile.txt")

docs=loader.load()
print(docs)

print(docs[0].page_content)
print(docs[0].metadata)

chain=prompt|model|parser

print(chain.invoke({"text": docs[0].page_content}));