# Ollama — Component


# Ollama — Local Model Runtime (Beginner's Guide)

Ollama runs local LLMs inside Docker and serves them on `http://ollama:11434` inside the Docker network. This page explains how Ollama is used, model considerations, and GPU tips.

## What Ollama provides

- Local hosting of LLM models (e.g., Llama 3.x).
- HTTP API for inference used by n8n and Open WebUI.

## Usage notes

- From within Docker services, use `http://ollama:11434` as the model API URL.
- If running Ollama on macOS host, use `host.docker.internal:11434` and update service credentials.
- The first model download can take a long time; check Ollama container logs for progress: `docker compose -p localai logs -f ollama`.

## GPU support tips

- For Nvidia GPUs, ensure Docker has GPU support and you have the correct runtime. Follow Ollama Docker docs.
- For AMD GPUs on Linux, use the `gpu-amd` profile where provided.
- On macOS, GPU sharing with Docker is not available — use CPU or run Ollama natively on the host.

## Troubleshooting

- If models fail to download, check container logs and available disk space.
- If inference is slow, verify GPU access and that the container is attached to the GPU runtime.

## Model considerations

### Model configuration

I recommend not changing any of the settings in the docker-compose.yml file. The defaults are optimized for performance and stability. If you switch to a model that is not gpt-oss, you can 
un-comment the [insert names here], which will speed up the models that aren't gpt (this is because of gpt's custom new quant - HMPK4). 

You can look at the model parameters for a given model by running:

```bash
docker exec -it ollama /bin/bash
```

```bash
ollama list 
```

```bash
ollama show gpt-oss:20b
```

```bash
ollama show gpt-oss:20b --modelfile
```

This will show you the model parameters, and you can change them if you want to. This will work for all models, not just gpt-oss. Next we will cover changing parameters, and some of the ones I changed.

```bash
ollama run gpt-oss:20b 
```

```bash
/set parameter num_ctx 65536
```

```bash
/save gpt-oss:20b-64k
```

### Model parameters

The following are the parameters I changed for gpt-3.5-turbo.


### Model download

Models are stored in the container at `/models`.

### Model size

Models are stored in the container at `/models`. The Ollama container is configured to use the `nvidia` runtime, which requires GPU access.

### Model format

Models are stored in the `.bin` format. The Ollama container is configured to use the `nvidia` runtime, which requires GPU access.

### Model license

Models are stored in the container at `/models`.
