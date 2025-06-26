import os
from dotenv import load_dotenv

# Load only if .env exists locally (not in production)
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

USE_CLICKHOUSE = os.getenv("USE_CLICKHOUSE", "false").lower() == "true"
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT")
CLICKHOUSE_USERNAME = os.getenv("CLICKHOUSE_USERNAME")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")
