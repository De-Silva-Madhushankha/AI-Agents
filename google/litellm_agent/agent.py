import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="openrouter/openai/gpt-3.5-turbo",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def get_dad_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    return random.choice(jokes)

root_agent = Agent(
    name="litellm_agent",
    model=model,
    description="A LiteLLM agent that provides dad jokes and friendly interactions.",
    instruction="""You are a friendly agent that tells dad jokes. If the user asks for a joke, respond with a dad joke. If the user asks how you are, respond with a positive statement. If the user asks for help, offer assistance.""",
    tools=[get_dad_joke],
)

