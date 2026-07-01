# Stateful Agent & Chatbot

This subdirectory contains two implementations of stateful conversational agents using LangChain and LangGraph, demonstrating how to maintain chat history across interactions.

## Content

- **`stateful.py`** — Demonstrates a stateful agent setup using LangChain's `create_agent` and `InMemorySaver` (from LangGraph) to persist message history for a specific `thread_id`.
- **`chatbot_stateful.py`** — An interactive command-line chat session using `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` to remember past messages within a session.

---

## How to Run

Before running, ensure you have set up your virtual environment and `.env` file containing your `GOOGLE_API_KEY` (see the root [README](../README.md)).

### 1. Stateful Agent Execution (`stateful.py`)
This script initializes an agent with a memory checkpointer (`InMemorySaver`), invokes it with a weather query, and retrieves/prints the stored history from the state.

Run the script:
```bash
python stateful_agent/stateful.py
```

### 2. Interactive Stateful Chatbot (`chatbot_stateful.py`)
This script launches an interactive terminal prompt where you can chat with the assistant. It maintains conversation history locally in memory under a session ID.

Run the chatbot:
```bash
python stateful_agent/chatbot_stateful.py
```

**Commands inside Chatbot:**
- Type any question or message to chat with the model.
- Type `history` to print the entire chat transcript for the current session.
- Type `quit`, `exit`, or `q` to leave the chat.
