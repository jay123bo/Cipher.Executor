# Cipher AI

Cipher AI is a lightweight terminal chatbot app meant to replace the original executor concept with a safe AI assistant.

## What you get after Download ZIP

If someone clicks **Code → Download ZIP**, extracts it, and opens the folder, they will see:

- `Cipher/` (project folder)
- `cipher_ai.py` (the runnable app)
- `requirements.txt`
- `README.md`

## Features

- Interactive chat loop in terminal
- Optional OpenAI-compatible API support (`OPENAI_API_KEY`)
- Local fallback mode when no API key is set
- Conversation history saved during a session

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python cipher_ai.py
```

## Environment variables

- `OPENAI_API_KEY`: required for real model responses
- `OPENAI_BASE_URL`: optional custom base URL for compatible providers
- `CIPHER_MODEL`: optional model name (default: `gpt-4o-mini`)

Without `OPENAI_API_KEY`, Cipher AI runs in local fallback mode.

## Example

```text
You: write a short study plan for python
Cipher: Here's a focused 7-day Python study plan...
```
