from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

data = TextLoader("notes.txt")
docs = data.load()

splitter = CharacterTextSplitter(separator="" , chunk_size = 1000 , chunk_overlap=10)

chunks = splitter.split_documents(docs)

print(chunks)

for i in chunks:
  print(i)
  print()
  print()
  
# split on bases of first search \nn , \n , " " , ""