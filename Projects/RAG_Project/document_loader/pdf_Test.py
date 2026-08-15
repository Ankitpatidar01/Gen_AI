
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("RAG_Exam_Overview_Notes.pdf")

docs = data.load()

print(len(docs)) # now this contain 7 document and each document contain (metadata , page-content)
# each page is converted in document 

print(docs[0].page_content)

# now because this pdf can content 100 pages and sending 100 document to our llm model will exceed its context window limit and so we will now study and deep dive in concept called Chunking

