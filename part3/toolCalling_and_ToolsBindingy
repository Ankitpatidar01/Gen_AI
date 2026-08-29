from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool

from rich import print # This is used to get ouput in structured way

#Creating a tool

@tool
def get_text_length(text : str) -> int:
  """ Return the number of character in a given text"""
  
  return len(text)

# llm model
model = ChatMistralAI(model= "mistral-small-2506")

# Tool binding
model_with_tool = model.bind_tools([get_text_length]) # above model is without tool but now here this model contain a tool name get_text_length

# we cannot bind tools to all the llm there are some model which support tools binding 

# tools which do not support tools calling or binding 
# DeepSeek-R1 / deepseek-reasoner
# Perplexity chat models via ChatPerplexity

result = model.invoke("Hello")

#print(result) # this will give simple ouput ,  usage_metadata={'input_tokens': 16, 'output_tokens': 13, 'total_tokens': 29}
# Here this 

result_with_model_with_tool = model_with_tool.invoke("Hello") # usage_metadata={'input_tokens': 79, 'output_tokens': 13, 'total_tokens': 92}
# here the input token is more because of tool binding because LangChain has to send the tool's definition to the LLM along with your "Hello" message.



#print(result_with_model_with_tool)

#------------------Tools calling----------------------#

result_without_tool = model.invoke("Return the number of character in a given text : 'Hello !")

print(result_without_tool)

result_with_tool = model_with_tool.invoke("Return the number of character in a given text : 'Hello !")
# by this llm only choose tool which can be used
print(result_with_tool) # so here we get nothing 

if result_with_tool.tool_calls:
  tool_call = result_with_tool.tool_calls[0]
  
  tool_name = tool_call['name']
  tool_args = tool_call['args']

  tool_result = get_text_length.invoke(tool_args)

  final_result = model.invoke(f"the Length of text is {tool_result}")

  print(final_result)

# human message 
# ai message
# tool message 
