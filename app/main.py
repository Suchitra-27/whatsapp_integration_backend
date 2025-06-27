from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.routes import webhook, send, agent
from app.config.env import USE_CLICKHOUSE, CLICKHOUSE_HOST
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Load environment variables from .env
load_dotenv()

limiter = Limiter(key_func=get_remote_address)

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

# ✅ Register rate limit exception handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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

