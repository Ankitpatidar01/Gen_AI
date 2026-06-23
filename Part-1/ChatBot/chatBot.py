from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-latest" , model_provider="mistralai" , temperature=0.9 , max_tokens= 100)

question = "Hello , Ankit Tell me how can i guide you ? "

print(question)

while True:
    question = input("Enter something (or 'exit'): ")

    if question.lower() == "exit":
        break
      
    response = model.invoke(question)

    print(response.content)
  
  
  #===============ChatBot With Memory==============
  
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-latest" , model_provider="mistralai" , temperature=0.9 , max_tokens= 100)

message = []  # memory with list or can use dictionary as question as key and response as value

question = "Hello , Ankit Tell me how can i guide you ? "

print(question)

while True:
    question = input("Enter something (or 'exit'): ")

    if question.lower() == "exit":
        break
    
    message.append(question)
      
    response = model.invoke(message)
    
    message.append(response.content)
    
    # so next time it will send this whole message list and  so llm model can know each time what we have chatted previously

    print(response.content)
  
  

# in this way 
# Problems With Your Current Short-Term Memory
# .No role separation (no system / user / assistant distinction)
# Just raw strings -> weak conversation structure
# Memory keeps growing infinitely
# Will hit token limit
# API cost increases over time
# Slower response as history grows
# No trimming mechanism
# No summarization of old chats
# Not production scalable
# No control over context window


#============chatBot with three types of roles======

from dotenv import load_dotenv
load_dotenv()

from langchain.messages import AIMessage , SystemMessage , HumanMessage

from langchain.chat_models import init_chat_model
model = init_chat_model("mistral-small-latest" , model_provider="mistralai" , temperature=0.9 , max_tokens= 100)

message = []  # memory with list or can use dictionary as question as key and response as value

question = "Hello , Ankit Tell me how can i guide you ? "

message.append(SystemMessage(content="You are a funny AI Agent")) # to change model response behaviour

print(question)

while True:
    question = input("Enter something (or 'exit'): ")

    if question.lower() == "exit":
        break
    
    message.append(HumanMessage(content=question))
      
    response = model.invoke(message)
    
    message.append(AIMessage(content=response.content))
    
    # so next time it will send this whole message list and  so llm model can know each time what we have chatted previously

    print(response.content)
  