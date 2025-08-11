# Self-hosted AI Package

This document details the Self-hosted AI Package, an open Docker Compose template designed to quickly bootstrap a fully-featured Local AI and Low Code development environment. It includes various components for local LLMs, an interface for N8N agents, and a comprehensive database, vector store, and authentication solution.

## Overview

This package is an enhanced version of the original Local AI Starter Kit by the n8n team, with improvements and additions by Cole. Key additions include Supabase, Open WebUI, Flowise, Neo4j, Langfuse, SearXNG, and Caddy. It also pre-configures local RAG AI Agent workflows within your n8n instance.

**Important Note:** Supabase has updated some environment variables. If you have an existing setup, you may need to add new default values from the `.env.example` file to your `.env` file. Specifically, `POOLER_DB_POOL_SIZE=5` is now required if the package was running before June 14th.

Below is an expanded, technical reference extracted from the `local-ai-copy/` folder to help an engineer run, debug, and extend the system.

### Included Components (detailed)

- **n8n**: low-code automation platform. The n8n service is configured for local use and uses shared volume mounts for file triggers. Default UI at `http://localhost:5678`.
- **Supabase**: Provides Postgres, Auth, Storage, and Functions. Run via `supabase/docker/docker-compose.yml`. Internal Postgres host is `db` and typical access uses `POSTGRES_PASSWORD` from `.env`.
- **Ollama**: Local LLM runtime. Models are downloaded inside the Ollama image; expect initial model pull delays when first starting the system.
- **Open WebUI**: Chat UI exposed on `http://localhost:3000` by default; integrates with n8n via functions.
- **Flowise**: Visual node-based builder for AI pipelines. Useful for prototyping.
- **Qdrant**: Vector store; URL `http://qdrant:6333` inside Docker network.
- **Neo4j**: Knowledge graph engine; persists files under `local-ai-copy/neo4j/data/`.
- **SearXNG**: Meta-search engine; requires `searxng/settings.yml` which is created from `settings-base.yml` on first run—secrets must be generated for it.
- **Caddy**: TLS reverse proxy. Configure hostnames in `.env` and `Caddyfile` for production.
- **Langfuse/ClickHouse/MinIO**: Observability and storage components; require secure secrets in `.env`.




## Important Links

*   [Local AI community forum](https://thinktank.ottomator.ai/c/local-ai/18) over in the oTTomator Think Tank
*   [GitHub Kanban board](https://github.com/users/coleam00/projects/2/views/1) for feature implementation and bug squashing.
*   [Original Local AI Starter Kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) by the n8n team
*   Download the N8N + OpenWebUI integration [directly on the Open WebUI site.](https://openwebui.com/f/coleam/n8n_pipe/)

## Included Components

The package combines the self-hosted n8n platform with a curated list of compatible AI products and components:

*   **Self-hosted n8n**: A low-code platform with over 400 integrations and advanced AI components.
*   **Supabase**: An open-source database-as-a-service, widely used for AI agents, providing database, vector store, and authentication.
*   **Ollama**: A cross-platform LLM platform for installing and running the latest local LLMs.
*   **Open WebUI**: A ChatGPT-like interface for private interaction with local models and N8N agents.
*   **Flowise**: A no/low-code AI agent builder that integrates well with n8n.
*   **Qdrant**: An open-source, high-performance vector store with a comprehensive API. It's faster than Supabase for certain RAG (Retrieval Augmented Generation) use cases.
*   **Neo4j**: A knowledge graph engine that powers tools like GraphRAG, LightRAG, and Graphiti.
*   **SearXNG**: An open-source, free internet metasearch engine that aggregates results from up to 229 search services, ensuring user privacy.
*   **Caddy**: Provides managed HTTPS/TLS for custom domains.
*   **Langfuse**: An open-source LLM engineering platform for agent observability.

## Prerequisites

Before you begin, ensure you have the following software installed:

*   **Python**: Required to run the setup script.
*   **Git/GitHub Desktop**: For easy repository management.
*   **Docker/Docker Desktop**: Required to run all services.

## Installation

1.  **Clone the repository and navigate to the project directory:**
    ```bash
    git clone -b stable https://github.com/coleam00/local-ai-packaged.git
    cd local-ai-packaged
    ```

2.  **Set up environment variables for Supabase:**
    *   Make a copy of `.env.example` and rename it to `.env` in the root directory.
    *   Set the required environment variables for N8N, Supabase, Neo4j, and Langfuse secrets.
    *   **IMPORTANT:** Generate secure random values for all secrets. Do not use example values in production.

3.  **Optional: Set environment variables for production deployment (if applicable):**
    *   Configure Caddy hostnames for N8N, Open WebUI, Flowise, Supabase, Ollama, SearXNG, Neo4j, and your Let's Encrypt email.

4.  **Start services using `start_services.py`:**
    This script handles starting both Supabase and local AI services and accepts a `--profile` flag for GPU configuration.

    *   **For Nvidia GPU users:**
        ```bash
        python start_services.py --profile gpu-nvidia
        ```
        *Note: If you haven't used your Nvidia GPU with Docker, follow the [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).*

    *   **For AMD GPU users on Linux:**
        ```bash
        python start_services.py --profile gpu-amd
        ```

    *   **For Mac / Apple Silicon users:**
        *   **Run fully on CPU:**
            ```bash
            python start_services.py --profile cpu
            ```
        *   **Run Ollama on Mac for faster inference (connect from n8n instance):**
            ```bash
            python start_services.py --profile none
            ```
            *If running Ollama locally on Mac, modify `OLLAMA_HOST` in `docker-compose.yml` to `host.docker.internal:11434` and update the base URL in n8n credentials.*

    *   **For everyone else:**
        ```bash
        python start_services.py --profile cpu
        ```

5.  **The `environment` argument:**
    The `start_services.py` script offers `private` (default) and `public` options for the environment:
    *   **private:** For safe environments where many ports can be accessible.
    *   **public:** For public environments, minimizing attack surface by closing all ports except 80 and 443.

## Deploying to the Cloud

### Prerequisites

*   Linux machine (preferably Ubuntu) with Nano, Git, and Docker installed.

### Extra Steps

Before pulling the repository and installing:

1.  **Open necessary ports (as root):**
    ```bash
    ufw enable
    ufw allow 80 && ufw allow 443
    ufw reload
    ```
    *Warning: `ufw` does not shield ports published by Docker. Ensure all traffic runs through Caddy via port 443, and port 80 is only used for redirection.*

2.  **Run `start_services.py` with `--environment public`:**
    ```bash
    python3 start_services.py --profile gpu-nvidia --environment public
    ```
    This closes all ports except 80 and 443.

3.  **Set up A records for DNS provider:**
    Point your subdomains (configured in `.env` for Caddy) to the IP address of your cloud instance.

    *Note: If "docker compose" command is not available (e.g., Ubuntu GPU instance on DigitalOcean), install it manually before running `start_services.py`.*

## Quick Start and Usage

The Docker Compose file is pre-configured with network and disk. After installation:

1.  **Set up n8n:** Open <http://localhost:5678/> in your browser. This is a one-time setup for a local account.
2.  **Open the included workflow:** <http://localhost:5678/workflow/vTN9y2dLXqTiDfPT>
3.  **Create credentials for every service:**
    *   Ollama URL: `http://ollama:11434`
    *   Postgres (through Supabase): Use DB, username, and password from `.env`. Host is `db`.
    *   Qdrant URL: `http://qdrant:6333` (API key can be anything locally).
    *   Google Drive: Follow [n8n's guide](https://docs.n8n.io/integrations/builtin/credentials/google/).
4.  **Test workflow:** Select "Test workflow" to start. You may need to wait for Ollama to download Llama3.1.
5.  **Activate workflow:** Toggle the workflow as active and copy the "Production" webhook URL.
6.  **Set up Open WebUI:** Open <http://localhost:3000/> in your browser. This is a one-time setup for a local account.
7.  **Add function in Open WebUI:** Go to Workspace -> Functions -> Add Function. Paste code from `n8n_pipe.py` (also [published here](https://openwebui.com/f/coleam/n8n_pipe/)).
8.  **Configure n8n_url:** Click the gear icon and set `n8n_url` to the production webhook URL copied earlier.
9.  **Toggle function on:** The function will now be available in your model dropdown.

To open n8n at any time, visit <http://localhost:5678/>.
To open Open WebUI at any time, visit <http://localhost:3000/>.

Your n8n instance provides over 400 integrations and AI nodes. For local operations, use the Ollama node for your language model and Qdrant as your vector store.

*Note: This starter kit is for proof-of-concept projects and not fully optimized for production environments.*

## Upgrading

To update all containers to their latest versions:

```bash
# Stop all services
docker compose -p localai -f docker-compose.yml --profile <your-profile> down

# Pull latest versions of all containers
docker compose -p localai -f docker-compose.yml --profile <your-profile> pull

# Start services again with your desired profile
python start_services.py --profile <your-profile>
```
Replace `<your-profile>` with `cpu`, `gpu-nvidia`, `gpu-amd`, or `none`. The `start_services.py` script only restarts or pulls containers if they are new; it does not update existing ones.

## Troubleshooting

### Supabase Issues

*   **Supabase Pooler Restarting**: Follow instructions in [this GitHub issue](https://github.com/supabase/supabase/issues/30210#issuecomment-2456955578).
*   **Supabase Analytics Startup Failure**: Delete `supabase/docker/volumes/db/data` if the container fails after changing Postgres password.
*   **Docker Desktop**: Ensure "Expose daemon on tcp://localhost:2375 without TLS" is enabled in Docker settings.
*   **Supabase Service Unavailable**: Avoid "@" character in Postgres password. Other special characters might also cause issues.
*   **SearXNG Restarting**: Run `chmod 755 searxng` within the `local-ai-packaged` folder.
*   **Files not Found in Supabase Folder**: Delete the `supabase/` folder and retry `start_services.py`.

### GPU Support Issues

*   **Windows GPU Support**: Enable WSL 2 backend in Docker Desktop settings. See [Docker GPU documentation](https://docs.docker.com/desktop/features/gpu/).
*   **Linux GPU Support**: Follow the [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

## Recommended Reading

n8n offers useful content for AI concepts and nodes:

*   [AI agents for developers: from theory to practice with n8n](https://blog.n8n.io/ai-agents/)
*   [Tutorial: Build an AI workflow in n8n](https://docs.n8n.io/advanced-ai/intro-tutorial/)
*   [Langchain Concepts in n8n](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/)
*   [Demonstration of key differences between agents and chains](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/)
*   [What are vector databases?](https://docs.n8n.io/advanced-ai/examples/understand-vector-databases/)

## Video Walkthrough

*   [Cole's Guide to the Local AI Starter Kit](https://youtu.be/pOsO40HSbOo)

## More AI Templates

Visit the [**official n8n AI template gallery**](https://n8n.io/workflows/?categories=AI) for more workflow ideas.

### Learn AI key concepts

*   [AI Agent Chat](https://n8n.io/workflows/1954-ai-agent-chat/)
*   [AI chat with any data source (using the n8n workflow too)](https://n8n.io/workflows/2026-ai-chat-with-any-data-source-using-the-n8n-workflow-tool/)
*   [Chat with OpenAI Assistant (by adding a memory)](https://n8n.io/workflows/2098-chat-with-openai-assistant-by-adding-a-memory/)
*   [Use an open-source LLM (via HuggingFace)](https://n8n.io/workflows/1980-use-an-open-source-llm-via-huggingface/)
*   [Chat with PDF docs using AI (quoting sources)](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)
*   [AI agent that can scrape webpages](https://n8n.io/workflows/2006-ai-agent-that-can-scrape-webpages/)

### Local AI templates

*   [Tax Code Assistant](https://n8n.io/workflows/2341-build-a-tax-code-assistant-with-qdrant-mistralai-and-openai/)
*   [Breakdown Documents into Study Notes with MistralAI and Qdrant](https://n8n.io/workflows/2339-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant/)
*   [Financial Documents Assistant using Qdrant and Mistral.ai](https://n8n.io/workflows/2335-build-a-financial-documents-assistant-using-qdrant-and-mistralai/)
*   [Recipe Recommendations with Qdrant and Mistral](https://n8n.io/workflows/2333-recipe-recommendations-with-qdrant-and-mistral/)

## Tips & Tricks

### Accessing local files

The self-hosted AI starter kit creates a shared folder (by default, in the same directory) mounted to the n8n container. This allows n8n to access files on disk at `/data/shared`.

**Nodes that interact with the local filesystem:**

*   [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filesreadwrite/)
*   [Local File Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger/)
*   [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/)

## License

This project (originally by the n8n team) is licensed under the Apache License 2.0.
