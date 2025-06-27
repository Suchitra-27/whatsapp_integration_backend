# ✅ File: app/routes/agent.py

from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class AgentQueryRequest(BaseModel):
    agent_id: str
    user_input: str

@router.post("/agent/query")
async def query_agent(payload: AgentQueryRequest):
    return {
        "response": f"Mocked Verbotix AI: You said '{payload.user_input}'",
        "trace_id": str(uuid4()),
        "fallback_path": None,
        "agent_signature": "1234567890"
    }
