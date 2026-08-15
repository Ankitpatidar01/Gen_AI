# So the document can be present in txt file , in pdf , From website

# so we use langchain document loader 
#  we select type of document loader according to out requirement 


from langchain_community.document_loaders import TextLoader

data = TextLoader("notes.txt") # path of file 

print(data) # it will give an object

docs = data.load()

# print(docs) # it is a list of documents which contain metadata and page_content
# [() , () , ()] here contain 3 documents 

print(docs[0])
