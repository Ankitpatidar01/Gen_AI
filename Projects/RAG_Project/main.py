from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma

load_dotenv()

llm = ChatMistralAI(model = "mistral-small-2506")
embedding_model = MistralAIEmbeddings()

vectorstore = Chroma(
  persist_directory="vector_store\chroma-db-1",
  embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
  search_type = "mmr",
  search_kwargs={
    "k" : 4, # give top 4 result
    "fetch_k" : 10, # fetch initially 10 result by similarity search and then get top 4 result
    "lambda_mult" : 0.5 # defined diversity 0 -> less diverse , 1 -> high diversity , middle value is given to staballize diversity
  }
)


prompt = ChatPromptTemplate.from_messages(
  [("system" , """You are an helpful AI Assistant. Use only the provided context to answer the question. If the answer is not present in the context, say: "I could not find the answer in the document."
    """),
  ("human" , 
   """Context: {context} Question: {question} """)]
)

print("Rag system Created...")

print("press 0 to exit...")

while True:
  print()
  query = input("you : ")
  if query == "0":
    break
  
  docs = retriever.invoke(query)
  
  context = "\n\n".join(
    [doc.page_content for doc in docs]
  )
  
  final_prompt = prompt.invoke({
    "context" : context,
    "question" : query
  })
  
  response = llm.invoke(final_prompt)
  
  print(f"\n AI : {response.content}")


# two more things missing that is runnable , memory 