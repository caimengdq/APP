import os
from langchain import OpenAI, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools
from keys import *

# higher temperature for higher randomness
os.environ["OPENAI_API_KEY"] = key_openai
llm = OpenAI(temperature=0)
prompt = PromptTemplate.from_template("Summarise some commonly used phrases from the show Modern Family {episode}, "
                                      "provide translation and explanation of context for each phrase in Chinese")

chain = LLMChain(llm=llm, prompt=prompt)

user_input = "Season 1 Episode 5"
print(chain.run(user_input))






