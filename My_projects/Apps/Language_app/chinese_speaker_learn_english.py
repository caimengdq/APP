import os
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools
from keys import *

# higher temperature for higher randomness
os.environ["OPENAI_API_KEY"] = key_openai


# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)

# use loader to load full transcript as a query database


def summarise_from_episode(episode):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)
    prompt_1 = "Select 10 commonly used phrases from the show Modern Family {episode}, " \
               "provide translation in Chinese, also explain the context in Chinese"
    prompt_2 = "You are trying to help someone to improve their English level, conduct a lecture based on {episode} " \
               "of Modern Family for a beginner Chinese speaker " \
               "learning English, providing translations and explanations in Chinese "
    prompt = PromptTemplate.from_template(prompt_2)

    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(episode)


print(summarise_from_episode("Season 1 Episode 5"))
