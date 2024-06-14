from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
  model = "text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embeddings
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
