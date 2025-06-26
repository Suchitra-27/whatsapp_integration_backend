from fastapi import APIRouter, Request
import uuid
from app.utils.log_trace import log_trace

router = APIRouter()

@router.post("/whatsapp")
async def receive_whatsapp_message(request: Request):
    try:
        data = await request.json()
        print("✅ Incoming WhatsApp Payload:", data)

        value = data["entry"][0]["changes"][0]["value"]
        user_input = value["messages"][0]["text"]["body"]
        phone_number = value["contacts"][0]["wa_id"]

        print(f"📨 From {phone_number}: {user_input}")

        # Mocked response from agent
        trace_id = str(uuid.uuid4())
        reply = f"🤖 Verbotix AI (mock): You said '{user_input}'"

        # ✅ Log to ClickHouse
        log_trace(
            trace_id=trace_id,
            agent_id="demo-agent-1",
            channel="whatsapp",
            token_used=None,
            fallback_path=None,
            delivery_status="replied"
        )

        # ✅ Respond to Nextel with WhatsApp reply structure
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
