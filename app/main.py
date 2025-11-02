from fastapi import FastAPI
from .routes import a2a_router

app = FastAPI(
    title="Email Triage A2A Agent",
    version="1.0.0",
    description="An AI agent that classifies, summarizes, and drafts replies for incoming emails using the A2A protocol."
)

app.include_router(a2a_router.router)