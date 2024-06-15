from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.vectorstores import Chroma

embedder = SpacyEmbeddings(model_name="ja_core_news_lg")

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embedder
)

QUERY = "飛行者の最高速度は？"

documents = database.similarity_search(QUERY)

print('--- QUERY')
print(QUERY)

print('')
print('--- ANSWER')
for doc in documents:
  print('- metadata')
  print(doc.metadata)
  print('- page_content')
  print(doc.page_content)
