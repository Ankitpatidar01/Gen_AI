from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(
        page_content="""
        Python is a high-level programming language known for its simple
        syntax and readability. It is widely used for web development,
        data science, machine learning, automation, and artificial intelligence.
        Python supports object-oriented, functional, and procedural programming.
        """,
        metadata={"source": "python.txt", "topic": "Python"}
    ),

    Document(
        page_content="""
        Machine learning is a branch of artificial intelligence that allows
        computers to learn patterns from data. Common machine learning
        techniques include supervised learning, unsupervised learning,
        and reinforcement learning. Python is commonly used for machine
        learning with libraries such as scikit-learn, TensorFlow, and PyTorch.
        """,
        metadata={"source": "machine_learning.txt", "topic": "Machine Learning"}
    ),

    Document(
        page_content="""
        Vector databases are designed to store and search numerical vectors.
        In a RAG application, documents are converted into embeddings and
        stored in a vector database. When a user asks a question, the question
        is also converted into an embedding, and the vector database retrieves
        documents with similar semantic meaning.
        """,
        metadata={"source": "vector_database.txt", "topic": "Vector Database"}
    )
]

embedding_model = MistralAIEmbeddings()

vectorStore = Chroma.from_documents(
  documents=docs, # document which need to be stored
  embedding=embedding_model, # embedding used before storing
  persist_directory=r"D:\GenAI_Code\Projects\RAG_Project\vector_store\chroma-db" # local storage
)

result = vectorStore.similarity_search("What is ML")


for r in result:
  print(r)



print("Vector store created successfully!")