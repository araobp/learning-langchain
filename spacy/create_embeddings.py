from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import SpacyTextSplitter
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_spliter = SpacyTextSplitter(
  chunk_size=300,
  pipeline="ja_core_news_lg"
)

splitted_documents = text_spliter.split_documents(documents)

embedder = SpacyEmbeddings(model_name="ja_core_news_lg")

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embedder
)

database.add_documents(
  splitted_documents
)

print("Embeddings.db created")