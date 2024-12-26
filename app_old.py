# source: https://www.youtube.com/watch?v=eZSpBLYG-Mk

# first step: import libraies
from PIL import Image
from io import BytesIO
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from constants import SYSTEM_PROMPT, INSTRUCTIONS
import os
from dotenv import load_dotenv

# second steps setup API keys
load_dotenv()

OPENAI_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENAI_API_KEY = os.getenv('TAVILY_API_KEY')
MAX_IMAGE_WIDTH=300


# third step: define the Agent object
agent=Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[TavilyTools()],
    markdown=True,
    system_prompt=SYSTEM_PROMPT,
    instructions=INSTRUCTIONS,
)

# fourth step: getting image list
# first approch image path
agent.print_response(
    "Analyze the product image",
    images=["images/bournvita.jpg"],
    stream=True
)

# second approch url
agent.print_response(
    "Analyze the product image",
    images=["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8QsXCIMygo9Ni3WMGFmmEn4fUntHjcDhOVA&s"],
    stream=True
)