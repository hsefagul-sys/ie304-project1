import streamlit as st
import google.generativeai as genai
from retriever import get_retriever

# --- Page Config ---
st.set_page_config(
    page_title="METU IE Summer Practice Assistant",
    page_icon="🎓",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .header-container {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .header-container h1 {
        color: #CC0000;
        font-size: 1.6rem;
        margin-bottom: 0.2rem;
    }
    .header-container p {
        color: #666;
        font-size: 0.95rem;
    }
    .info-box {
        background-color: #f8f9fa;
        border-left: 4px solid #CC0000;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0 1rem 0;
        border-radius: 0 4px 4px 0;
        font-size: 0.88rem;
        color: #444;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="header-container">
    <h1>🎓 METU IE Summer Practice Assistant</h1>
    <p>Ask me anything about IE 300 / IE 400 Summer Practice!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    💡 <strong>Sample questions:</strong> "What are the requirements for IE 300?", 
    "How do I apply for SGK insurance?", "Who is on the SP committee?",
    "What is the duration of IE 400 project-based internship?"
</div>
""", unsafe_allow_html=True)

# --- Sidebar for API Key ---
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    api_key = st.secrets.get("GEMINI_API_KEY", "")
    
    if not api_key:
    st.error("API key not configured. Please contact the administrator.")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown(
        "This chatbot answers questions about **METU Industrial Engineering** "
        "Summer Practice (IE 300 & IE 400) based on the official "
        "[SP website](https://sp-ie.metu.edu.tr/en)."
    )
    st.markdown("---")
    st.markdown(
        "<small>Built for IE 304 Project 1 | Spring 2025-2026</small>",
        unsafe_allow_html=True
    )

# --- Initialize ---
retriever = get_retriever()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
if prompt := st.chat_input("Ask about summer practice..."):
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar first.")
        st.stop()

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Retrieve relevant context
    results = retriever.retrieve(prompt, top_k=5)
    
    context_parts = []
    for r in results:
        context_parts.append(f"[{r['topic']}]\n{r['content']}")
    context_text = "\n\n".join(context_parts) if context_parts else "No specific information found."

    # Build prompt for Gemini
    system_prompt = f"""You are a helpful assistant for METU (Middle East Technical University) Industrial Engineering Department's Summer Practice program.

Your role is to answer student questions about IE 300 and IE 400 summer practice courses accurately based on the provided context from the official SP website (https://sp-ie.metu.edu.tr/en).

RULES:
1. Answer ONLY based on the provided context. Do not make up information.
2. If the context does not contain enough information to answer the question, say so clearly and suggest the student check the SP website or contact the SP committee at ie-staj@metu.edu.tr.
3. Be friendly, concise, and helpful.
4. If the question is not related to METU IE Summer Practice, politely inform the student that you can only help with summer practice related questions.
5. You can answer in both Turkish and English - match the language of the question.
6. When relevant, mention specific links, room numbers, or contact information.

CONTEXT FROM SP WEBSITE:
{context_text}
"""

    # Call Gemini API
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3-flash-preview")
        
        # Build conversation history for Gemini
        gemini_history = []
        for msg in st.session_state.messages[:-1]:  # exclude current message
            role = "user" if msg["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=gemini_history)
        
        full_prompt = system_prompt + "\n\nUser question: " + prompt

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat.send_message(full_prompt)
                answer = response.text
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        error_msg = str(e)
        if "API_KEY" in error_msg.upper() or "PERMISSION" in error_msg.upper():
            st.error("❌ Invalid API key. Please check your Gemini API key.")
        else:
            st.error(f"❌ Error: {error_msg}")
