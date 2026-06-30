from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool 
from langchain.agents import create_agent
from better_profanity import profanity
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv
import re
import sys

# Configure stdout to support UTF-8 characters (like music notes) in Windows consoles
sys.stdout.reconfigure(encoding='utf-8')


load_dotenv()


@tool
def Moderator(lyrics: str) -> str:
    """Cleans and returns moderated lyrics by masking profanity."""
    has_profanity = profanity.contains_profanity(lyrics)
    print(f"Contains bad words: {has_profanity}")
    clean_lyrics = profanity.censor(lyrics)
    return clean_lyrics

@tool
def lyrics_fetcher(youtube_url: str) -> str:
    """Extracts, cleans, and returns lyrics from a YouTube video."""
    try:
        loader = YoutubeLoader.from_youtube_url(
            youtube_url,
            add_video_info=False,
            language=["en"]
        )
        docs = loader.load()
        if not docs:
            return "No lyrics found."
            
        raw_text = docs[0].page_content
        clean_text = re.sub(r'\[.*?\]|\(.*?\)', '', raw_text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        return clean_text
    except Exception as e:
        return f"An error occurred: {e}"

def agent_runner(url:str):
    yt_url = url
    # 1. Correct the model name to standard string structures
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )
    
    # 2. Give the agent its role instructions right here using system_prompt
    agent = create_agent(
        model=llm,
        tools=[Moderator, lyrics_fetcher],
        system_prompt="You are a lyrics moderation assistant. Your goal is to fetch lyrics using tools and filter out bad words."
    )
    
    # 3. Invoke with standard message inputs
    response = agent.invoke({
        "messages": [{"role": "user", "content": f"Please fetch the lyrics for this video {yt_url} and moderate them."}]
    })
    
    # LangGraph-backed create_agent returns the message state list; grab the last response text
    return response["messages"][-1].content

print(agent_runner("https://youtu.be/34Na4j8AVgA?si=8MX2ZQpTxxtEsRsS"))