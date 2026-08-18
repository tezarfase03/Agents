from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pathlib import Path
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_ENV_PATH)

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_BASE_URL = os.getenv(
    "OPENAI_BASE_URL", "https://api.openai.com/v1"
)


def get_api_key() -> Optional[str]:
    return os.getenv("OPENAI_API_KEY")


def has_llm() -> bool:
    return bool(get_api_key())


@lru_cache(maxsize=8)
def get_llm(model: Optional[str] = None, temperature: float = 0.7,) -> BaseChatModel:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to your .env file."
        )

    return ChatOpenAI(
        model=model or DEFAULT_MODEL,
        temperature=temperature,
        max_retries=3,
        request_timeout=30,
        max_tokens=1000,
        # extra_body={
        #     "reasoning":{
        #         "effort":"low"
        #     }
        # },
        openai_api_key=api_key,
        openai_api_base=OPENAI_BASE_URL,

    )

