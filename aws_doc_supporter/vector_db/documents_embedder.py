import logging
from typing import List
from tqdm import tqdm
import os
from time import sleep
from aws_doc_supporter.commons import VECTOR_DB_SUBPATH, EMBEDDING, VECTOR_STORE, EMBEDDING_BATCH_SIZE, \
    EMBEDDING_SLEEP_TIME


class EmbeddedDocuments:
    def __init__(self, splitted_documents: List[str], path_to_md_files_dir: str):
        logging.debug(f"Initialize {type(self).__name__} class.")
        self.splitted_documents = splitted_documents
        self._prepare_directory(path_to_md_files_dir)
        self.vector_db = self._vectorizing_documents()

    def _prepare_directory(self, path_to_md_files_dir):
        self.path_to_vector_db = os.path.join(os.path.dirname(path_to_md_files_dir), VECTOR_DB_SUBPATH)
        if os.path.exists(self.path_to_vector_db):
            logging.info(f'Directory {self.path_to_vector_db} already exists.')
        else:
            os.mkdir(self.path_to_vector_db)
            logging.info(f'Directory {self.path_to_vector_db} created.')

    def _vectorizing_documents(self):
        total_length = len(self.splitted_documents)
        with tqdm(desc="Vectorizing text.", total=int(total_length/EMBEDDING_BATCH_SIZE)):
            for batch_start in range(0, total_length, EMBEDDING_BATCH_SIZE):
                batch_end = min(batch_start + EMBEDDING_BATCH_SIZE, total_length)
                batch_texts = self.splitted_documents[batch_start:batch_end]
                try:
                    vector_db = self._vectorizing_document(batch_texts)
                except:
                    logging.warning(f'Batch not loaded. Sleep for {EMBEDDING_SLEEP_TIME} seconds')
                    sleep(EMBEDDING_SLEEP_TIME)
        return vector_db

    def _vectorizing_document(self, batch_texts):
        return VECTOR_STORE.from_documents(
            batch_texts,
            embedding=EMBEDDING(),
            persist_directory=self.path_to_vector_db
        )

    def persist(self):
        self.vector_db.persist()
