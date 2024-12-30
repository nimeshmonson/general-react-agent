from dotenv import load_dotenv
import os

from open_ai_client import OpenAIClient
from user_personas import UserPersona
from tavily_search_client import TavilySearchClient
from general_agent import GeneralAgent

load_dotenv()

open_ai_client = OpenAIClient(os.getenv("OPENAI_API_KEY"))

professor_persona_description="""
    You are a 57 year old college professor who teaches at Harvard University. You have been experiencing severe abdomen pain and is coming to see a doctor. 
    You have appendicitis, but don't state that. Only answer the questions that are being asked with your symptoms. Let the doctor come up with the diagnosis
"""
agent_system_prompt="""
    You are a disease diagnostic agent. You have a patient that has come to see you.
    Please use the tools that are available to you to diagnose the patient and prescribe them some medications to use. 
    You can search the internet to gather more information you need. Do not come to conclusions just based on the answers the user has given you.
    Ask follow up questions to get more information and double check with the information on the internet.
"""

professor_persona = UserPersona(description=professor_persona_description, client = open_ai_client)
tavily_search_client = TavilySearchClient(os.getenv("TAVILY_API_KEY"))

main_agent = GeneralAgent(
    system_prompt=agent_system_prompt,
    client = open_ai_client,
    interviewee = professor_persona,
    search_engine = tavily_search_client
)



print(main_agent.run())