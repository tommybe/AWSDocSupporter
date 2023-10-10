import logging
from typing import Dict

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

from langchain.text_splitter import RecursiveCharacterTextSplitter


class SplittedDocuments:
    def __init__(self, raw_documents: Dict[str, str]):
        self.raw_documents = raw_documents
        self.documents = {}
        logging.debug(f"Initialize {type(self).__name__} class.")
        self._splitting_documents()

    def _splitting_documents(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        logging.info("Splitting text.")
        self.documents = text_splitter.split_documents(list(self.raw_documents.values()))
