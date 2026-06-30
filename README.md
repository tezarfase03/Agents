# Agents LangChain

My first project exploring **AI agents** with LangChain. I'm still learning how agents, tools, and LLMs work together — this repo is where I figured it out step by step.

## What I built

A **lyrics moderation assistant** that:

1. Takes a YouTube video URL
2. Fetches the lyrics from the video transcript
3. Uses an AI agent to decide when to call tools
4. Cleans up bad language before returning the result

### Files

- **`langchain_helper.py`** — The main agent setup using Google Gemini and LangChain tools.

### Tools the agent can use

- **`lyrics_fetcher`** — Loads lyrics from a YouTube video and removes extra formatting.
- **`Moderator`** — Detects and masks profanity in the lyrics.

## How it works

The agent is built with `create_agent` from LangChain. It uses **Gemini 2.5 Flash** as the model and gets a system prompt telling it to fetch lyrics and moderate them. When you give it a YouTube link, the agent picks the right tools and returns cleaned lyrics.

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
