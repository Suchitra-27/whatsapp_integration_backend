from fastapi import APIRouter, Request, Header, HTTPException
import uuid
from app.utils.log_trace import log_trace
from app.utils.safe_mode import check_wallet, verify_agent_signature
from app.routes.agent import query_agent, AgentQueryRequest
from app.utils.safe_mode import NEXTEL_TOKEN
import json
from urllib.parse import parse_qs

router = APIRouter()

@router.post("/whatsapp")

async def receive_whatsapp_message(request: Request, authorization: str = Header(None)):

    # 🔐 Temporarily skip strict token check until Nextel clarifies
    # if authorization != f"Bearer {NEXTEL_TOKEN}":
    #     raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        # 🧠 Fallback decoding: support both JSON & form-urlencoded
        content_type = request.headers.get("content-type", "")
        if "application/json" in content_type:
            data = await request.json()
        else:
            raw_body = await request.body()
            decoded_body = raw_body.decode()
            parsed_form = parse_qs(decoded_body)
            if "payload" in parsed_form:
                data_str = parsed_form["payload"][0]
                data = json.loads(data_str)
            else:
                data = json.loads(decoded_body)  # fallback for badly labeled but raw JSON

        print("✅ Incoming WhatsApp Payload:", data)

        # 🔎 Extract user input
        value = data["entry"][0]["changes"][0]["value"]
        user_input = value["messages"][0]["text"]["body"]
        phone_number = value["contacts"][0]["wa_id"]
        print(f"📨 From {phone_number}: {user_input}")

        # 🔐 Wallet & Signature Checks (Mocked for now)
        agent_id = "demo-agent-1"
        if not check_wallet(agent_id):
            raise HTTPException(status_code=403, detail="Agent wallet inactive")

        if not verify_agent_signature(agent_id, user_input):
            raise HTTPException(status_code=403, detail="Invalid agent signature")

        # 🤖 Query agent (mocked)
        agent_request = AgentQueryRequest(agent_id=agent_id, user_input=user_input)
        agent_data = await query_agent(agent_request)
        reply = agent_data["response"]
        trace_id = agent_data["trace_id"]

        # 📊 Log to ClickHouse
        log_trace(
            trace_id=trace_id,
            agent_id=agent_id,
            channel="whatsapp",
            token_used=None,
            fallback_path=None,
            delivery_status="replied"
        )

        # ✅ Return response back to Nextel
        return {
            "message": {
                "type": "text",
                "message": reply
            },
            "userinfo": {
                "phone": phone_number
            }
        }

    except Exception as e:
        print("❌ Webhook Error:", e)
        return {
            "message": {
                "type": "text",
                "message": "Error occurred while processing your message."
            },
            "userinfo": {
                "phone": "unknown"
            }
        }
