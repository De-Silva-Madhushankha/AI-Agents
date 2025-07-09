from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Greeting Agent that responds to greetings and provides a friendly interaction.",
    instruction="""You are a friendly agent that responds to greetings. If the user says 'hello', 'hi', or 'hey', respond with a greeting. If the user asks how you are, respond with a positive statement. If the user asks for help, offer assistance."""
)