from pydantic import BaseModel, Field
from enum import Enum


class EmailInput(BaseModel):
    """ The request model for the API endpoint """
    sender: str = Field(..., description="The email address of the sender.")
    body: str = Field(..., description="The raw text content of the email")


class EmailCategory(str, Enum):
    """ Enum for classifying the email's intent."""
    SPAM = "spam"
    INQUIRY = "inquiry"
    INVOICE = "invoice"
    SUPPORT_REQUEST = "support-request"
    PERSONAL = "personal"
    OTHER = "other"

class Urgency_level(str, Enum):
    """ Enum for the email's urgency"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class EmailTriageOutput(BaseModel):
    """ The structured output model that pydantic ai will force the LLM to generate """
    summary : str = Field(description="A concise one-sentence summary of the email's content.")
    category: EmailCategory = Field(description="The primary category of the email.")
    urgency: Urgency_level = Field(description="The urgency level for a reply")
    suggested_draft: str = Field(
        description=(
            "A brife, professional reply draft."
            "if no reply is needed (e.g, spam), this should be an empty string"
        )
    )


# --- A2A STRTUCTURES ----
class A2ARequest(BaseModel):
    """ A2A request format """
    input: EmailInput
    context: dict = {}
    meta: dict = {}

class A2AResponse(BaseModel):
    """ A2A response format"""
    output: EmailTriageOutput
    usage: dict = {}
    status: str = "success"

