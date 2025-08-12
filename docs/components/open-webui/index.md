# Open WebUI — Setup and n8n Integration

Open WebUI provides a browser chat interface for local LLMs and supports adding custom Functions that can trigger n8n workflows via webhooks. This page explains how to add the included `n8n_pipe.py` function and connect it to n8n.

---

## Quick setup

1. Start the stack: `python local-ai-copy/start_services.py --environment private`.
2. Open Open WebUI at `http://localhost:3000/`.
3. Create a local account (one-time setup).

---

## Adding the n8n function (detailed)

1. In Open WebUI, go to Workspace → Functions → Add Function.
2. Copy the contents of `local-ai-copy/n8n_pipe.py` and paste into the code editor.
3. In the function settings, configure these fields:
   - `name`: e.g., `n8n_bridge`
   - `description`: short explanation like "Calls local n8n RAG workflow via webhook"
   - `n8n_url`: set to the "Production" webhook URL you copied from n8n (e.g., `http://localhost:5678/webhook/abcd`)
   - Any additional environment or headers the function expects (open the Python code to confirm).
4. Toggle the function on. It will appear in the model dropdown and can be used inside the chat UI to trigger your n8n workflow.

Testing the function:
- Open Open WebUI, select a model, and in the Function dropdown choose `n8n_bridge`.
- Ask a simple test prompt that triggers n8n, for example: "Run test workflow with sample payload". Watch n8n for a webhook execution.

Example payload & headers (what `n8n_pipe.py` sends):
- Headers include an Authorization Bearer token (optional) and `Content-Type: application/json`.
- JSON payload shape sent to n8n:
  {
    "sessionId": "<chat_id>",
    "chatInput": "<user question>"
  }
- The function expects the n8n workflow response JSON to contain a field `output` (configurable via `response_field`) which it will append to the Open WebUI assistant messages.

Troubleshooting:
- If no webhook is received, verify the `n8n_url` is reachable from the Open WebUI container. Run from host: `docker compose -p localai exec openwebui curl -v <n8n_url>` to confirm connectivity.
- Confirm `n8n_bearer_token` (if set) matches the token the n8n webhook expects.
- Check Open WebUI logs: `docker compose -p localai logs -f openwebui` and n8n logs: `docker compose -p localai logs -f n8n`.
- If `n8n` returns an error response, the function will raise and report the HTTP status and body; inspect the n8n workflow execution logs to find the failing node.


---

## Notes for Mac users running Ollama locally

- If Ollama runs on the host macOS (not in Docker), point n8n to `host.docker.internal:11434` for `OLLAMA_HOST` and configure the n8n Ollama credential accordingly.

---

## Debugging

- If the function does not trigger the workflow, verify the webhook URL (Production webhook), and check n8n logs: `docker compose -p localai logs -f n8n`.
- Ensure network connectivity inside Docker: the Open WebUI container must be able to reach the n8n webhook endpoint or public webhook URL if Caddy is used.
