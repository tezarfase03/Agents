# Agents LangChain

My first project exploring **AI agents** with LangChain. I'm still learning how agents, tools, and LLMs work together — this repo is where I figured it out step by step.

## What I built

1. **Lyrics Moderation Assistant** — An agent that takes a YouTube video URL, fetches lyrics from the video transcript using document loaders, and cleans up bad language using custom moderation tools.
2. **Stateful Agent & Chatbot** — Conversational implementations in the [stateful_agent](file:///c:/Users/kesha/OneDrive/Desktop/agents_langchain/Agents/stateful_agent) directory that demonstrate how to manage and persist chat history using LangChain/LangGraph checkpointers.

### Files

- **`langchain_helper.py`** — The main lyrics moderation assistant agent setup.
- **`stateful_agent/`** — Subdirectory containing the stateful agents. See [stateful_agent/README.md](file:///c:/Users/kesha/OneDrive/Desktop/agents_langchain/Agents/stateful_agent/README.md) for details.

### Tools the Lyrics Assistant can use

- **`lyrics_fetcher`** — Loads lyrics from a YouTube video and removes extra formatting.
- **`Moderator`** — Detects and masks profanity in the lyrics.

## How it works

- **Lyrics Moderation Assistant**: The agent is built with `create_agent` from LangChain. It uses **Gemini 2.5 Flash** as the model and gets a system prompt telling it to fetch lyrics and moderate them. When you give it a YouTube link, the agent picks the right tools and returns cleaned lyrics.
- **Stateful Agent**: Uses `InMemorySaver` memory checkpointing inside `create_agent` to track messages tied to a specific `thread_id` across invocations.
- **Stateful Chatbot**: Uses `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` to build an interactive console chat program that remembers conversation history.


## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/tezarfase03/Agents.git
   cd Agents
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your API key:

   ```bash
   copy .env.example .env
   ```

   Open `.env` and set `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey).

## Run

```bash
python langchain_helper.py
```

## What I learned

- How to define **tools** with `@tool` so an agent can call Python functions
- How an **agent** uses an LLM to decide which tool to use and when
- How to load environment variables and connect to **Google Gemini**
- How to fetch text from **YouTube** using LangChain document loaders

This is my first time working with agents, so the code is simple on purpose — a starting point to build on.
