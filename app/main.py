from fastapi import FastAPI
from .routes import a2a_router
import os

app = FastAPI(
    title="Email Triage A2A Agent",
    version="1.0.0",
    description="An AI agent that classifies, summarizes, and drafts replies for incoming emails using the A2A protocol."
)

well_known_path = os.path.join(os.path.dirname(__file__), ".well-known")
if os.path.exists(well_known_path):
    app.mount("/.well-known", StaticFiles(directory=well_known_path), name="well-known")

app.include_router(a2a_router.router)