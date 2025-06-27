from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.routes import webhook, send, agent
from app.config.env import USE_CLICKHOUSE, CLICKHOUSE_HOST


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
app.include_router(agent.router, prefix="/agent")

# Root route
@app.get("/")
def read_root():
    return {"status": "Verbotix WhatsApp API is running"}

@app.get("/env-debug")
def env_debug():
    return {
        "USE_CLICKHOUSE": USE_CLICKHOUSE,
        "CLICKHOUSE_HOST": CLICKHOUSE_HOST
    }

