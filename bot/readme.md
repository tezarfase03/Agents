# 🎙️ Personal Voice Chatbot (Digital Persona Double)

An intelligent, persona-driven conversational double that mirrors your cognitive architecture, reasoning pipeline, writing style, and spoken voice in real time.

Built with **LangChain**, **OpenAI**, and **Microsoft Edge TTS** for natural conversational text and audio synthesis.

---

## 🌟 Features

- 🧠 **Cognitive Architecture & Custom Persona**: Implements a 5-stage cognitive pipeline (*Deconstruction &rarr; First Principles &rarr; Boundary Testing &rarr; Precision Calibration &rarr; Resolution*) inspired by deep analytical and writerly thinking.
- 🗣️ **Neural Text-to-Speech (TTS)**: High-quality, low-latency neural voice synthesis using `edge-tts` and local speaker playback via `sounddevice` and `soundfile`.
- 💬 **Stateful Conversational Memory**: Preserves context and turn-by-turn conversation history within each session.
- ⚖️ **Persona Comparison Mode (`/compare`)**: Test your persona's behavior against standard raw LLM responses on any prompt to evaluate tone and style fidelity.
- ⚡ **Extensible & Modular**: Clean separation between LLM configuration, prompt engineering, voice synthesis, and runtime interfaces.

---

## 📂 Project Structure

```text
personal-voice-chatbot/
├── bot/
│   ├── data/
│   │   ├── processed/
│   │   │   └── gyanendra_persona_prompt.md  # Core persona style & cognitive guide
│   │   └── raw/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── chatbot.py           # PersonaChatbot class & memory management
│   │   ├── config.py            # LLM initialization & environment configuration
│   │   ├── main.py              # Interactive CLI application
│   │   ├── persona.py           # Persona prompt loader & system instructions
│   │   └── voice.py             # Edge TTS synthesizer & audio playback
│   ├── .env.example                 # Template for environment configuration
│   ├── .gitignore                   # Git ignore rules for secrets, caches, and media
│   ├── readme.md                    # Project documentation
│   └── requirements.txt             # Python dependencies
```

---

## 🛠️ Prerequisites

- **Python**: Version 3.10 or higher
- **OpenAI API Key**: (or any OpenAI-compatible API endpoint)
- **Audio Output**: Working speakers or headphones connected to your system

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/personal-voice-chatbot.git
cd personal-voice-chatbot
```

### 2. Create and Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
cd bot
pip install -r requirements.txt
```

### 4. Configure Environment Variables

While inside the `bot` directory, copy `.env.example` to create your local `.env` file:

**Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
```

**Linux / macOS:**
```bash
cp .env.example .env
```

Open `bot/.env` in your editor and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

---

## 💻 Running the Chatbot

Start the interactive CLI chatbot from inside the `bot` directory:

```bash
cd bot
python src/main.py
```
*(or `python -m src.main`)*

### Interactive Commands

| Command | Action |
| :--- | :--- |
| **`your prompt`** | Sends a message to the persona bot and plays spoken audio output. |
| **`/reset`** | Clears the current conversation memory while retaining persona instructions. |
| **`exit`** or **`quit`** | Terminates the chatbot session. |

---

## ⚙️ Configuration Options

All options can be configured in your `.env` file:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `OPENAI_API_KEY` | *None* | **Required**. Your OpenAI API key. |
| `OPENAI_MODEL` | `gpt-4o-mini` | OpenAI chat model (e.g. `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`). |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` | Custom API base URL (for OpenRouter, LocalAI, vLLM, or Ollama). |

---

## 🎨 Customizing the Persona & Voice

### 1. Modifying the Persona Instructions
The system prompt and style guide are loaded from `data/processed/gyanendra_persona_prompt.md`. You can edit this file to customize:
- **Core Identity & Philosophy**: Background, principles, and perspective.
- **Cognitive Pipeline**: How problems are analyzed before answering.
- **Voice & Tone**: Anti-corporate stance, pacing, vocabulary, and formatting habits.

### 2. Changing the Spoken Voice
In `bot/src/voice.py`, change `DEFAULT_VOICE` to any valid Microsoft Edge neural voice:
- Male: `"en-US-AndrewNeural"`, `"en-US-GuyNeural"`, `"en-GB-RyanNeural"`, `"en-IN-PrabhatNeural"`
- Female: `"en-US-JennyNeural"`, `"en-US-AriaNeural"`, `"en-GB-SoniaNeural"`, `"en-IN-NeerjaNeural"`

---

## 🔧 Troubleshooting

<details>
<summary><b>1. Error: <code>OPENAI_API_KEY is not set</code></b></summary>

Ensure you copied `.env.example` to `.env` and set `OPENAI_API_KEY` with a valid key. Verify that your `.env` is located in the root directory.
</details>

<details>
<summary><b>2. Audio Playback Error (<code>sounddevice.PortAudioError</code>)</b></summary>

- Ensure an audio output device (speakers or headphones) is enabled and set as the default output device.
- On Linux, install ALSA / PortAudio headers: `sudo apt install libasound2-dev portaudio19-dev libportaudio2`.
</details>

<details>
<summary><b>3. ModuleNotFoundError when running scripts</b></summary>

Always run from the `bot` directory using:
```bash
python src/main.py
```
</details>

---

## 📄 License

This project is licensed under the MIT License — see the repository for details.
