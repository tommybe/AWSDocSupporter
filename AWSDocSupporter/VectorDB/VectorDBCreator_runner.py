from typing import NoReturn

import click

from DocumentsEmbedder import EmbeddedDocuments
from DocumentsLoader import RawDocuments
from DocumentsSplitter import SplittedDocuments


def run_vdb_creator(
        path_to_md_files_dir: str
) -> NoReturn:
    raw_documents = RawDocuments(path_to_md_files_dir)
    splitted_documents = SplittedDocuments(raw_documents.documents)
    embedded_documents = EmbeddedDocuments(splitted_documents.documents, path_to_md_files_dir)
    embedded_documents.persist()


@click.command(help="Script for training LLM on AWS documentation in md data")
@click.option("--path_to_md_files_dir", type=str, required=True, help="Path to directory with md files")
def run(path_to_md_files_dir: str) -> NoReturn:
    run_vdb_creator(path_to_md_files_dir)


def main():
    run(auto_envvar_prefix="AWS_DOC_SUPPORTER")


if __name__ == "__main__":
    run()
