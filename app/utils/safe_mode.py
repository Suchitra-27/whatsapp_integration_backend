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
def verify_agent_signature(agent_id: str, user_input: str) -> bool:
    return user_input is not None and len(user_input) > 0  # or any mock logic


# 🔐 Check if request has a valid Bearer token

def validate_incoming_token(request: Request) -> bool:
    token = request.headers.get("Authorization")
    return token == f"Bearer {NEXTEL_TOKEN}"