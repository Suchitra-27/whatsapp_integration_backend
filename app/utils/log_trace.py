import os
from datetime import datetime
import clickhouse_connect
from app.config.env import (
    USE_CLICKHOUSE,
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USERNAME,
    CLICKHOUSE_PASSWORD
)
print("DEBUG: USE_CLICKHOUSE =", USE_CLICKHOUSE)

def log_trace(trace_id, agent_id, channel, token_used=None, fallback_path=None, delivery_status=None):
    if not USE_CLICKHOUSE:
        print("\U0001f4dd Trace Log (local fallback):", {
            "trace_id": trace_id,
            "agent_id": agent_id,
            "channel": channel,
            "token_used": token_used,
            "fallback_path": fallback_path,
            "delivery_status": delivery_status
        })
        return

    client = clickhouse_connect.get_client(
        host=CLICKHOUSE_HOST,
        port=CLICKHOUSE_PORT,
        username=CLICKHOUSE_USERNAME,
        password=CLICKHOUSE_PASSWORD,
        secure=True
    )

    columns = [
        "trace_id",
        "agent_id",
        "channel",
        "token_used",
        "fallback_path",
        "delivery_status",
        "timestamp"
    ]

    rows = [[
        trace_id,
        agent_id,
        channel,
        token_used,
        fallback_path,
        delivery_status,
        datetime.utcnow()
    ]]

    client.insert("trace_logs", rows, column_names=columns)
    print(f"\U0001f4ca Trace logged to ClickHouse: {trace_id}")
