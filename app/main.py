from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routes import webhook, send

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Verbotix WhatsApp Integration",
    version="1.0.0"
)

# CORS middleware (optional for testing from web tools)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(webhook.router, prefix="/webhook")
app.include_router(send.router, prefix="/send")

# Root route
@app.get("/")
def read_root():
    return {"status": "Verbotix WhatsApp API is running"}
