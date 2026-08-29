from dotenv import load_dotenv
load_dotenv()

from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool = TavilySearch(max_result = 5)

llm = ChatMistralAI(model="mistral-small-2506")


prompt = ChatPromptTemplate.from_template(
  """
  you are a helpful asssistant 
  summarize the following new into clear bullet points
  {news}
  """
)

chain = prompt | llm | StrOutputParser()

news_result = search_tool.run("Latest AI news of 2026")

news_output = chain.invoke({"news" : news_result})

print(news_output)

