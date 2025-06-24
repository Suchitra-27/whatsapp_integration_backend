 
from pydantic import BaseModel
from typing import List, Optional

class TextMessage(BaseModel):
    body: str

class Message(BaseModel):
    text: TextMessage

class Contact(BaseModel):
    wa_id: str

class Value(BaseModel):
    messages: List[Message]
    contacts: List[Contact]

class Change(BaseModel):
    value: Value

class Entry(BaseModel):
    changes: List[Change]

class WhatsAppWebhookPayload(BaseModel):
    entry: List[Entry]

class WhatsAppSendPayload(BaseModel):
    phone_number: str
    message: str
