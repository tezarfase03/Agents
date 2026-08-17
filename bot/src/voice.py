import asyncio
import tempfile
from pathlib import Path
import edge_tts
import sounddevice as sd
import soundfile as sf

# Some natural female options: en-US-JennyNeural, en-US-AriaNeural
DEFAULT_VOICE = "en-US-AndrewNeural"

async def _synthesize_and_play(text: str, voice: str) -> None:
    communicate = edge_tts.Communicate(text, voice)

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    await communicate.save(str(tmp_path))

    data, samplerate = sf.read(tmp_path)

    sd.play(data, samplerate)
    sd.wait()

    tmp_path.unlink(missing_ok=True)

def speak(text: str, voice: str = DEFAULT_VOICE) -> None:
    """Synthesize text and play through speakers."""
    asyncio.run(_synthesize_and_play(text, voice))