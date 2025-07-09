from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent that can perform Google searches.",
    instruction="""You are a tool agent that can perform Google searches. If the user asks a question, use the google_search tool to find relevant information and provide a concise answer.""",
    tools=[google_search],
)