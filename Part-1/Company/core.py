from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

model = ChatMistralAI(model='mistral-small-2506')

input_text = input("Enter the movie descirption : ")

prompt = PromptTemplate.from_template("""
You are an expert movie information extraction system.

Extract only information explicitly mentioned in the text.

Return ONLY valid JSON.

Text:
{input_text}

Output Format:
{{
    "title": null,
    "genre": null,
    "director": null,
    "cast": [],
    "release_year": null,
    "language": null,
    "country": null,
    "plot_summary": null
}}
""")

chain = prompt | model

response = chain.invoke({
    "input_text": input_text
})

print("output : " , response.content)

# movie Description
# Inception is a 2010 science fiction thriller directed by Christopher Nolan. The film stars Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, and Ken Watanabe. It follows Dom Cobb, a skilled thief who specializes in stealing secrets from people's dreams. Cobb is offered a chance to have his criminal record erased if he can successfully perform an impossible task known as "inception"—planting an idea into someone's mind through a dream. The movie was released in the United States in 2010, is in English language, and is known for its complex storytelling and stunning visual effects.

# also see example with from_messages(
#   ("system" , """ """),
#   ("human" , """ """)
# )