# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Provider switching: settings resolution and model construction (offline)."""

import pytest

from app.config import Settings
from app.llm import LLM


def _settings(**kw) -> Settings:
    base = dict(ANTHROPIC_API_KEY="a-key", OPENAI_API_KEY="o-key")
    base.update(kw)
    return Settings(_env_file=None, **base)


def test_default_provider_is_anthropic():
    s = _settings()
    assert s.provider == "anthropic"
    assert s.llm_api_key == "a-key"
    assert s.active_smart_model == s.smart_model


def test_openai_provider_resolves_key_and_models():
    s = _settings(LLM_PROVIDER="OpenAI")
    assert s.provider == "openai"
    assert s.llm_api_key == "o-key"
    assert s.llm_api_key_name == "OPENAI_API_KEY"
    assert s.active_fast_model == "gpt-4o-mini"
    assert s.active_smart_model == "gpt-4o"


def test_invalid_provider_raises():
    with pytest.raises(ValueError):
        _ = _settings(LLM_PROVIDER="gemini").provider


def test_llm_builds_provider_specific_chat_models():
    anth = LLM(_settings()).chat("fast")
    assert type(anth).__name__ == "ChatAnthropic"
    oai = LLM(_settings(LLM_PROVIDER="openai")).chat("smart")
    assert type(oai).__name__ == "ChatOpenAI"
    assert oai.model_name == "gpt-4o"


def test_reasoning_models_skip_temperature():
    oai = LLM(_settings(LLM_PROVIDER="openai", OPENAI_SMART_MODEL="gpt-5")).chat("smart")
    assert oai.temperature is None
