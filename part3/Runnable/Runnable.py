from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # to represent output in structure way 

from langchain_core.runnables import RunnableParallel , RunnableLambda


# model = ChatMistralAI(model="mistral-small-2506")
# parser = StrOutputParser()
# prompt = ChatPromptTemplate.from_template("Explain {topic} in simple word")



# formated_prompt = prompt.format_messages(topic="Machine Learning")

# output = model.invoke(formated_prompt)

# structured_output = parser.parse(output.content)

# print(structured_output)


### ----------------------WITH CHAIN------------------------

# LMMChain(prompt , model , parser)


## Though chain are not actually perfect all the time due to many reason so we move toward runnable

##------------------------------------ Runnable_Sequence
# chain = prompt | model | parser
# output = chain.invoke({"topic": "Machine Learning"})

# print(output)

##-------------------------------Parallel_runnable

# if we want two different type of explanation of two different topic then
# lets take one as short explanation 

model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

short_prompt = ChatPromptTemplate.from_template("Explain {topic} in short")

# another as detailed explanation

detailed_prompt = ChatPromptTemplate.from_template("Explain {topic} in detail.")

# create multiple pipline 

# short_pipline = short_prompt | model | parser
# detailed_pipline = detailed_prompt | model | parser

# now we have to store then in dictionary to run in paraller

# chain = {"short" : short_pipline , "detailed" : detailed_pipline}

# now though this is dictionary to call invoke we have to comvert it into runnable

# chain = RunnableParallel({"short" : short_pipline , "detailed" : detailed_pipline})

# output = chain.invoke({"topic" : "Machine Learning"})



short_pipline = RunnableLambda(lambda x : x['short']) | short_prompt | model | parser
detailed_pipline = RunnableLambda(lambda x : x['detailed']) | detailed_prompt | model | parser

chain = RunnableParallel({"short" : short_pipline , "detailed" : detailed_pipline})

output = chain.invoke({"short" : {"topic" : "Machine Learning"},
                       "detailed" : {"topic" : "Deep Learning"}})

print(output["short"])
print()
print()
print(output["detailed"])
