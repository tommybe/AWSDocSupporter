from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI

VECTOR_DB_SUBPATH = 'vectors'
EMBEDDING_BATCH_SIZE = 200
EMBEDDING_SLEEP_TIME = 10
LLM_TEMPERATURE =0.7

# TODO - could be parametrized in the future
VECTOR_STORE = Chroma
EMBEDDING = OpenAIEmbeddings
LLM = OpenAI
