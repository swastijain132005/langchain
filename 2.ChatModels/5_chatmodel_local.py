from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    model_id="TheBloke/vicuna-13B-1.1-HF",
    task="text-generation",
    temperature=0.9,
    max_new_tokens=100
)

model=ChatHuggingFace(llm=llm)
result = model.invoke("Write a poem about the beauty of nature.")
print(result.content)