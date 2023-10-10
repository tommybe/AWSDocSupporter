import logging

from aws_doc_supporter.commons import LLM
from langchain.schema.vectorstore import VectorStoreRetriever
from langchain.chains import RetrievalQA

TEMPERATURE =0.7

class Questioner:
    def __init__(self, retriever: VectorStoreRetriever):
        self.qa_retriever = RetrievalQA.from_llm(
            llm=LLM(temperature=TEMPERATURE),
            retriever=retriever
            # return_source_documents=True
        )

    def ask_simple_question(self, question: str):
        logging.info(f'Question: {question}')
        query_result = self.qa_retriever.run({'query': question})
        logging.info(f'Answer: {query_result}')
        return query_result