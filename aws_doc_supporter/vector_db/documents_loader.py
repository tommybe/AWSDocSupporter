import logging
import os
from tqdm import tqdm

from langchain.document_loaders import UnstructuredMarkdownLoader


class RawDocuments:
    def __init__(self, path_to_md_files_dir: str):
        self.path_to_md_files_dir = path_to_md_files_dir
        self.documents = {}
        logging.debug(f"Initialize {type(self).__name__} class.")
        self._loading_documents()

    def _loading_documents(self):
        all_files = os.listdir(self.path_to_md_files_dir)
        with tqdm(desc=f"Loading documents from {self.path_to_md_files_dir} directory.", total=len(all_files)):
            for filename in all_files:
                filepath = os.path.join(self.path_to_md_files_dir, filename)
                loader = UnstructuredMarkdownLoader(filepath)
                self.documents[filename] = loader.load()[0]
                del loader
