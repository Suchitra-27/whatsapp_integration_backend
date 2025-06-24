# import os
# import requests

# NEXTEL_API_URL = os.getenv("NEXTEL_API_URL")
# NEXTEL_TOKEN = os.getenv("NEXTEL_TOKEN")

# def send_whatsapp_message(phone_number: str, message: str):
#     if not NEXTEL_API_URL or not NEXTEL_TOKEN:
#         return {"error": "Nextel credentials not configured"}

#     headers = {
#         "Authorization": f"Bearer {NEXTEL_TOKEN}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "to": phone_number,
#         "type": "text",
#         "text": {
#             "body": message
#         }
#     }

#     try:
#         response = requests.post(NEXTEL_API_URL, json=payload, headers=headers, timeout=10)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         print("Send WhatsApp Error:", e)
#         return {"error": str(e)}


import os
import requests

NEXTEL_API_URL = os.getenv("NEXTEL_API_URL")
NEXTEL_TOKEN = os.getenv("NEXTEL_TOKEN")

def send_whatsapp_message(phone_number: str, message: str):
    if not NEXTEL_API_URL or not NEXTEL_TOKEN:
        print("[MOCK] Sending WhatsApp message to:", phone_number)
        print("[MOCK] Message:", message)
        return {
            "status": "mocked",
            "message": message,
            "to": phone_number,
            "delivery_status": "mock_success"
        }

    headers = {
        "Authorization": f"Bearer {NEXTEL_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }

    try:
        response = requests.post(NEXTEL_API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Send WhatsApp Error:", e)
        return {"error": str(e)}
