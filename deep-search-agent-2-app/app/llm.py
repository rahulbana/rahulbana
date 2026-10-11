# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""LLM access layer with a switchable provider (Anthropic or OpenAI via LangChain).

Centralizes model construction so nodes ask for a *role* ("fast" vs "smart")
rather than a model id, and so token usage is uniformly extractable for the
budget tracker. `structured` returns a runnable that emits a validated Pydantic
object via provider tool-calling, which is how the synthesis node produces a
`ResearchReport`.
"""

from __future__ import annotations

from typing import TypeVar

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from pydantic import BaseModel

from app.budget import Usage
from app.config import Settings

T = TypeVar("T", bound=BaseModel)


class LLM:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def provider(self) -> str:
        return self._settings.provider

    def _model_id(self, role: str) -> str:
        s = self._settings
        return s.active_smart_model if role == "smart" else s.active_fast_model

    def chat(self, role: str = "fast", *, temperature: float = 0.2) -> BaseChatModel:
        s = self._settings
        model = self._model_id(role)
        if s.provider == "openai":
            from langchain_openai import ChatOpenAI

            kwargs: dict = {"model": model, "api_key": s.openai_api_key, "max_tokens": 4096}
            if s.openai_base_url:
                kwargs["base_url"] = s.openai_base_url
            # Reasoning models only accept the default temperature.
            if not model.startswith(("o1", "o3", "o4", "gpt-5")):
                kwargs["temperature"] = temperature
            return ChatOpenAI(**kwargs)

        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model=model,
            temperature=temperature,
            api_key=s.anthropic_api_key,
            max_tokens=4096,
        )

    def structured(self, schema: type[T], *, role: str = "smart"):
        """Return a runnable that emits `schema` and the raw message (for usage)."""
        chat = self.chat(role)
        if self._settings.provider == "openai":
            # function_calling accepts our non-strict Pydantic schemas (defaults, optionals);
            # OpenAI's strict json_schema mode would reject them.
            return chat.with_structured_output(schema, include_raw=True, method="function_calling")
        return chat.with_structured_output(schema, include_raw=True)

    @staticmethod
    def usage_from(message: BaseMessage, model: str) -> Usage:
        """Extract token usage from an AIMessage (same shape for both providers)."""
        meta: dict = {}
        if isinstance(message, AIMessage):
            meta = message.usage_metadata or {}  # type: ignore[assignment]
        return Usage(
            input_tokens=int(meta.get("input_tokens", 0)) if meta else 0,
            output_tokens=int(meta.get("output_tokens", 0)) if meta else 0,
            model=model,
        )
