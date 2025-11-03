from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from ..models.models import EmailInput, EmailTriageOutput
import os
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("google api key environment not found/set")

# provider = GoogleGLAProvider(api_key=api_key)

model = GeminiModel("gemini-2.5-flash", api_key=papi_key)

email_agent = (
        Agent(
        model = model,
        output_type =EmailTriageOutput,
        instructions= """
        You are an Email Triage Agent that receives an email and classifies it.

        Input:
        - sender: the email address of the sender
        - body: raw email text

        Output:
        - summary: one-sentence summary
        - category: one of [spam, inquiry, invoice, support_request, personal, other]
        - urgency: one of [low, medium, high]
        - suggested_reply_draft: a short, polite professional reply (or empty string for spam)

        Respond ONLY in JSON matching the EmailTriageOutput schema.
        """
    )
)
