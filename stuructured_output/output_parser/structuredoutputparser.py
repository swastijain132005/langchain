from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import promptTemplate
from dotenv import load_dotenv
from langchain.output_parsers import structuredOutputParser,ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact1',description='fact 1 about the topic'),
    ResponseSchema(name='fact2',description='fact 2 about the topic'),
    ResponseSchema(name='fact3',description='fact 3 about the topic'),


]
parser=structuredOutputParser.from_response_schemas(schema)

template=promptTemplate(
    template='give me the name,age and city of a fictional charc\n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)



chain=template|model|parser

result=chain.invoke({'topic':'black-hole'})

print(result)
