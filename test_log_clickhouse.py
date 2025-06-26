import os
from dotenv import load_dotenv

# Force load .env manually
load_dotenv(dotenv_path=".env")

# TEMP: override value to make sure logging works
os.environ["USE_CLICKHOUSE"] = "true"

# Debug print
print("DEBUG: USE_CLICKHOUSE =", os.getenv("USE_CLICKHOUSE"))
print("DEBUG: HOST =", os.getenv("CLICKHOUSE_HOST"))

# Run log_trace
from app.utils.log_trace import log_trace
import uuid

trace_id = str(uuid.uuid4())

log_trace(
    trace_id=trace_id,
    agent_id="demo-agent-1",
    channel="whatsapp",
    token_used="test-token",
    fallback_path="fallback-reply",
    delivery_status="delivered"
)
