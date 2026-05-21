import time
import os
import streamlit as st

from backend.rag.rag_pipeline import (
    ask_question,
    ask_image_question
)


st.set_page_config(
    page_title="NCERT AI Tutor",
    layout="wide"
)


st.title("📘 NCERT AI Doubt Solver")

st.markdown(
    """
Ask doubts from NCERT textbooks using:
- Text questions
- Uploaded images
- AI-powered explanations
"""
)


# SIDEBAR
st.sidebar.title("⚙️ Filters")


selected_class = st.sidebar.selectbox(
    "Select Class",
    [
        None,
        "class5",
        "class6",
        "class7",
        "class8",
        "class9",
        "class10"
    ]
)


selected_subject = st.sidebar.selectbox(
    "Select Subject",
    [
        None,
        "maths",
        "science"
    ]
)
if st.sidebar.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()

st.sidebar.markdown("---")

st.sidebar.info(
    """
This AI tutor uses:
- RAG
- FAISS
- Ollama
- Gemma2
- Moondream OCR
"""
)
uploaded_image = st.file_uploader(
    "Upload doubt image",
    type=["png", "jpg", "jpeg"]
)
if uploaded_image:

    try:

        image_path = os.path.join(
            "uploads",
            uploaded_image.name
        )

        with open(image_path, "wb") as f:
            f.write(uploaded_image.read())

        st.image(uploaded_image)

        with st.spinner("Analyzing image..."):

            response = ask_image_question(
                image_path=image_path,
                selected_class=selected_class,
                selected_subject=selected_subject
            )

        with st.chat_message("assistant"):
            st.markdown(response)

    except Exception as e:

        st.error(f"OCR Error: {str(e)}")
# CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = []


# DISPLAY OLD MESSAGES
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# USER INPUT
query = st.chat_input(
    "Ask your NCERT doubt..."
)


if query:

    # SHOW USER MESSAGE
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    # GET AI RESPONSE
    try:

     with st.spinner("Thinking..."):

        response = ask_question(
            query=query,
            selected_class=selected_class,
            selected_subject=selected_subject
        )

    except Exception as e:

        response = f"Error: {str(e)}"
    # SHOW AI RESPONSE
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
st.markdown("---")

st.caption(
    "Built using Streamlit + LangChain + FAISS + Ollama"
)