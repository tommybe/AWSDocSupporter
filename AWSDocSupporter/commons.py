from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

VECTOR_DB_SUBPATH = 'vectors'
VECTOR_STORE = Chroma
EMBEDDING = OpenAIEmbeddings  # TODO - could be parametrized in the future