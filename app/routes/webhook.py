from fastapi import APIRouter
from app.schemas.models import WhatsAppWebhookPayload
from app.services.verbotix_client import call_verbotix_agent
from app.utils.log_trace import log_trace 
from app.utils.safe_mode import check_wallet, verify_agent_signature
from app.services.whatsapp_client import send_whatsapp_message  # use this to send reply


router = APIRouter()

@router.post("/whatsapp")
async def receive_whatsapp_message(payload: WhatsAppWebhookPayload):
    try:
        entry = payload.entry[0]
        change = entry.changes[0]
        value = change.value
        
        user_input = value.messages[0].text.body
        phone_number = value.contacts[0].wa_id

        print(f"Received from {phone_number}: {user_input}")

        agent_id = "demo-agent-id"

        # Step 1: Call the Verbotix Agent
        agent_response = call_verbotix_agent(agent_id=agent_id, user_input=user_input)

        # Step 2: Log the trace
        log_trace(
            trace_id=agent_response["trace_id"],
            agent_id=agent_id,
            channel="whatsapp",
            token_used=None,
            fallback_path=agent_response.get("fallback_path")
        )

        return {
            "status": "processed",
            "phone_number": phone_number,
            "user_input": user_input,
            "agent_response": agent_response
        }

    except Exception as e:
        print("Webhook Error:", e)
        return {"status": "error", "error": str(e)}
