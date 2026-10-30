from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import promptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import pydanticOutputParser
from pydantic import BaseModel,Field


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)
#pydantic object
class person(BaseModel):

    name:str=Field(description='name of person')
    age:int=Field(gt=18,description='age of the person')
    city:str=Field(description='name of city')

parser=pydanticOutputParser(pydantic_object=person)


template=promptTemplate(
    template='generate the name,age and {place } of person\n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    
)

chain=template |model| parser
final_result=chain.invoke({'place':'sri lankan'})
print(final_result)



