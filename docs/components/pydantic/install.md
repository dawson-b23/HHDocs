# Install — Pydantic AI

Quick (concise)
- Create venv: `python3 -m venv .venv && source .venv/bin/activate`
- Install: `pip install pydantic 'pydantic-ai'` (or `pip install -r requirements.txt` if provided)

Comprehensive
- Recommended Python: 3.10+
- Use `pipx` for CLI tools if you prefer: `pipx install pydantic-ai`
- If you target specific LLM backends, also install their SDKs, e.g. `pip install openai` or `pip install ollama-client`.

Notes
- Lock dependencies with `pip freeze > requirements.txt` for reproducible environments.
