from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


# Output Schema for the email content
class EmailContent(BaseModel):
    subject: str = Field(..., description="The subject of the email. should be consize and descriptive.")
    body: str = Field(..., description="The body content of the email.should be well-formatted with proper greetings, paragraphs and signature.")

root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction=""" You are an Email generation Assistant.
    Your task is to generate a professional email based on the provided content.
    GUIDELINES:
    - The email should have a clear subject line that summarizes the content.
    - The body of the email should be well-structured, with a proper greeting, main content, appropriate closing and your name as closing signature.
    - Suggest relevant attachments if necessary.
    - Email tone should match the purpose of the email, whether it's formal, informal, or business-related.
    - Keep emails concise and to the point, avoiding unnecessary jargon or overly complex language.

    IMPORTANT: your response MUST be valid JSON matching this structure:
    {
        "subject": "The subject of the email. should be consize and descriptive.",
        "body": "The body content of the email.should be well-formatted with proper greetings, paragraphs and signature."
    }

    DO NOT include any additional text or explanations outside of the JSON structure.
    """,
    description="Email generation agent that creates professional emails based on provided content.",
    output_schema=EmailContent, 
    output_key="email",
)