from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "mistral-small-2506",
    model_provider="mistralai",
    temperature=0.1,
    max_tokens=100
)

response = model.invoke("Write a poem on AI ?")
print(response.content)