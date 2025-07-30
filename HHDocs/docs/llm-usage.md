# H&H AI Assistant Usage Documentation

## Introduction

**NOTE**: you *MUST* be on either H&H Secure or the H&H Quality Wifi networks

The H&H AI Assistant is a web-based application built with Streamlit and Pydantic, designed to assist with injection molding queries. It supports multiple modes for handling different types of questions:

- **General Mode**: Uses Retrieval-Augmented Generation (RAG) to query and summarize documents, including listing documents, fetching file contents, and running SQL queries on tabular data.
- **Press Data Mode**: Queries the `press20_data` table using natural language to SQL conversion, allowing analysis of machine data like shot numbers, temperatures, pressures, and pass/fail statuses.
- **Websearch Mode**: Performs web searches, crawls pages, and summarizes content relevant to the query.

The app integrates with services like Supabase for authentication and data storage, ChromaDB for vector search, Ollama for local LLM inference, and Langfuse for observability. It runs in a Dockerized environment for persistence and ease of deployment.

This documentation covers access, authentication, and detailed usage. It assumes the application is deployed via Docker Compose as described in previous instructions.

## Help 

To get help for modes you can enter one of these queries into the general mode:
  - general-mode.md
  - press20-mode.md
  - websearch-mode.md
  - what-can-you-do.md
  
Entering any of these into the chat (general mode) will make the model output contents it has saved regarding those services.

## Definitions

**LLM (Large Language Model):** An AI model trained on vast data to understand and generate human-like text, used here for natural language queries and responses.

**RAG (Retrieval-Augmented Generation):** A technique where the AI retrieves relevant documents from a knowledge base before generating a response, ensuring accurate and context-specific answers.

**Agent:** A specialized AI component that handles specific tasks (e.g., routing queries, querying databases, or performing calculations).

**Press20 Data Agent:** Handles queries on the press20_data table, converting natural language to SQL for data retrieval.

**Websearch Agent:** Searches the web, crawls pages, and summarizes results for external information.

**SQL Agent:** Sub-component of Press20 Agent that translates natural language to SQL queries.

**Chain-of-Thought (CoT):** Internal reasoning process used by agents to verify decisions, not visible in outputs.

**Session/Conversation:** A chat thread with history; switchable in the sidebar for multiple ongoing discussions.

## Accessing the Application

1. **Open in Browser**:

    - Go to [LLM Website](http://10.0.0.21:8501) 
    - The page title is "H&H AI Assistant" with a robot icon (🤖).
    - If the app doesn't load, tell Dawson or whoever is in chareg of the app and check Docker logs for errors (e.g., connection issues to Supabase, chroma, or Ollama).

2. **Troubleshooting Access**:

    - Network: Make sure you are either connected to H&H Secure, or H&H Quality Wifi networks (or hardwired in to ethernet).
    - Browser Cache: Clear cache or try incognito mode if UI issues occur.

## Signup and Login

The app uses Supabase for authentication (enabled when `DEPLOY = True` in `app.py`). Anonymous access is not supported in production mode.

### Signup

1. On the login screen (displayed if not authenticated), select "Sign Up" from the "Action" dropdown.
2. Enter a valid email address (e.g., `user@example.com`). Don't worry you will never recieve spam or emails, this is just for user authentication. You can use work email or personal.
3. Enter a password (at least 6 characters; Supabase enforces basic rules).
4. Click "Register".
5. If successful, you'll see "Registered! Log in." 
6. Troubleshooting:

    - Error like "Sign-up failed": Tell Dawson and he will check email/password format or Supabase logs 
    - Duplicate email: Use a unique email.

### Login

1. On the login screen, select "Login" from the "Action" dropdown (default).
2. Enter your registered email and password.
3. Click "Login".
4. If successful, you'll see "Welcome back, [email]!" and be redirected to the main app interface.
5. The sidebar will show "Logged in as: [email]" and the H&H logo.
6. Troubleshooting:

    - "Login failed": Verify credentials or reset password via Supabase dashboard if needed.
    - Session persistence: The app uses Streamlit session state; closing the browser logs you out—re-login required.

### Logout

1. In the sidebar, click "Logout".
2. You'll be redirected to the login screen, and session data is cleared.

### Account Management

- No built-in password reset or profile editing in the app—handle via Supabase admin panel (access at `http://localhost:8000` with Supabase credentials).
- For security: Use strong passwords and monitor Supabase logs for unauthorized attempts.
- If you forget your log in information, use a new email or contact Dawson (or whoever is in charge) to reset user information.

## Using the Application

Once logged in, the interface consists of a sidebar for controls and a main chat area for interactions.

### Sidebar Controls

- **Header**: "H&H AI Assistant" with logo and logged-in email.
- **Mode Selector**: Choose the query mode (dropdown: "general", "press_data", "websearch").

    - General: For document-based queries (e.g., "Summarize the models.py file").
    - Press Data: For machine data queries (e.g., "Average ActNozzleTemp for shots 100-200").
    - Websearch: For internet-related queries (e.g., "Latest trends in injection molding").

- **Show COT Toggle**: Checkbox to display Chain-of-Thought (COT) reasoning in responses (default: enabled). COT shows the agent's internal thinking process. This sometimes disconnects with tool calls/agent mode.
- **Conversation Selector**: Dropdown to switch between chat sessions. Each shows title, ID, and timestamp (e.g., "New Chat (ID: uuid) - 2025-07-28T12:00:00").
- **New Chat Button**: Starts a new session with a unique ID. Switches to it automatically.
- **Rename Current Chat**: Text input to rename the active session (e.g., from "New Chat" to "Molding Trends"). Click "Rename" to save.
- **Help Section**:

    - "Ask about docs, press20 data, calculations, trends, defects."
    - Link to Docs: [https://dawson-b23.github.io/HHDocs/](https://dawson-b23.github.io/HHDocs/)
    - Contact: intern@hhmoldsinc.com | 832-977-3004

### Main Chat Interface

- **Title**: "H&H AI Assistant" with a brief description: "Assist with injection molding: queries on Press20, docs, calculations, trends, defect fixes."
- **Chat History**: Displays previous messages.
- User messages: In blue bubbles (e.g., your query).
- Assistant responses: In gray bubbles, showing:

  - **Agent Mode**: e.g., "General" or "Press Data". There is a bug where sometimes this will be "Unknown"
  - **COT** (if enabled): The agent's reasoning (e.g., "Thinking: [steps]").
  - **Model Response**: The final answer.

- **Input Field**: At the bottom—"Your question..." placeholder. Type your query and press Enter.
- Queries are processed based on the selected mode.
- First query in a "New Chat" auto-renames the session to a truncated version of the query (e.g., "how many failed shots..." becomes "how many failed shots"). You can rename this chat if needed.
- **Spinner**: Shows "Processing..." during queries (may take seconds due to LLM inference).

### Querying in Different Modes

#### General Mode
- Use for document-related tasks.
 
In this mode, you can ask general questions with a few having specific formats. It will answer based on whats in the knowledge base, if there is a gap, you can use a websearch. 
You can ask "what is a [insert defect]," "what are causes of [insert defect]," and "how to troubleshoot/fix [insert defect]." Talk to this normally like you would any chatbot.

- Examples:

  - "List all documents": Lists titles, IDs, schemas.
  - "What is splay"
  - "What are the causes of splay"
  - "How to fix splay" or "fix splay" or any variation of this.
  - For help: Use these queries to find more information: 
      - "general-mode.md"
      - "press20-mode.md"
      - "websearch-mode.md"

- Responses use RAG: Searches ChromaDB, formats context, and generates answers.

#### Press Data Mode
- For analyzing `press20_data` table (machine timestamps, temperatures, pressures, etc.).
- Natural language to SQL: e.g., "How many failed shots" → SQL like `SELECT COUNT(shot_num) FROM press20_data WHERE overallpassfail = 'FAIL'`.

- Examples:

    - "Average actnozzletemp over shot_num 100 to 200".
    - "Number of FAIL shots" (can specify for overallpassfail, bottompassfail, toppassfail for stopbox compacts)
    - "Shots with bottomanomalylevel greater than 0.5".
    - Outputs formatted data (e.g., key-value pairs per row).

#### Websearch Mode
- For external knowledge. Use this like a regular search engine. It will take the top 5 results, then scrape, aggreagte, and summarize the pages.
- Searches web, crawls pages, filters/summarizes content.

- Examples:

    - "Defect fixes for injection molding".
    - Outputs: Aggregated summaries from top results.

### Chat History and Sessions

- History persists per session via Supabase.
- Switch sessions: Loads messages without losing data.
- New chats start empty.
- No deletion—manage via Supabase if needed.
- If you have any problems, please contact Dawson with the chat name and ID, as well as what your problem was.

### Best Practices

- **Query Tips**: Be specific (e.g., include keywords like "shot_num", "temperature"). Use modes wisely to avoid irrelevant results. Try a query again if you get weird results.
- **Performance**: Local Ollama may be slow; monitor CPU/GPU usage. Increase retries in agent configs if errors occur.
- **Errors**: Common: "No response" (check connections), "Empty query" (type something). View logs for details. Let Dawson know.
- **Security**: Don't share sensitive data in queries. Auth protects sessions. You are directly tied to this, so don't do anything NSFW.
- **Customization**: Edit `app.py` for UI changes; rebuild Docker image.

## Troubleshooting

- **App Not Starting**: Check Docker logs; ensure env vars are set correctly (e.g., no "localhost" in container envs—use service names).
- **Auth Issues**: Verify Supabase is running and keys match.
- **Query Failures**: If LLM errors, check Ollama service. For ChromaDB, ensure data is ingested.
- **Updates**: Pull code changes, rebuild (`docker compose build`), restart (`docker compose up -d`).

For support, contact intern@hhmoldsinc.com or check the linked docs. This app is for internal H&H use— please report bugs promptly.
