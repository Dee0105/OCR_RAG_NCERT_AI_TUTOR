from langchain_community.llms import Ollama


def load_llm():

    llm = Ollama(
        model="gemma2:2b",
        temperature=0.3
    )

    return llm