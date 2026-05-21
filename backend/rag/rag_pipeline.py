from backend.rag.retriever import retrieve_docs
from backend.llm.llm_engine import load_llm

from backend.ocr.vision import extract_text_from_image


llm = load_llm()

chat_history = []


def ask_question(
    query,
    selected_class=None,
    selected_subject=None
):

    docs = retrieve_docs(
        query=query,
        selected_class=selected_class,
        selected_subject=selected_subject
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    history = "\n".join(chat_history[-6:])

    prompt = f"""
You are an intelligent NCERT tutor AI.

Rules:
1. Answer ONLY from NCERT context.
2. Keep answers simple and educational.
3. Explain step-by-step when needed.
4. If answer is unavailable, say:
   "I could not find the answer in NCERT."
5. Avoid hallucinations.

Conversation History:
{history}

NCERT Context:
{context}

Student Question:
{query}

AI Tutor Answer:
"""

    response = llm.invoke(prompt)

    chat_history.append(f"User: {query}")
    chat_history.append(f"AI: {response}")

    return response


def ask_image_question(
    image_path,
    selected_class=None,
    selected_subject=None
):

    extracted_text = extract_text_from_image(
        image_path
    )

    response = ask_question(
        query=extracted_text,
        selected_class=selected_class,
        selected_subject=selected_subject
    )

    return response