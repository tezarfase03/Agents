from langchain.agents import create_agent
from deepagents.backends import FilesystemBackend
from deepagents.middleware import FilesystemMiddleware ,SkillsMiddleware, SummarizationMiddleware, MemoryMiddleware
from deepagents.middleware.subagents import SubAgent
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
load_dotenv()
backend = FilesystemBackend(
    root_dir =r"C:\Users\kesha\OneDrive\Desktop\agents_langchain"
)
llm = ChatMistralAI(model="mistral-large-latest", temperature=0.7)
agent = create_agent(
    model = llm,
    middleware=[
        
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=llm, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        
    ]

)

while True:
    user_input = input("You: ")
    if user_input.lower() =="quit":
        break
    response = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":user_input
                }
            ]
        }
      
    )
    print("\n Agent")
    print(response)