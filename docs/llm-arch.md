# LLM Architecture

This page summarizes the H&H AI Assistant architecture and agents.

---

## Overview
The H&H AI Assistant is modular, using Streamlit for UI, Pydantic-based agents for orchestration, Supabase for data and auth, ChromaDB for embeddings and vectory search, and Ollama for local LLM hosting. Langfuse is used for observability.

---
## Code Layout

### Github Repository
https://github.com/pegasora/local-ai

**Note**: This is private github repository, so you will need to be a member of the HH Molds Inc. Currently, only Gary and Dawson have access to the repository.

### Docs
https://github.com/pegasora/HHDocs

- This is where you will find the documentation for the project, may be out-of-date at a later point. 
- To see the most up-to-date docs, you will need to build them via docsify from the Local-AI repository (the /docs folder).
- Gary will be in charge of maintaining this documentation and any new additions.

--- 

## Ubuntu Workstation Layout 

### Tank 
/tank is the mount point for the 4TB HDD drive where all of the data for images, chromadb, and others currently lives. Supabase's data is in the /home/local-ai folder as of right now, 
and in the future will be moved to the tank. This is very long term, does not need to happen right now. It is in the root area of the system, and therefore will need sudo (admin) access.

### Local AI 

### Pydantic-models 
Everything related to the Pydantic models is located in the /home/local-ai/pydantic-models folder. The pydantic folder has the following layout:

- /pydantic-models/models
- /pydantic-models/tests
- /pydantic-models/scripts
- /pydantic-models/README.md

The models folder contains all of the pydantic models for the project.

--- 

## Frontend

The frontend is built using Streamlit. It is a Python library for simple, interactive web apps. Does not allow for fine grain control, likely one of the first things to explore upgrading.

[Streamlit UI](https://user-images.githubusercontent.com/11437163/230182250-c7e7f3f1-f8f0-4f6c-b1c1-a9a8b2f7c6e0.png)

It allows for easy creation of web apps with a focus on interactivity and user experience, especailly since I am not a frontend dev.

This can be kind of janky, but it is a good starting point, and definitely a good way to demonstrate proof of concept.

---

## Backend

The backend is built using Python. It is a powerful and versatile programming language that is widely used in data science, machine learning, and web development.

[Python](https://user-images.githubusercontent.com/11437163/230182263-e1e5d4f7-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It is known for its simplicity, readability, and versatility, making it a popular choice for a wide range of applications.

---

## Database

The database is built using Supabase. It is a cloud or locally based database that provides a secure and scalable platform for storing and retrieving data. In this project, it is the self-hosted version.

[Supabase](https://user-images.githubusercontent.com/11437163/230182270-f3a7f0c6-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It offers a range of features, including user authentication, real-time data synchronization, and data backup and recovery.

---

## LLM

The LLM is built using Ollama. It is a local LLM hosting service that allows for the running of LLMs locally inside Docker containers.

[Ollama](https://user-images.githubusercontent.com/11437163/230182277-0a8f3a9a-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It provides a range of features, including model management, model inference, and model deployment.

---

## Docker 

All components are run inside Docker containers. This allows for easy deployment and management of the components.

[Docker](https://user-images.githubusercontent.com/11437163/230182291-2a8f3a9a-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It also allows for easy management of the components, including versioning, updates, and rollbacks. The biggest additional bonus is 
providing a consistent environment for all components, ensuring that they all run the same version of the same software, and if something does go wrong,
it doesn't brick you system and can be easily rolled back to a previous version.

---

## AI

The agents are built using Pydantic AI. It is a Python library for defining data models and serializing them to JSON or other formats. Very powerful for expected I/O and control flow.

[Pydantic](https://user-images.githubusercontent.com/11437163/230182284-1a8f3a9a-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It provides a range of features, including data validation, serialization, and deserialization.

---

## Observability

The observability is built using Langfuse. It is a Python library for collecting and visualizing data from various sources, such as Prometheus, Grafana, and OpenTelemetry (in this case we are using OpenTelemetry).

[Langfuse](https://user-images.githubusercontent.com/11437163/230182291-2a8f3a9a-c1a0-4b3a-b0a1-a9a8b2f7c6e0.png)

It provides a range of features, including data collection, visualization, and alerting.

---

## Agents

### Currently in use
*General RAG Agent*: document retrieval and answer generation. This agent is the most flexible, can adapt to new knowledge via document ingestion - allows for fine-tuning of knowledge access.
  - Used for: General questions, general information retrieval such as "What is X defect," "How to fix X defect/what causes X defect," and can answer questions about data sheets, etc.
*Calculator Agent*: evaluates simple math.

*Websearch Agent*: performs external web searches when prefixed with `websearch.`
  - Used for: Websearches that take the top 2 results and summarize them. Was used as a supplementary agent until RAG was better.
*Logging Agent*: logs setup changes for press or part, allows users to query using natrual language.
  - Used for:  Logging changes to press setups. Keeping track of changes for techs.
  - Agent also has a helper agent "logging_sql_agent" that translates NL to SQL and queries.

### Deprecated
*Master Agent*: routes queries. THIS IS CURRENTLY DEPRECATED. It was replaced by a dropdown menu for routing queries. With some system upgrades, this becomes more feasible.

### Planned
*Press20 Data Agent*: converts natural language to SQL and queries press20_data.
  - Agent also has a helper agent "sql_agent" that translates NL to SQL and queries.
*Analysis Agent*: performs analysis on data. This agent is currently being developed, and relys on the completion of the press20 agent.

---

## Troubleshooting and Checklist
- Ensure network connectivity (H&H Secure/Quality or wired).
- Restart services: `python start_services.py`.
- Check Docker containers and GPU usage.

<!-- Migrated and merged from old_docs/HHDocs/docs/llm-arch.md and llm-old.md -->
