# from dotenv import load_dotenv
# import os

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-7B-Instruct",
#     huggingfacehub_api_token=os.getenv("HF_TOKEN"),
# )

# chat = ChatHuggingFace(llm=llm)

# response = chat.invoke("What is AI?")

# print(response.content)


#------------------locally----------------

from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
  model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",
  pipeline_kwargs= dict(
    max_new_tokens=512,
    do_sample=False, 
    repetition_penalty=1.03,
  )
    
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is the distance between earth and sun ?")

print(response.content)

