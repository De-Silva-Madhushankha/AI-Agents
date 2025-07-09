from google.adk.agents import Agent
from google.adk.tools import google_search

### Best practice: Define custom tools for specific functionalities -> Specify return types and descriptions, return meaningful and descriptive data instead of just results

def get_current_time() -> dict:
    """Get the current time in the format YYYY-MM-DD HH:MM:SS."""
    from datetime import datetime
    now = datetime.now()
    return {
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent that can perform Google searches.",
    instruction="""You are a tool agent that can perform Google searches. If the user asks a question, use the google_search tool to find relevant information and provide a concise answer.""",
    #tools=[get_current_time],  # Custom tool to get current time
    tools=[google_search], # Can only use one built-in tool at a time
    #tools=[google_search, get_current_time], # Doesn't work with multiple tools yet
)