import os

USE_CLICKHOUSE = os.environ.get("USE_CLICKHOUSE", "false").lower() == "true"
CLICKHOUSE_HOST = os.environ.get("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = int(os.environ.get("CLICKHOUSE_PORT", 8443))
CLICKHOUSE_USERNAME = os.environ.get("CLICKHOUSE_USERNAME")
CLICKHOUSE_PASSWORD = os.environ.get("CLICKHOUSE_PASSWORD")
