import logging

from aws_doc_supporter.commons import LLM, LLM_TEMPERATURE
from langchain.schema.vectorstore import VectorStoreRetriever
from langchain.chains import RetrievalQA


class Questioner:
    def __init__(self, retriever: VectorStoreRetriever):
        self.retriever = retriever
        self.llm = LLM(temperature=LLM_TEMPERATURE)

    def get_answer(self, question: str):
        qa_retriever = RetrievalQA.from_llm(
            llm=self.llm,
            retriever=self.retriever
        )
        logging.info(f'Question: {question}')
        answer = qa_retriever.run({'query': question})
        logging.info(f'Answer: {answer}')
        return answer

    def get_document(self, question: str):
        qa_retriever = RetrievalQA.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=True
        )
        logging.info(f'Question: {question}')
        source_documents = qa_retriever({'query': question})["source_documents"]
        logging.info(f'Document in which you can find answer: {source_documents}')
        #TODO - create better output formatting
        return source_documents

    def get_similar_documents(self):
        print('#TODO')
        #TODO - write this function
