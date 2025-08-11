---
layout: default
title: LLMs
---
{% include navigation.html %}

# Getting started  
This section covers LLM/AI models usage and information documentation. 

Visit the streamlit ui (service that serves agent model through a GUI)to interact with the model here: 

**NOTE**: you *MUST* be on either H&H Secure or the H&H Quality Wifi networks


# Definitions

# Usage 

# Core Principles for Crafting Effective Prompts
Creating effective prompts requires adherence to three fundamental principles: clarity, specificity, and relevance. These principles form the foundation 
of successful prompt engineering.

- **Clarity:** A clear prompt eliminates ambiguity, making sure the AI understands your request. For instance, instead of saying, “Explain this,” specify what “this” refers to and the type of explanation you require. A clear prompt might be, “Explain the concept of renewable energy in simple terms.” Now, that's not to say "explain this won't work, but it has a higher chance of not delivering desired output.
- **Specificity:** Narrowing the scope of your request reduces the likelihood of irrelevant or generic responses. For example, instead of asking, “Describe renewable energy,” you could say, “List three advantages of solar energy compared to fossil fuels.”
- **Relevance:** Align your prompt with the AI model’s capabilities (this is touched on in the usage section). Understanding the strengths and limitations of the system is crucial for crafting prompts that yield meaningful results. 

By applying these principles, you can create prompts that are actionable and precise, leading to more effective and reliable outputs.

# Architecture 
This agent/system has a few different parts that make up a large portion of its funcionality:

- Master Agent  
- General Rag Agent
- Press20 Data Agent
- Calculator Agent 
- Websearch Agent 

# Tools Used in Project
A list of tools that were used to make this project possible (some will have links with further detail that can be found in sidebar):

- Docker 
- Ollama 
- Llama3.1:8b 
- OpenWebUI
- Pydantic AI 
- n8n
- Postgres
- Supabase
- Langfuse
- Streamlit 
- FastAPI
- Redis
- Searxng
- Docling 
