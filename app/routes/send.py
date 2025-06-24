from fastapi import APIRouter
from app.schemas.models import WhatsAppSendPayload
from app.services.whatsapp_client import send_whatsapp_message

router = APIRouter()

@router.post("/whatsapp")
def send_whatsapp(payload: WhatsAppSendPayload):
    response = send_whatsapp_message(phone_number=payload.phone_number, message=payload.message)
    return {"status": "sent", "response": response}
