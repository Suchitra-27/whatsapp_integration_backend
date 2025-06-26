import os
from dotenv import load_dotenv

# Railway automatically provides env vars at runtime
RAILWAY_ENV = os.getenv("RAILWAY_ENVIRONMENT")

# Load .env file only when running locally (i.e., not on Railway)
if RAILWAY_ENV is None:
    print("📦 Loading from .env (local mode)")
    load_dotenv()
else:
    print("🚀 Using Railway runtime environment")

USE_CLICKHOUSE = os.getenv("USE_CLICKHOUSE", "false").lower() == "true"
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT")
CLICKHOUSE_USERNAME = os.getenv("CLICKHOUSE_USERNAME")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")