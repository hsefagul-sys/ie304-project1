# METU IE Summer Practice Chatbot 🎓

An intelligent chatbot that answers questions about METU Industrial Engineering Summer Practice (IE 300 / IE 400).

Built for **IE 304 – Project 1** (Spring 2025-2026).

## 🏗️ Architecture

```
User Question
     │
     ▼
┌──────────────┐
│  Streamlit   │  ← Web UI (chat interface)
│  Frontend    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Retriever   │  ← TF-IDF based similarity search
│  (RAG)       │     finds relevant knowledge chunks
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Gemini API  │  ← Generates answer using retrieved context
│  (LLM)       │
└──────────────┘
```

- **Knowledge Base**: Curated chunks from https://sp-ie.metu.edu.tr/en
- **Retrieval**: TF-IDF cosine similarity (no external vector DB needed)
- **Generation**: Google Gemini 2.0 Flash (free tier)
- **Frontend**: Streamlit with chat interface

## 🚀 Quick Start (Local)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a Gemini API Key
- Go to https://aistudio.google.com
- Click "Get API Key" → "Create API key"
- Copy the key

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Enter your API key in the sidebar and start chatting!

## ☁️ Deploy to Streamlit Cloud

1. Push this project to a GitHub repository
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your repo, branch, and `app.py` as the main file
5. Click "Deploy"

Users will enter their own Gemini API key in the sidebar.

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── knowledge_base.py   # Curated knowledge chunks from SP website
├── retriever.py        # TF-IDF based RAG retrieval
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml     # Streamlit theme configuration
└── README.md           # This file
```

## 🧪 Sample Test Queries

1. **"What are the requirements for IE 300?"** → Should explain IE 300 summer practice basics
2. **"How do I apply for SGK insurance?"** → Should detail OCW application process
3. **"Who is on the SP committee?"** → Should list committee members with contact info
4. **"How long is IE 400 project-based internship?"** → Should say minimum 30 workdays (6 weeks)
5. **"Can I do my summer practice abroad?"** → Should mention Erasmus and abroad options

## 🔧 How It Works

1. User types a question in the chat interface
2. The **Retriever** tokenizes the query and computes TF-IDF similarity against all knowledge chunks
3. Top 5 most relevant chunks are selected as context
4. A prompt is constructed with the context + user question + system instructions
5. The prompt is sent to **Gemini 2.0 Flash** API
6. The response is displayed in the chat interface
7. Conversation history is maintained for follow-up questions
