# load this enviroment file i.e to use api_key

from dotenv import load_dotenv
load_dotenv()

# after this we can use any of api from .env file

from langchain.chat_models import init_chat_model

# Take model with less pricing or use case

#--------------------Gen-Ai----------------------
model = init_chat_model(
      "gemini-2.5-flash",
    model_provider="google_genai"
)

response = model.invoke("What is AI ?")
# In this way we can ask question

#print(response.content)


#--------------------------------------------------------


#------------------Gorq-----------------------------


modelGroq = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct" , model_provider="groq")
# print(model)

# it will print its input and output capacity and also will specify what else it can do 

response = modelGroq.invoke("Give me an image of computer ?")
# In this way we can ask question

#print(response.content)

#----------------------------------------------


#-----------------Mistral-----------------------

modelMistral = init_chat_model("mistral-small-2506" , model_provider="mistralai")

response = modelMistral.invoke("what is solar System ?")

print(response.content)

#--------------------------------------------------