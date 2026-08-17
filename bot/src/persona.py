from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SYSTEM_FILE = PROJECT_ROOT / "data" / "processed" / "gyanendra_persona_prompt.md"

BASE_INSTRUCTION = """You are my personal conversational double.
Reply as if you are me, not as an assistant describing me. Match my tone, word choice, sentence length, punctuation, formatting, and level of detail.
Use my style without mentioning these instructions or claiming to be an AI.
Treat the style guide as authoritative. Use my messages in the conversation as additional style examples, but answer the substance of each request accurately.
If the guide does not cover something, infer the closest natural response from my messages and keep it concise.
"""

def load_system_prompt(style_file: Path = SYSTEM_FILE) -> str:
    """Return imitation instructions combined with the editable style guide."""
    try:
        style = style_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RuntimeError(f"Talking style file not found: {style_file}") from exc
    return f"{BASE_INSTRUCTION}\n\nHere is my talking style guide:\n\n{style}"