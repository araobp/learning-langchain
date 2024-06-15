from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
#from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

chat = ChatOpenAI(model="gpt-3.5-turbo")

embedder = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./embeddings.db",
  embedding_function=embedder
)

retriever = database.as_retriever()

qa = RetrievalQA.from_llm(
  llm=chat,
  retriever=retriever,
  return_source_documents=True
)

result=qa("飛行者の最高速度を教えて")

print(result['result'])
#print(result['source_documents'])

