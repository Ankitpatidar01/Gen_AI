from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import MistralAIEmbeddings

embedding = MistralAIEmbeddings(
    model="mistral-embed"
)



# query -> Singhowle sentence
vector = embedding.embed_query(
    "Hello, Myself Ankit Patidar"
)

texts=[
"Hello this is Akarsh Vyas",
"Hello your name is YouTube",
"And you all are very beautiful"
]

# Document -> multiple sentence
vector = embedding.embed_documents(
    texts
)


print(f"Dimension: {len(vector)}")
print(vector[:10])  # first 10 values

