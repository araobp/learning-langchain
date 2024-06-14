
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
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

doc_string = ""

for doc in documents:
  doc_string += f"""
---------------------
{doc.page_content}
"""
  
prompt = PromptTemplate(
  template="""文章を元に質問に答えてください。

文章:
{document}

質問: {query}
""",
input_variables=["document", "query"]
)

chat = ChatOpenAI(
  model="gpt-3.5-turbo"
)

content=prompt.format(document=doc_string, query=QUERY)

result = chat([
  HumanMessage(content=content)
])

print('--- Query')

print(content)

print('--- Result')

print(result.content)
