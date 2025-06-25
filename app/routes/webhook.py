from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/whatsapp")
async def receive_whatsapp_message(request: Request):
    try:
        # Log raw body
        raw = await request.body()
        print("📦 Raw Body:", raw.decode())

        # Parse JSON
        data = await request.json()
        print("✅ Incoming WhatsApp Payload:", data)

        # ✅ TEMP: Just return what keys are in the payload
        return {
            "status": "received",
            "keys": list(data.keys())
        }

    except Exception as e:
        print("❌ Webhook Error:", e)
        return {"status": "error", "error": str(e)}

