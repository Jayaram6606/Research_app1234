from langchain_core.prompts import ChatPromptTemplate

chat_Template = ChatPromptTemplate([
    ('system', 'you are helpful {domain} expert'),
    ('human', 'Please explain {topic}')
])

prompt = chat_Template.invoke({'domain': 'cricket', 'topic': 'Doosra'})
print(prompt)