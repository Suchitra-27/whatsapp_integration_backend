# ✅ File: app/utils/safe_mode.py

import os
from fastapi import Request

NEXTEL_TOKEN = os.getenv("NEXTEL_TOKEN")

# 🔐 Check if agent wallet is valid (mocked logic for now)
def check_wallet(agent_id: str) -> bool:
    # Example logic: only allow if agent_id starts with 'demo'
    if agent_id.startswith("demo"):
        return True
    return False

# 🔐 Validate signature sent from agent (mocked logic)
def verify_agent_signature(signature: str) -> bool:
    # Example logic: consider signature valid if length is 10
    return signature is not None and len(signature) == 10

# 🔐 Check if request has a valid Bearer token

def validate_incoming_token(request: Request) -> bool:
    token = request.headers.get("Authorization")
    return token == f"Bearer {NEXTEL_TOKEN}"