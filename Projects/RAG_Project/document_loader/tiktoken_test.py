from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("RAG_Exam_Overview_Notes.pdf")

docs = data.load()

splitter = TokenTextSplitter(chunk_size = 500 , chunk_overlap = 50)

chunks = splitter.split_documents(docs)

print(len(chunks))

for chnk in chunks:
  print(chnk.page_content)
  print()
  print()
  print()

