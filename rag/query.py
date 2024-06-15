from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
  model = "text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embeddings
)

QUERY = "飛行者に許される最高の高度は？"

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
