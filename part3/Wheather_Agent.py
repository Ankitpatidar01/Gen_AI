from dotenv import load_dotenv
load_dotenv()

import os
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient

# new creat tools

#wheather tools 

@tool
def get_weather(city : str) -> str:
  """Get Current weather of a city"""
  
  API_KEY = os.getenv("OPENWEATHER_API_KEY")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
 
  
  response = requests.get(url)
  data = response.json()
  
  print(data)

  
  if response.status_code != 200:
    return f"Error: {data.get('message', 'Could not fetch weather')}"
  
  temp = data["main"]["temp"]
  desc = data["weather"][0]["description"]
  
  return f"Weather in {city}: {desc} , {temp}C"


result = get_weather.invoke("Bhopal")

print(result)


#tavily new tools
  # TavilyClient(api_key=os.getenv("TAVILY_API_KEY")) 