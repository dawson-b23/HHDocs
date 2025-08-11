# Ollama — Local Model Runtime (Beginner's Guide)

Ollama runs local LLMs inside Docker and serves them on `http://ollama:11434` inside the Docker network. This page explains how Ollama is used, model considerations, and GPU tips.

---

## What Ollama provides

- Local hosting of LLM models (e.g., Llama 3.x).
- HTTP API for inference used by n8n and Open WebUI.

---

## Usage notes

- From within Docker services, use `http://ollama:11434` as the model API URL.
- If running Ollama on macOS host, use `host.docker.internal:11434` and update service credentials.
- The first model download can take a long time; check Ollama container logs for progress: `docker compose -p localai logs -f ollama`.

---

## GPU support tips

- For Nvidia GPUs, ensure Docker has GPU support and you have the correct runtime. Follow Ollama Docker docs.
- For AMD GPUs on Linux, use the `gpu-amd` profile where provided.
- On macOS, GPU sharing with Docker is not available — use CPU or run Ollama natively on the host.

---

## Troubleshooting

- If models fail to download, check container logs and available disk space.
- If inference is slow, verify GPU access and that the container is attached to the GPU runtime.