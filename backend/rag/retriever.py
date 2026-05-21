from langchain_community.vectorstores import FAISS

from backend.rag.embeddings import load_embeddings


FAISS_PATH = "faiss_index"


embeddings = load_embeddings()


vectorstore = FAISS.load_local(
    FAISS_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)


def retrieve_docs(
    query,
    k=5,
    selected_class=None,
    selected_subject=None
):

    docs = vectorstore.similarity_search(
        query=query,
        k=k
    )

    filtered_docs = []

    for doc in docs:

        class_match = (
            selected_class is None
            or doc.metadata.get("class") == selected_class
        )

        subject_match = (
            selected_subject is None
            or doc.metadata.get("subject") == selected_subject
        )

        if class_match and subject_match:
            filtered_docs.append(doc)

    return filtered_docs