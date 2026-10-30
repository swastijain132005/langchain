from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import promptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import strOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

template1=promptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']

)

template2 =promptTemplate(
    template='write a 5 line summary on the following text/n {text}',
    input_variables=['text']
)

parser=strOutputParser()
chain=template1|model|parser|template2|model|parser
result=chain.invoke({'topic':'black-magic'})
