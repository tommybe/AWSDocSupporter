from typing import NoReturn

import click

from documents_embedder import EmbeddedDocuments
from documents_loader import RawDocuments
from documents_splitter import SplittedDocuments
import os
import logging

logging.basicConfig(level=logging.INFO)


def run_vdb_creator(path_to_md_files_dir: str) -> NoReturn:
    raw_documents = RawDocuments(path_to_md_files_dir)
    splitted_documents = SplittedDocuments(raw_documents.documents)
    del raw_documents
    embedded_documents = EmbeddedDocuments(splitted_documents.documents, path_to_md_files_dir)
    embedded_documents.persist()


@click.command(help="Script for training LLM on AWS documentation in md data")
@click.option("--path_to_md_files_dir", type=str, required=True, help="Path to directory with md files")
@click.option("--open_ai_api_key", type=str, required=True, help="Your API key for OpenAI")
def run(path_to_md_files_dir: str, open_ai_api_key: str) -> NoReturn:
    os.environ["OPENAI_API_KEY"] = open_ai_api_key
    run_vdb_creator(path_to_md_files_dir)


def main():
    run(auto_envvar_prefix="AWS_DOC_SUPPORTER")


if __name__ == "__main__":
    run()
