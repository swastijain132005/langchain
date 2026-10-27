from langchain_core.prompt import chatpromptTemplate ,MessagePlaceholder

chat_template=chatpromptTemplate([
    ('system','you are a helpful {domain} expert'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human','Explain in simple terms ,what is {topic}')])

chat_history=[]

with open('chat_history.txt','r') as f:
    for line in f:
        chat_history.append(line.strip())

prompt=chat_template.invoke({'domain':'cricket','topic':'xyz','chat_history':chat_history})