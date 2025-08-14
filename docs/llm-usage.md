# H&H AI Assistant Usage Documentation

## Introduction

**NOTE**: you *MUST* be on either H&H Secure or the H&H Quality Wifi networks

The H&H AI Assistant is a web-based application built with Streamlit and Pydantic, designed to assist with injection molding queries. It supports multiple modes for handling different types of questions:

- **RAG Mode**: Previously known as "general mode". Uses Retrieval-Augmented Generation (RAG) to query and summarize documents, including listing documents, fetching file contents, and running SQL queries on tabular data.
- **Websearch Mode**: Performs web searches, crawls pages, and summarizes content relevant to the query.
- **Logging Mode**: Allows setup techs to log changes to various parts and presses. Setup techs can then query the data using natrual language.

---

## Help 

To get help for modes you can enter one of these queries into the general mode:
  - `general-mode.md`
  - `websearch-mode.md`
  - `what-can-you-do.md`
  

Entering any of these into the chat (RAG mode) will make the model output contents it has saved regarding those services.

Definitions and detailed usage are included here.

---

## Accessing the Application

1. **Open in Browser**:

  - Go to [LLM Website](http://10.0.0.76:8501) 
  - The page title is "H&H AI Assistant" with a robot icon (🤖).
  - If the app doesn't load, tell Dawson or whoever is in chareg of the app and check Docker logs for errors (e.g., connection issues to Supabase, chroma, or Ollama).

2. **Troubleshooting Access**:

  - Network: Make sure you are either connected to H&H Secure, or H&H Quality Wifi networks (or hardwired in to ethernet).
  - Browser Cache: Clear cache or try incognito mode if UI issues occur.
  - OOM: If you get an out of memory error, let Dawson or whoever is in charge of the app know. You likely have too much stored memory in a chat, and need it cleared out. 
  - Gary, see the troubleshooting section of the docs to resolve an error like this.

---

## Signup and Login

The app uses Supabase for authentication (enabled when `DEPLOY = True` in `app.py`). Anonymous access is not supported in production mode.

### Signup

1. On the login screen (displayed if not authenticated), select "Sign Up" from the "Action" dropdown.
2. Enter a valid email address (e.g., `user@example.com`). Don't worry you will never recieve spam or emails, this is just for user authentication. You can use work email or personal.
3. Enter a password (at least 6 characters; Supabase enforces basic rules).
4. Click "Register".
5. If successful, you'll see "Registered! Log in." 

### Login

1. On the login screen, select "Login" from the "Action" dropdown (default).
2. Enter your registered email and password.
3. Click "Login".
4. If successful, you'll see "Welcome back, [email]!" and be redirected to the main app interface.

### Logout

1. In the sidebar, click "Logout".
2. You'll be redirected to the login screen, and session data is cleared.

---

## Using the Application

Once logged in, the interface consists of a sidebar for controls and a main chat area for interactions.

### Sidebar Controls

- **Header**: "H&H AI Assistant" with logo and logged-in email.
- **Mode Selector**: Choose the query mode (dropdown: "general", "press_data", "websearch").

### Main Chat Interface

- **Title**: "H&H AI Assistant" with a brief description: "Assist with injection molding: queries on Press20, docs, calculations, trends, defect fixes."
- **Chat History**: Displays previous messages.
- **Input Field**: At the bottom—"Your question..." placeholder. Type your query and press Enter.

---

## Troubleshooting

- **App Not Starting**: Check Docker logs; ensure env vars are set correctly.
- **Auth Issues**: Verify Supabase is running and keys match.
- **Query Failures**: If LLM errors, check Ollama service. For ChromaDB, ensure data is ingested.

For support, contact intern@hhmoldsinc.com or check the linked docs. This app is for internal H&H use— please report bugs promptly.
