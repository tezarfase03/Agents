from __future__ import annotations

from collections.abc import Iterator

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

try:
    from .config import get_llm
    from .persona import load_system_prompt
except (ImportError, ModuleNotFoundError):
    try:
        from bot.src.config import get_llm
        from bot.src.persona import load_system_prompt
    except (ImportError, ModuleNotFoundError):
        from config import get_llm
        from persona import load_system_prompt


class PersonaChatbot:
    """keep conversation history and respond in the configured persona """
    def __init__(self, llm: BaseChatModel | None = None) -> None:
        self._llm = llm or get_llm()
        self._system_prompt = load_system_prompt()
        self._history: list[BaseMessage] = []

    def messages(self, user_message: str) -> list[BaseMessage]:
        return [
            SystemMessage(content=self._system_prompt),
            *self._history,
            HumanMessage(content=user_message),
        ]

    def ask(self, user_message: str) -> str:
        """send one turn and save it to the memory, and return the answer"""
        response = self._llm.invoke(self.messages(user_message))
        answer = str(response.content).strip()
        self._history.extend(
            [HumanMessage(content=user_message), AIMessage(content=answer)]
        )
        return answer
    def compare(self, user_message: str)-> tuple[str,str]:
        """Return isolated deterministic responses with and without the persona"""
        comparison_llm = get_llm(temperature=0)
        with_persona = comparison_llm.invoke(
            [
                SystemMessage(content=self._system_prompt),
                HumanMessage(content=user_message),
            ]
        )
        without_persona = comparison_llm.invoke([HumanMessage(content = user_message)])
        return(
            str(with_persona.content).strip(),
            str(without_persona.content).strip(),
        )
    def stream(self, user_message: str) -> Iterator[str]:
        """stream one answer and save the completed turn to memory"""
        # Use non-streaming invoke and simulate streaming for compatibility
        response = self._llm.invoke(self.messages(user_message))
        answer = str(response.content).strip()
        for char in answer:
            yield char
        self._history.extend(
            [HumanMessage(content=user_message), AIMessage(content=answer)]
        )
    def reset(self) -> None:
        """Clear conversation memory while keeping the current persona."""
        self._history.clear()




      


