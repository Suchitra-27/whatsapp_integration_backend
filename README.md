📦 WhatsApp API Integration for Verbotix Agent Runtime

🧩 Objective
Design and deploy a secure, traceable API interface between the WhatsApp platform and the Verbotix OS. This will allow Verbotix Agents to receive user messages from WhatsApp and send AI-generated responses back via WhatsApp.

👨‍💻 Key Features

✅ Webhook Endpoint (/webhook/whatsapp)

Receives messages from WhatsApp via Nextel.

Parses nested payloads and extracts user_input and phone_number.

Calls mock Verbotix Agent API to generate replies.

Logs all traces into ClickHouse.

Returns formatted WhatsApp response to Nextel.

✅ Send Endpoint (/send/whatsapp)

Present for design completeness. Not used, as replies are embedded in webhook response per Nextel's design.

✅ Internal Agent Query (/agent/query)

Mocks a Verbotix agent response using a local function for now.

📈 ClickHouse Logging

Captures all trace data (trace_id, agent_id, channel, etc.).

🔐 Safe Mode Checks (Mocked)

Agent wallet validity

Agent signature

🔒 Token-Based Authorization

Verifies Authorization header: Bearer <NEXTEL_TOKEN>

⚖️ Fallback Payload Parser

Supports both application/json and application/x-www-form-urlencoded

🔍 Environment Variables

Set in Railway or local .env file:

NEXTEL_TOKEN=verbotix-secure-key
USE_CLICKHOUSE=true
CLICKHOUSE_HOST=your-host.clickhouse.cloud
CLICKHOUSE_PORT=443
CLICKHOUSE_USERNAME=your-user
CLICKHOUSE_PASSWORD=your-pass

📦 Installation & Local Dev

# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Install requirements
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

🔖 Endpoints

1. /webhook/whatsapp (POST)

Receives messages and returns structured replies.

2. /send/whatsapp (POST)

(Not used) Present for completeness in system design.

3. /agent/query (POST)

Mocked endpoint for Verbotix Agent response.

4. /env-debug (GET)

Debug endpoint to verify env variable loading.

🚫 Limitations

Rate-limiting code (slowapi) is commented due to Railway issues.

Agent backend and signature logic are mocked.

 
