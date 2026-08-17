from __future__ import annotations

import sys
from pathlib import Path

# Add project root and bot directories to sys.path
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_BOT_DIR = Path(__file__).resolve().parent.parent
_SRC_DIR = Path(__file__).resolve().parent
for _p in (str(_PROJECT_ROOT), str(_BOT_DIR), str(_SRC_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from bot.src.chatbot import PersonaChatbot
    from bot.src.voice import speak
except (ImportError, ModuleNotFoundError):
    try:
        from src.chatbot import PersonaChatbot
        from src.voice import speak
    except (ImportError, ModuleNotFoundError):
        from chatbot import PersonaChatbot
        from voice import speak
def main() -> int:
    try:
        chatbot = PersonaChatbot()
    except RuntimeError as exc:
        print(f"Error: {exc}")
        return 1
    
    print("=" * 60)
    print("🎙️  Personal Voice Chatbot Started")
    print("Commands: /compare <prompt> | /reset | /exit")
    print("=" * 60)

    while True:
        try:
            user_message = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return 0
    
        if not user_message:
            continue
        if user_message.lower() in ("exit", "quit", "/exit", "/quit"):
            print("Goodbye.")
            return 0
        if user_message.lower() == "/reset":
            chatbot.reset()
            print("Conversation memory reset.")
            continue
        if user_message.lower().startswith("/compare"):
            query = user_message[len("/compare"):].strip()
            if not query:
                print("Usage: /compare <your question or prompt>")
                continue
            try:
                print("Comparing responses...")
                with_p, without_p = chatbot.compare(query)
                print("\n" + "=" * 50)
                print("🧠 [With Persona]:")
                print(with_p)
                print("-" * 50)
                print("🤖 [Standard LLM (Without Persona)]:")
                print(without_p)
                print("=" * 50)
            except Exception as exc:
                print(f"Error during comparison: {exc}")
            continue
        
        try:
            answer = chatbot.ask(user_message)
            print(f"\nBot: {answer}")
            try:
                speak(answer)
            except Exception as ve:
                print(f"[Voice playback notice: {ve}]")
        except Exception as exc:
            print(f"\nError: {exc}")


if __name__ == "__main__":
    raise SystemExit(main())