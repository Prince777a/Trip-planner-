from crewai import Agent
import google.generativeai as genai
from dotenv import load_dotenv
import os
from typing import Any, Dict, List, Optional
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.outputs import ChatGeneration, ChatResult
import time
import google.api_core.exceptions
from pydantic import PrivateAttr

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

# Load environment variables
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a custom LLM wrapper for Gemini
class GeminiLLM(BaseChatModel):
    model_name: str = "gemini-1.5-flash-8b"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        object.__setattr__(self, "_last_request_time", 0.0)

    def _generate(self, messages: List[Any], **kwargs: Any) -> Any:
        gemini_messages = []
        for message in messages:
            if isinstance(message, HumanMessage):
                gemini_messages.append({"role": "user", "parts": [message.content]})
            elif isinstance(message, AIMessage):
                gemini_messages.append({"role": "model", "parts": [message.content]})
            elif isinstance(message, SystemMessage):
                gemini_messages.append({"role": "user", "parts": [message.content]})
        model = genai.GenerativeModel(self.model_name)

        min_interval = 4.1  # seconds
        now = time.time()
        elapsed = now - getattr(self, "_last_request_time", 0.0)
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        object.__setattr__(self, "_last_request_time", time.time())

        while True:
            try:
                response = model.generate_content(gemini_messages)
                break
            except google.api_core.exceptions.ResourceExhausted as e:
                print("Quota exceeded, waiting 45 seconds before retrying...")
                time.sleep(45)
        generation = ChatGeneration(
            message=AIMessage(content=response.text),
            generation_info={"model_name": self.model_name}
        )
        return ChatResult(generations=[generation])
    
    def _llm_type(self) -> str:
        return "gemini"

# Initialize the custom LLM
llm = GeminiLLM()

class TripAgents():

  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm=llm)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm=llm)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True,
        llm=llm)
