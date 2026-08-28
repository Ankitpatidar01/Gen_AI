from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma


load_dotenv()

data = PyPDFLoader("document_loader/RAG_Exam_Overview_Notes.pdf") # path of file

docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000  ,  chunk_overlap = 200)

chunks = splitter.split_documents(docs)

embedding_model = MistralAIEmbeddings()

vectorStore = Chroma.from_documents(
  documents=chunks, # chunks which need to be stored
  embedding=embedding_model, # embedding used before storing
  persist_directory=r"D:\GenAI_Code\Projects\RAG_Project\vector_store\chroma-db-1" # local storage , if not mentioned then it will store vector embedding in RAM
)
