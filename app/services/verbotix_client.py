import os
import uuid
import requests

# Load Verbotix agent query URL from .env
AGENT_URL = os.getenv("AGENT_QUERY_URL")

# def call_verbotix_agent(agent_id: str, user_input: str, channel="whatsapp") -> dict:
#     trace_id = f"TRACE_{uuid.uuid4()}"

#     payload = {
#         "agent_id": agent_id,
#         "channel": channel,
#         "user_input": user_input,
#         "trace_id": trace_id
#     }

#     if AGENT_URL:
#         try:
#             response = requests.post(AGENT_URL, json=payload, timeout=10)
#             response.raise_for_status()
#             data = response.json()
#             data["trace_id"] = trace_id
#             return data
#         except Exception as e:
#             print(f"[Agent Error] {e}")
#             return {
#                 "message": "Agent error. Please try again later.",
#                 "agent_signature": None,
#                 "fallback_path": "error",
#                 "trace_id": trace_id
#             }
#     else:
#         # If AGENT_QUERY_URL is not set, use a mock
#         print("[Mock Agent] Agent URL not found, using dummy response.")
#         return {
#             "message": f"(Mock) Reply to: {user_input}",
#             "agent_signature": "mock_signature_123",
#             "fallback_path": None,
#             "trace_id": trace_id
#         }

def call_verbotix_agent(agent_id: str, user_input: str):
    # Mock agent response
    trace_id = str(uuid.uuid4())
    return {
        "trace_id": trace_id,
        "message": f"🤖 Verbotix (mock): You said '{user_input}'",
        "fallback_path": None
    }
