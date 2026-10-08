from types import SimpleNamespace

import pytest

from fnirs_ai_helper.provider import (
    OPENROUTER_API_URL,
    GeminiProvider,
    OpenRouterProvider,
    SYSTEM_INSTRUCTIONS,
)


def test_gemini_provider_sends_question_and_context_with_timeout():
    captured = {}

    class FakeModels:
        @staticmethod
        async def generate_content(**kwargs):
            captured.update(kwargs)
            return SimpleNamespace(text="Grounded answer.")

    class FakeAsyncClient:
        models = FakeModels()

        @staticmethod
        async def aclose():
            captured["async_closed"] = True

    class FakeClient:
        def __init__(self, **kwargs):
            captured["client"] = kwargs
            self.aio = FakeAsyncClient()

        @staticmethod
        def close():
            captured["closed"] = True

    answer = GeminiProvider(
        "not-a-real-key",
        model="test-model",
        client_factory=FakeClient,
    ).answer("How do I pair markers?", "Reviewed local documentation.")

    assert answer == "Grounded answer."
    assert captured["client"]["api_key"] == "not-a-real-key"
    assert captured["client"]["http_options"] == {
        "timeout": 60_000,
        "retry_options": {"attempts": 1},
    }
    assert captured["model"] == "test-model"
    assert captured["contents"] == "How do I pair markers?"
    assert "Reviewed local documentation." in captured["config"]["system_instruction"]
    assert "How do I pair markers?" not in captured["config"]["system_instruction"]
    assert captured["async_closed"] is True
    assert captured["closed"] is True
    assert "tool" not in captured


def test_gemini_provider_enforces_total_deadline(monkeypatch):
    import asyncio

    import fnirs_ai_helper.provider as provider_module

    monkeypatch.setattr(provider_module, "REQUEST_TIMEOUT_SECONDS", 0.01)

    class FakeModels:
        @staticmethod
        async def generate_content(**kwargs):
            await asyncio.sleep(1)

    class FakeAsyncClient:
        models = FakeModels()

        @staticmethod
        async def aclose():
            pass

    class FakeClient:
        aio = FakeAsyncClient()

        def __init__(self, **kwargs):
            pass

        @staticmethod
        def close():
            pass

    provider = GeminiProvider("not-a-real-key", client_factory=FakeClient)

    with pytest.raises(TimeoutError, match="within 0.01 seconds"):
        provider.answer("question", "context")


@pytest.mark.parametrize(
    ("question", "context"),
    [("", "context"), ("question", "")],
)
def test_gemini_provider_rejects_missing_input(question, context):
    provider = GeminiProvider("not-a-real-key", client_factory=object)

    with pytest.raises(ValueError):
        provider.answer(question, context)


def test_openrouter_provider_sends_chat_completion_request():
    captured = {}

    class FakeResponse:
        @staticmethod
        def raise_for_status():
            pass

        @staticmethod
        def json():
            return {"choices": [{"message": {"content": "Grounded answer."}}]}

    class FakeClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            captured["closed"] = True

        async def post(self, url, **kwargs):
            captured.update(url=url, **kwargs)
            return FakeResponse()

    provider = OpenRouterProvider(
        "openrouter-secret",
        "provider/model",
        client_factory=lambda **kwargs: FakeClient(),
    )
    answer = provider.answer("How do I pair markers?", "Reviewed local documentation.")

    assert answer == "Grounded answer."
    assert captured["url"] == OPENROUTER_API_URL
    assert captured["headers"]["Authorization"] == "Bearer openrouter-secret"
    assert captured["json"]["model"] == "provider/model"
    assert captured["json"]["messages"][1] == {
        "role": "user",
        "content": "How do I pair markers?",
    }
    assert "Reviewed local documentation." in captured["json"]["messages"][0]["content"]
    assert captured["closed"] is True


def test_openrouter_provider_enforces_total_deadline(monkeypatch):
    import asyncio

    import fnirs_ai_helper.provider as provider_module

    monkeypatch.setattr(provider_module, "REQUEST_TIMEOUT_SECONDS", 0.01)

    class FakeClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

        async def post(self, *args, **kwargs):
            await asyncio.sleep(1)

    provider = OpenRouterProvider(
        "not-a-real-key",
        "provider/model",
        client_factory=lambda **kwargs: FakeClient(),
    )

    with pytest.raises(TimeoutError, match="within 0.01 seconds"):
        provider.answer("question", "context")


def test_openrouter_provider_rejects_empty_model():
    provider = OpenRouterProvider("not-a-real-key", " ")

    with pytest.raises(ValueError, match="model ID"):
        provider.answer("question", "context")


def test_system_instructions_disclose_no_dataset_or_tool_access():
    instructions = SYSTEM_INSTRUCTIONS.lower().replace("\n", " ")
    assert "cannot inspect a dataset" in instructions
    assert "do not provide python, pseudocode" in instructions
    assert "ask one short, specific clarification question and stop" in instructions
    assert 'treat "how do i do this?" as a request for gui instructions' in instructions
    assert "never imply that you have inspected or changed data" in instructions
