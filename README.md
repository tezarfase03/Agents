# Agents LangChain

My first project exploring **AI agents** with LangChain. I'm still learning how agents, tools, and LLMs work together — this repo is where I figured it out step by step.

## What I built

1. **Lyrics Moderation Assistant** — An agent that takes a YouTube video URL, fetches lyrics from the video transcript using document loaders, and cleans up bad language using custom moderation tools.
2. **Stateful Agent & Chatbot** — Conversational implementations in the `stateful_agent` directory that demonstrate how to manage and persist chat history using LangChain's `RunnableWithMessageHistory` and `InMemoryChatMessageHistory`.

### Files

- [`langchain_helper.py`](langchain_helper.py) — The main lyrics moderation assistant agent setup.
- [`stateful_agent/`](stateful_agent/) — Subdirectory containing the stateful agents.

### Tools the Lyrics Assistant can use

- `lyrics_fetcher` — Loads lyrics from a YouTube video and removes extra formatting.
- `Moderator` — Detects and masks profanity in the lyrics.

## How it works

- **Lyrics Moderation Assistant**: The agent is built with `create_agent` from LangChain. It uses **Gemini 2.5 Flash** as the model and gets a system prompt telling it to fetch lyrics and moderate them. When you give it a YouTube link, the agent picks the right tools (like `lyrics_fetcher` and `Moderator`) and returns cleaned lyrics via `agent_runner`.
- **Stateful Agent (`stateful.py`)**: Uses `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` to build an asynchronous, streaming interactive console chatbot. It defines `get_session_history` to fetch session message history and streams output tokens via `astream_events` in the `main` function loop.
- **Stateful Chatbot (`chatbot_stateful.py`)**: A synchronous version of the interactive console chatbot that uses `RunnableWithMessageHistory` and `get_session_history` to manage history, retrieving response output via synchronous `invoke`.


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

### 1. Run Lyrics Moderation Assistant
```bash
python langchain_helper.py
```

### 2. Run Asynchronous Streaming Stateful Chatbot
```bash
python stateful_agent/stateful.py
```

### 3. Run Synchronous Stateful Chatbot
```bash
python stateful_agent/chatbot_stateful.py
```

## What I learned

- How to define **tools** with `@tool` so an agent can call Python functions
- How an **agent** uses an LLM to decide which tool to use and when
- How to load environment variables and connect to **Google Gemini**
- How to fetch text from **YouTube** using LangChain document loaders

This is my first time working with agents, so the code is simple on purpose — a starting point to build on.
