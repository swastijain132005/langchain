from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import promptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)
parser=JsonOutputParser()

"""template1=promptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']

)

template2 =promptTemplate(
    template='write a 5 line summary on the following text/n {text}',
    input_variables=['text']
)"""

template=promptTemplate(
    template='give me the name,age and city of a fictional charc\n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.format()

result=model.invoke(prompt)

final_result=parser.parse(result.content)
print(type(final_result))

#or

chain=template|model|parser

result=chain.invoke({})
print(result)


