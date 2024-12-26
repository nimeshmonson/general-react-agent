from dotenv import load_dotenv
import os

from open_ai_client import OpenAIClient
from user_personas import UserPersona

load_dotenv()

open_ai_client = OpenAIClient(os.getenv("OPENAI_API_KEY"))

professor_persona = UserPersona(description="You are a 56 year old college professor who teaches at Stanford University. You have PHD in Astrophysics and has a taste for finer things in life")


answer = professor_persona.ask_question(question="tell me about your profession", client=open_ai_client)