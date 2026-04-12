# METU IE Summer Practice Chatbot

A chatbot that answers questions about METU Industrial Engineering Summer Practice (IE 300 / IE 400) for IE 304 – Project 1 (Spring 2025-2026).

## Architecture

```
User Question
     |
     v
+--------------+
|  Streamlit   |  <- Web UI (chat interface)
|  Frontend    |
+------+-------+
       |
       v
+--------------+
|  Retriever   |  <- TF-IDF based similarity search
|  (RAG)       |     finds relevant knowledge chunks
+------+-------+
       |
       v
+--------------+
|  Gemini API  |  <- Generates answer using retrieved context
|  (LLM)       |
+--------------+
```

- **Knowledge Base**: Information chunks extracted from https://sp-ie.metu.edu.tr/en, for the pages on 
- **Retrieval**: TF-IDF cosine similarity (no external vector DB needed)
- **Generation**: Google Gemini (free tier)
- **Frontend**: Streamlit chat interface

## Running Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a Gemini API Key
- Go to https://aistudio.google.com
- Click "Get API Key" then "Create API key"
- Copy the key

### 3. Run the app
```bash
streamlit run app.py
```

## Deploying to Streamlit Cloud

1. Push this project to a GitHub repository
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your repo, branch, and `app.py` as the main file
5. Add your Gemini API key under Settings > Secrets as `GEMINI_API_KEY = "your-key"`
6. Click "Deploy"

## Project Structure

```
app.py              - Main Streamlit application
knowledge_base.py   - Knowledge chunks from SP website
retriever.py        - TF-IDF based RAG retrieval
requirements.txt    - Python dependencies
.streamlit/
  config.toml       - Streamlit theme config
README.md           - This file
```

## Sample Test Queries

- "What are the prerequisites for IE 300?" - Should list prerequisite courses
- "How do I apply for SGK insurance?" - Should explain the OCW application steps
- "Who is on the SP committee?" - Should list members with contact info
- "How long is IE 400 project-based internship?" - Should say minimum 30 workdays (6 weeks)
- "How is the IE 300 report graded?" - Should give the 200-point breakdown

## How It Works

1. User types a question in the chat box
2. The retriever tokenizes the query and computes TF-IDF similarity against knowledge chunks
3. Top 5 relevant chunks are selected as context
4. A prompt is built with context + user question + system instructions
5. The prompt is sent to Gemini API
6. Response is shown in the chat
7. Conversation history is kept for follow-up questions
