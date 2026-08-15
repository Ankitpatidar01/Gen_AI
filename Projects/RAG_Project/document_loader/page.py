from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/shop/buy-mac/macbook-air/13-inch-midnight-m5-chip-10-core-cpu-8-core-gpu-16gb-memory-512gb-storage"

data = WebBaseLoader(url)

docs = data.load()

print(len(docs)) # single page from website

print(docs[0].page_content)

