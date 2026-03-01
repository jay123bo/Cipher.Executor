"""Cipher AI terminal assistant."""

from __future__ import annotations

import os
from dataclasses import dataclass, field

try:
    from openai import OpenAI
except ImportError:  # dependency might not be installed yet
    OpenAI = None

SYSTEM_PROMPT = (
    "You are Cipher AI, a helpful assistant focused on safe, practical guidance. "
    "Keep answers concise unless the user asks for depth."
)


@dataclass
class CipherAI:
    """A simple chat interface over an OpenAI-compatible API."""

    model: str = field(default_factory=lambda: os.getenv("CIPHER_MODEL", "gpt-4o-mini"))
    client: object | None = field(default=None)
    history: list[dict[str, str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and OpenAI is not None:
            base_url = os.getenv("OPENAI_BASE_URL")
            self.client = OpenAI(api_key=api_key, base_url=base_url)

    def reply(self, user_text: str) -> str:
        """Return assistant reply from API or fallback mode."""
        self.history.append({"role": "user", "content": user_text})

        if self.client is None:
            return self._fallback(user_text)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}, *self.history]
        response = self.client.chat.completions.create(model=self.model, messages=messages)
        text = response.choices[0].message.content or "I could not generate a response."
        self.history.append({"role": "assistant", "content": text})
        return text

    def _fallback(self, user_text: str) -> str:
        text = (
            "(Local mode) I am Cipher AI and no OPENAI_API_KEY is configured. "
            "Set your key to enable real AI responses. "
            f"You said: {user_text}"
        )
        self.history.append({"role": "assistant", "content": text})
        return text


def run() -> None:
    """Run terminal chat loop."""
    bot = CipherAI()
    print("Cipher AI is ready. Type 'exit' to quit.")

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"exit", "quit"}:
            print("Cipher AI: Goodbye!")
            break
        if not user_text:
            continue
        print(f"Cipher AI: {bot.reply(user_text)}")


if __name__ == "__main__":
    run()
