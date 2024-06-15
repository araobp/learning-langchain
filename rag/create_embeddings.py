from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import SpacyTextSplitter

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_spliter = SpacyTextSplitter(
  chunk_size=300,
  pipeline="ja_core_news_lg"
)

splitted_documents = text_spliter.split_documents(documents)

embedder = OpenAIEmbeddings(model="text-embedding-ada-002")

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embedder
)

database.add_documents(
  splitted_documents
)

print("Embeddings.db created")