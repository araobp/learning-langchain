from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI(model="gpt-3.5-turbo")

retriever = WikipediaRetriever(
  lang="ja",
  doc_content_chars_max=500,
  top_k_results=2
)

query = RetrievalQA.from_llm(
  llm=chat,
  retriever=retriever,
  return_source_documents=True
)

answer = query("バーボンウィスキーとは？")

source_documents = answer["source_documents"]
result = answer["result"]

for doc in source_documents:
  print("--- 取得したメタデータ ---")
  print(doc.metadata)
  print("--- 取得したテキスト ---")
  print(doc.page_content[:100])

print("----")
print(result)
