# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Application settings loaded from environment / .env."""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # LLM provider: "anthropic" or "openai"
    llm_provider: str = Field(default="anthropic", alias="LLM_PROVIDER")

    # Anthropic (FAST_MODEL / SMART_MODEL are the legacy names for these two)
    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    fast_model: str = Field(default="claude-haiku-4-5-20251001", alias="FAST_MODEL")
    smart_model: str = Field(default="claude-sonnet-5", alias="SMART_MODEL")

    # OpenAI (base URL is optional, for OpenAI-compatible gateways)
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    openai_base_url: str = Field(default="", alias="OPENAI_BASE_URL")
    openai_fast_model: str = Field(default="gpt-4o-mini", alias="OPENAI_FAST_MODEL")
    openai_smart_model: str = Field(default="gpt-4o", alias="OPENAI_SMART_MODEL")

    # Search backends
    tavily_api_key: str = Field(default="", alias="TAVILY_API_KEY")
    serper_api_key: str = Field(default="", alias="SERPER_API_KEY")
    exa_api_key: str = Field(default="", alias="EXA_API_KEY")

    # Persistence
    database_url: str = Field(default="", alias="DATABASE_URL")

    # Observability
    langfuse_public_key: str = Field(default="", alias="LANGFUSE_PUBLIC_KEY")
    langfuse_secret_key: str = Field(default="", alias="LANGFUSE_SECRET_KEY")
    langfuse_host: str = Field(default="https://cloud.langfuse.com", alias="LANGFUSE_HOST")

    # Budget / safety caps
    max_iterations: int = Field(default=5, alias="MAX_ITERATIONS")
    max_usd_cost: float = Field(default=2.50, alias="MAX_USD_COST")
    max_searches_per_iteration: int = Field(default=6, alias="MAX_SEARCHES_PER_ITERATION")
    max_sources: int = Field(default=40, alias="MAX_SOURCES")

    @property
    def provider(self) -> str:
        p = self.llm_provider.strip().lower()
        if p not in ("anthropic", "openai"):
            raise ValueError(f"LLM_PROVIDER must be 'anthropic' or 'openai', got {self.llm_provider!r}")
        return p

    @property
    def llm_api_key(self) -> str:
        return self.openai_api_key if self.provider == "openai" else self.anthropic_api_key

    @property
    def llm_api_key_name(self) -> str:
        return "OPENAI_API_KEY" if self.provider == "openai" else "ANTHROPIC_API_KEY"

    @property
    def active_fast_model(self) -> str:
        return self.openai_fast_model if self.provider == "openai" else self.fast_model

    @property
    def active_smart_model(self) -> str:
        return self.openai_smart_model if self.provider == "openai" else self.smart_model

    @property
    def has_postgres(self) -> bool:
        return bool(self.database_url)

    @property
    def has_langfuse(self) -> bool:
        return bool(self.langfuse_public_key and self.langfuse_secret_key)

    def enabled_backends(self) -> list[str]:
        backends = ["arxiv"]  # keyless
        if self.tavily_api_key:
            backends.append("tavily")
        if self.serper_api_key:
            backends.append("serper")
        if self.exa_api_key:
            backends.append("exa")
        return backends


@lru_cache
def get_settings() -> Settings:
    return Settings()
