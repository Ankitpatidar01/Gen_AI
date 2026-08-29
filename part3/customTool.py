from langchain.tools import tool

@tool # decorator for creating tool , This function now become tool now , Decorator is just kind of wrapper
def greeting(name : str) -> str:
  """ Generate a greeting message for a user""" #doc string 
  return f"Hello {name} here !!"
  
if __name__ == "__main__":
  result = greeting.invoke({"name" : "Ankit"}) # Though it is runnable now so we have to invoke this. 
  print(result)
  
  # how to know name , description and its args
  
  print(greeting.name)
  print(greeting.description) # this will be shown as output here """ Generate a greeting message for a user"""
  print(greeting.args)
  
