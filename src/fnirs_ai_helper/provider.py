"""Provider interface and API adapters for supported LLM services."""

import asyncio
from typing import Protocol

import httpx

REQUEST_TIMEOUT_MS = 60_000
REQUEST_TIMEOUT_SECONDS = REQUEST_TIMEOUT_MS / 1_000
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_INSTRUCTIONS = """\
You are the Brain Analyzer fNIRS analysis help assistant for researchers who
do not write code.

Give short, plain-language answers focused on how to use Brain Analyzer. Lead
with the direct answer, then give only the minimum GUI steps needed. Prefer
the names of actual menus and controls documented in the supplied context.
Do not provide Python, pseudocode, formulas, implementation details, or
developer caveats unless the user explicitly asks for them. Treat "How do I
do this?" as a request for GUI instructions, not code.

If a missing detail could change the correct GUI action or outcome, ask one
short, specific clarification question and stop. Do not include possible
solutions, code sketches, lengthy explanations, or conditional branches in
that reply. Once clarified, answer the question directly.

If the requested action is not supported by the documented toolbox, say so
plainly (for example, "The current toolbox does not do that automatically.")
and, only if supported by context, mention the closest available GUI feature.
Never invent menus, controls, or behavior. Keep the answer to about 120 words
or fewer unless the user asks for detail.

Use only the supplied Brain Analyzer context for claims about toolbox
functionality. Distinguish documented behavior from general guidance when
needed. This prototype cannot inspect a dataset, access the filesystem, or
operate Brain Analyzer; never imply that you have inspected or changed data.

Do not ask for, repeat, or encourage sharing PHI, identifying information,
credentials, or other sensitive study data.
"""


class LLMProvider(Protocol):
    """Small provider-independent text question/answer interface."""

    def answer(self, question: str, context: str) -> str:
        """Answer one question using the supplied local documentation context."""


class GeminiProvider:
    """Send one question and selected local documentation directly to Gemini."""

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.8-flash",
        client_factory=None,
    ):
        self._api_key = api_key
        self.model = model
        self._client_factory = client_factory

    def answer(self, question: str, context: str) -> str:
        if not question.strip():
            raise ValueError("Enter a question before sending.")
        if not context.strip():
            raise ValueError("Assistant context is empty.")

        if self._client_factory is None:
            try:
                from google import genai
                from google.genai import types
            except ImportError as exc:
                raise RuntimeError(
                    "The Google Gen AI SDK is unavailable. Install the app dependencies."
                ) from exc
            client = genai.Client(
                api_key=self._api_key,
                http_options=types.HttpOptions(
                    timeout=REQUEST_TIMEOUT_MS,
                    retry_options=types.HttpRetryOptions(attempts=1),
                ),
            )
        else:
            client = self._client_factory(
                api_key=self._api_key,
                http_options={
                    "timeout": REQUEST_TIMEOUT_MS,
                    "retry_options": {"attempts": 1},
                },
            )

        async def generate_content():
            try:
                return await asyncio.wait_for(
                    client.aio.models.generate_content(
                        model=self.model,
                        contents=question.strip(),
                        config={
                            "system_instruction": (
                                f"{SYSTEM_INSTRUCTIONS}\n\n"
                                f"Brain Analyzer context:\n{context}"
                            )
                        },
                    ),
                    timeout=REQUEST_TIMEOUT_SECONDS,
                )
            except TimeoutError as exc:
                raise TimeoutError(
                    "Gemini did not return a response within "
                    f"{REQUEST_TIMEOUT_SECONDS:g} seconds."
                ) from exc
            finally:
                await client.aio.aclose()

        try:
            response = asyncio.run(generate_content())
        finally:
            client.close()
        answer = response.text
        if not isinstance(answer, str) or not answer.strip():
            raise RuntimeError("Gemini returned an empty answer.")
        return answer.strip()


class OpenRouterProvider:
    """Send one question and local context to an OpenRouter chat model."""

    def __init__(
        self,
        api_key: str,
        model: str,
        client_factory=None,
    ):
        self._api_key = api_key
        self.model = model
        self._client_factory = client_factory

    def answer(self, question: str, context: str) -> str:
        if not question.strip():
            raise ValueError("Enter a question before sending.")
        if not context.strip():
            raise ValueError("Assistant context is empty.")
        if not self.model.strip():
            raise ValueError("Enter an OpenRouter model ID before sending.")

        async def create_answer() -> str:
            client_factory = self._client_factory or httpx.AsyncClient
            async with client_factory(timeout=REQUEST_TIMEOUT_SECONDS) as client:
                try:
                    response = await asyncio.wait_for(
                        client.post(
                            OPENROUTER_API_URL,
                            headers={
                                "Authorization": f"Bearer {self._api_key}",
                                "Content-Type": "application/json",
                            },
                            json={
                                "model": self.model.strip(),
                                "messages": [
                                    {
                                        "role": "system",
                                        "content": (
                                            f"{SYSTEM_INSTRUCTIONS}\n\n"
                                            f"Brain Analyzer context:\n{context}"
                                        ),
                                    },
                                    {"role": "user", "content": question.strip()},
                                ],
                            },
                        ),
                        timeout=REQUEST_TIMEOUT_SECONDS,
                    )
                except TimeoutError as exc:
                    raise TimeoutError(
                        "OpenRouter did not return a response within "
                        f"{REQUEST_TIMEOUT_SECONDS:g} seconds."
                    ) from exc

                response.raise_for_status()
                try:
                    payload = response.json()
                    answer = payload["choices"][0]["message"]["content"]
                except (KeyError, IndexError, TypeError, ValueError) as exc:
                    raise RuntimeError(
                        "OpenRouter returned an invalid or empty chat-completion response."
                    ) from exc
                if not isinstance(answer, str) or not answer.strip():
                    raise RuntimeError("OpenRouter returned an empty answer.")
                return answer.strip()

        return asyncio.run(create_answer())
