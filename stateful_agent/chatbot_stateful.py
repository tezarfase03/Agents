from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a helpful assistant. Anser questions conciesly."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}"),
])

chain = prompt | llm | StrOutputParser()

store = {}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]= InMemoryChatMessageHistory()
    return store[session_id]


chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",

)

config = {"configurable": {"session_id": "chat-1"}}
print(config['configurable'])
print("chat ready! Type 'quite' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit","exit","q"):
        print("Goodbye!")
        break
    elif user_input.lower() in ("history"):
        session_id=config['configurable']['session_id']
        if session_id in store:
            for msg in store[session_id].messages:
                role = "You" if msg.type =="human" else "Bot"
                print(f" {role}: {msg.content}" )
                
        else:
            print(" NO History Yet!")
            
        print()
        continue 
    
    response = chatbot.invoke({"input":user_input}, config=config)
    print(f"Bot: {response}\n")