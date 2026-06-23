from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

from pydantic import BaseModel
from typing import List , Optional
from langchain_core.output_parsers import PydanticOutputParser  # for output parser

model = ChatMistralAI(model='mistral-small-2506')


# this is schema 

class Movie(BaseModel):
  title: str
  release_year : Optional[int]
  genre: List[str]
  director: Optional[str]
  cast: List[str]
  rating: Optional[float]
  summary: str
  
parser = PydanticOutputParser(pydantic_object=Movie)
  

input_text = input("Enter the movie descirption : ")

prompt = ChatPromptTemplate.from_messages([
  ('system' , """ Extract Movie information from the paragraph {format_instruction}"""),
  ('human'  , "{input_text}")
]
)

chain = prompt | model | parser

response = chain.invoke({
    "input_text": input_text,
    "format_instruction": parser.get_format_instructions()
})

print("output : " , response)

# movie Description
# Inception is a 2010 science fiction thriller directed by Christopher Nolan. The film stars Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, and Ken Watanabe. It follows Dom Cobb, a skilled thief who specializes in stealing secrets from people's dreams. Cobb is offered a chance to have his criminal record erased if he can successfully perform an impossible task known as "inception"—planting an idea into someone's mind through a dream. The movie was released in the United States in 2010, is in English language, and is known for its complex storytelling and stunning visual effects.

# also see example with from_messages(
#   ("system" , """ """),
#   ("human" , """ """)
# )