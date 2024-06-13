from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_spliter = SpacyTextSplitter(
  chunk_size=300,
  pipeline="ja_core_news_trf"
)

splitted_documents = text_spliter.split_documents(documents)

embeddings = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embeddings
)

database.add_documents(
  splitted_documents
)

print("Embeddings.db created")