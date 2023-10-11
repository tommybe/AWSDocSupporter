from langchain.chains import ConversationalRetrievalChain
from langchain.schema.vectorstore import VectorStoreRetriever

from aws_doc_supporter.commons import LLM, LLM_TEMPERATURE


class Chatter:
    def __init__(self, retriever: VectorStoreRetriever):
        self.qa_retriever = ConversationalRetrievalChain.from_llm(
            llm=LLM(temperature=LLM_TEMPERATURE),
            retriever=retriever,
            return_source_documents=True
        )

    def chat(self, question: str):
        print('#TODO')
        # TODO - write loop to communicate with LLM with chat history
