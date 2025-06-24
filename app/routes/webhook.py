from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/whatsapp")
async def receive_whatsapp_message(request: Request):
    try:
        data = await request.json()
        print("✅ Incoming WhatsApp Payload:", data)
        return {"status": "received"}
    except Exception as e:
        print("❌ Error parsing webhook:", e)
        return {"status": "error", "error": str(e)}
