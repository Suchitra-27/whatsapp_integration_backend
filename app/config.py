import os
from dotenv import load_dotenv

# ✅ Only load .env locally
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

# ✅ Always fetch from os.environ
USE_CLICKHOUSE = os.getenv("USE_CLICKHOUSE", "false").lower() == "true"
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 8443))
CLICKHOUSE_USERNAME = os.getenv("CLICKHOUSE_USERNAME")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")
