import logging
from typing import List
from AWSDocSupporter.commons import VECTOR_DB_SUBPATH, EMBEDDING, VECTOR_STORE


class EmbeddedDocuments:
    def __init__(self, splitted_documents: List[str], path_to_md_files_dir: str):
        self.splitted_documents = splitted_documents
        self.path_to_md_files_dir = path_to_md_files_dir
        self.vector_db = VECTOR_STORE
        logging.debug(f"Initialize {type(self).__name__} class.")

    def _vectorizing_documents(self):
        logging.info("Vectorizing text.")
        self.vector_db = VECTOR_STORE.from_documents(
            self.splitted_documents,
            embedding=EMBEDDING(),
            persist_directory=VECTOR_DB_SUBPATH
        )

    def persist(self):
        self.vector_db.persist()
