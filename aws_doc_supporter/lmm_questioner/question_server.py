from flask import Flask
import click
import logging
import os
from typing import NoReturn
from threading import Thread
from aws_doc_supporter.commons import VECTOR_STORE, EMBEDDING
from aws_doc_supporter.lmm_questioner.questioner import Questioner

flask_app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

SEARCH_KWARGS = {
    "maximal_marginal_relevance": True,
    "distance_metric": "cos",
    "fetch_k": 20,
    "k": 10,
}


def run_aws_questioner(path_to_vector_db: str, flask_host: str, flask_port: int) -> NoReturn:
    vectordb = VECTOR_STORE(persist_directory=path_to_vector_db, embedding_function=EMBEDDING())
    retriever = vectordb.as_retriever(**SEARCH_KWARGS)
    del vectordb

    questioner = Questioner(retriever)

    flask_app.add_url_rule("/get_answer/<question>", "get_answer", questioner.get_answer)
    flask_app.add_url_rule("/get_document/<question>", "get_document", questioner.get_document)
    Thread(target=flask_app.run, kwargs={"host": flask_host, "port": flask_port, "debug": False}).start()


@click.command(help="Flask server responsible for answering questions about AWS documentation.")
@click.option("--open_ai_api_key", type=str, required=True, help="OpenAI API key")
@click.option("--path_to_vector_db", type=str, required=True, help="Path to directory with vector db")
@click.option("--flask_host", type=str, required=False, help="Host for questioning flask server.")
@click.option("--flask_port", type=int, required=False, help="Port for questioning flask server.")
def run(open_ai_api_key: str, path_to_vector_db: str, flask_host: str, flask_port: int) -> NoReturn:
    os.environ["OPENAI_API_KEY"] = open_ai_api_key
    run_aws_questioner(path_to_vector_db, flask_host, flask_port)


def main():
    run(auto_envvar_prefix="AWS_DOC_QUESTIONER")


if __name__ == "__main__":
    run()
