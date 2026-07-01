from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
load_dotenv()
agent = create_agent(
    model="google_genai:gemini-3.5-flash",
    tools =[],
    checkpointer = InMemorySaver()
)
id=str(uuid7())
config = {"configurable":{"thread_id":id}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in assam?"}]},
    config=config,
)

print(result["messages"][-1].content)


def state_checker() -> str:

    # Use the same config/thread_id you used for your invocations
    config = {"configurable": {"thread_id":id }}

    # Retrieve the current state snapshot
    snapshot = agent.get_state(config)

    # Print the messages stored in the state
    print(snapshot.values.get("messages"))

state_checker()