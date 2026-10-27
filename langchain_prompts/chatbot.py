from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

model=ChatOpenAI()
chathistory=[
    systemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("User: ")
    chathistory.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(chathistory)
    chathistory.append(AIMessage(content=response.content))
    print("Chatbot:", response.content)

