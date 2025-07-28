# Getting started  

This section covers LLM/AI models usage and information documentation. 

Visit the streamlit ui (service that serves agent model through a GUI)to interact with the model here: 

**NOTE**: you *MUST* be on either H&H Secure or the H&H Quality Wifi networks

# Components

- Usage
- Hardware
- Software (Workstation)
- Definitions
- System Architecture
- Troubleshooting checklist

# Usage 

To use this software, first make sure you are logged into the company network via - H&H Secure, H&H Quality, or directly hard-wired into the network.

## Logging in

To use the system, please visit [H&H AI Assistant](http://10.0.0.21:8501) on any device with a web browser. You will be greated with the log in screen. 

To log in, you will need to:
1. Make an account (You will only need to do this once)
    - Select the Sign up option from the 'Action' dropdown
    - Log in with work email, and set a password. You wont recieve any emails, this is simply for logs and usage.

2. Sign in 
    - Select the 'Login' option from the 'Action' dropdown
    - Log in with user credentials

## Main System Page  

Here you can 
1. See Currently opened chat 
2. Name current chat 
3. create new chat or load another chat session 
4. click the link to the docs 
5. If you have any issues, please let dawson know with you session_id and chat.

## Core Principles for Crafting Effective Prompts

Creating effective prompts requires adherence to three fundamental principles: clarity, specificity, and relevance. These principles form the foundation 
of successful prompt engineering.

- **Clarity:** A clear prompt eliminates ambiguity, making sure the AI understands your request. For instance, instead of saying, “Explain this,” specify what “this” refers to and the type of explanation you require. A clear prompt might be, “Explain the concept of renewable energy in simple terms.” Now, that's not to say "explain this won't work, but it has a higher chance of not delivering desired output.
- **Specificity:** Narrowing the scope of your request reduces the likelihood of irrelevant or generic responses. For example, instead of asking, “Describe renewable energy,” you could say, “List three advantages of solar energy compared to fossil fuels.”
- **Relevance:** Align your prompt with the AI model’s capabilities (this is touched on in the usage section). Understanding the strengths and limitations of the system is crucial for crafting prompts that yield meaningful results. 

By applying these principles, you can create prompts that are actionable and precise, leading to more effective and reliable outputs.

## How to Prompt/Ways You can prompt 

Prompts will fall into one of these categories:

1. General Questions about process, company documents, etc 

    - These are queries about internal documents, processes, or general knowledge stored in the system's knowledge base (e.g., "Summarize the scope meeting" or "What is the company policy on safety?"). 
    - The system uses Retrieval-Augmented Generation (RAG) to search and summarize relevant documents. 
    - No special prefix is needed—just ask naturally. 

2. Question About Specific Shots/data points related to Press data 

    - This can be questions about bottom/top/overall in or out of spec parts (pass/fail) based on shot number, e.g., "How many failed shots in press20_data?" or "What is the average ActNozzleTemp over shot_num 100 to 200 in press20_data?"
    - Questions about specific machine data points, e.g., "List ActCycleTime for shot_num 50 in press20_data."
    - **Prefix Required:** Start your query with "press20_data" (e.g., "press20_data how many failed shots?"). The system will strip the prefix and route to the Press20 Data Agent, which converts natural language to SQL and queries the database.

3. Questions about tweaks, changes to process, or defects and how to combat them 

    - This can be something like, "I am seeing a lot of (certain defect), what machine settings can I adjust to change this" or "What is the definition of (insert defect)?" or "What are the common causes of (insert defect)?"
    - These are routed to the Analysis Agent for trends or defect suggestions. No special prefix needed—keywords like "defect," "fix," or "tweak" trigger it.

4. Calculations

    - Simple numerical queries, e.g., "What is 2 + 2?" or "Calculate 5 * (3 + 4)."
    - Routed to the Calculator Agent automatically if operators (+, -, *, /) are detected. No prefix needed.

5. Web Searches

    - External searches, e.g., "websearch. latest injection molding techniques."
    - **Prefix Required:** Start with "websearch." The system strips the prefix, searches using DuckDuckGo, crawls top results, filters content, and summarizes in markdown.
    - This Agent will act as a placeholder for missing knowledge the system may not have. Early on, it will be one of the more useful tools until we have a more tuned dataset for the model.

**Tips for all Prompts**

- Be direct and use natural language.
- For history-aware queries, the system remembers previous messages in the conversation.
- If unsure, start with "what can you do" for capabilities.
- Sometimes, you will need to ask the same question twice if you get a weird answer, I am still working on this.

## Hardware 

Ubuntu AI Workstation Specs:
- OS: 
- CPU:
- GPU: 
- Memory:
- Storage:

## Software Used in Project

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

# Definitions

**LLM (Large Language Model):** An AI model trained on vast data to understand and generate human-like text, used here for natural language queries and responses.

**RAG (Retrieval-Augmented Generation):** A technique where the AI retrieves relevant documents from a knowledge base before generating a response, ensuring accurate and context-specific answers.

**Agent:** A specialized AI component that handles specific tasks (e.g., routing queries, querying databases, or performing calculations).

**Master Agent:** The central router that decides which specialized agent to use based on the query type.

**Press20 Data Agent:** Handles queries on the press20_data table, converting natural language to SQL for data retrieval.

**Calculator Agent:** Performs simple arithmetic operations from user queries.

**Websearch Agent:** Searches the web, crawls pages, and summarizes results for external information.

**SQL Agent:** Sub-component of Press20 Agent that translates natural language to SQL queries.

**Chain-of-Thought (CoT):** Internal reasoning process used by agents to verify decisions, not visible in outputs.

**Session/Conversation:** A chat thread with history; switchable in the sidebar for multiple ongoing discussions.

**Markdown:** Formatting language used for outputs (e.g., bullets, tables) to make responses readable.

# Architecture 

This agent/system has a few different parts that make up a large portion of its funcionality:

- Master Agent  
- General Rag Agent
- Press20 Data Agent
- Calculator Agent 
- Websearch Agent 

## Master Agent 

The Master Agent is the central orchestrator. It receives all user queries and routes them to the appropriate specialized agent based on keywords or patterns:

- Checks for predefined commands like "who are you," "what can you do," or "help" and responds directly.
- Routes prefixed queries (e.g., "websearch." or "press20_data").
- Uses chain-of-thought internally to verify routing.
- Ensures outputs are always in markdown format.

## General RAG Agent 

The Press20 Data Agent queries the press20_data table for machine/shot data:

- Activated by queries starting with "press20_data" (prefix stripped).
- Uses SQL Agent to convert natural language to SQL (e.g., "how many failed shots" → SELECT COUNT(*) FROM press20_data WHERE overallPassFail = 'FAIL').
- Executes SQL and formats results as markdown bullets (e.g., - shot_num: 123\n- overallPassFail: FAIL).
- Handles errors like no data with markdown messages.

## Press20 Data Agent

The Press20 Data Agent queries the press20_data table for machine/shot data:

- Activated by queries starting with "press20_data" (prefix stripped).
- Uses SQL Agent to convert natural language to SQL (e.g., "how many failed shots" → SELECT COUNT(*) FROM press20_data WHERE overallPassFail = 'FAIL').
- Executes SQL and formats results as markdown bullets (e.g., - shot_num: 123\n- overallPassFail: FAIL).
- Handles errors like no data with markdown messages.

## Calculator Agent 

The Calculator Agent performs numerical computations:

- Detects operators (+, -, *, /) in queries.
- Executes calculations and returns simple markdown results (e.g., Result: 4).
- No prefix needed.

## Websearch Agent 

The Websearch Agent fetches external information:

- Activated by queries starting with "websearch." (prefix stripped).
- Searches using DuckDuckGo, crawls top results with Crawl4AI, filters content via LLM.
- Returns summarized markdown from pages (e.g., - From url.com: Summary text).

# Troubleshooting

## Common Errors 

**Error 404 - No Response**
Check network connection—must be on H&H Secure/Quality or hard-wired.
- Restart services with python start_services.py.
- Verify Ollama/Supabase containers are healthy in Docker.

**Slow Responses to Questions**
- Check GPU usage with btop—if not spiking, restart services.
- Ensure no heavy loads on the workstation.
- For websearch, limit to specific queries to reduce crawl time.

## Checklist 

1. Check internet connection of devices (workstation, users device, etc.) - make sure you are on the H&H network
2. Check health of docker containers - if any are unhealthy, run python start_services.py  in the local-ai folder to restart system 
3. Check to make sure GPU is being used - if system is running slow, use btop on the workstation and run a query. if the GPU usage doesnt spike, run python start_services.py in the local-ai folder to restart system  
4. Check to make sure that the streamlit app is running. This is what starts the whole system up (will be docker-ized soon)
5. Verify Supabase connection—test queries in dashboard.
6. Clear browser cache or try incognito mode for Streamlit issues.
7. If agent routing fails (e.g., wrong responses), check prompt keywords match exactly (case-insensitive).
