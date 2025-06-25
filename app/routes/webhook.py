from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/whatsapp")
async def receive_whatsapp_message(request: Request):
    try:
        data = await request.json()
        print("✅ Incoming WhatsApp Payload:", data)

        # Extract user message & phone number
        user_input = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        phone_number = data["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]

        print(f"📨 From {phone_number}: {user_input}")

        # Mocked agent reply
        # agent_response = call_verbotix_agent(agent_id="demo", user_input=user_input)
        #     return {
        #         "message": agent_response["message"]
        #     }
        
        reply_message = f"🤖 This is a bot reply to: '{user_input}'"

        # ✅ Return response in Nextel expected format
        return {
            "message": {
                "type": "text",
                "message": reply_message
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
                "message": "❌ Error processing message"
            },
            "userinfo": {
                "phone": "unknown"
            }
        }
