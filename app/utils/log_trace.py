import os
from datetime import datetime
import clickhouse_connect

USE_CLICKHOUSE = os.getenv("USE_CLICKHOUSE", "false").lower() == "true"
print("DEBUG: USE_CLICKHOUSE =", os.getenv("USE_CLICKHOUSE"))


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
        host=os.getenv("CLICKHOUSE_HOST"),
        port=int(os.getenv("CLICKHOUSE_PORT", "8443")),
        username=os.getenv("CLICKHOUSE_USERNAME"),
        password=os.getenv("CLICKHOUSE_PASSWORD"),
        secure=True
    )

    # ✅ Correct format: list of rows (list of lists), column_names must match
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

    # ✅ Must include column_names parameter when sending list of lists
    client.insert("trace_logs", rows, column_names=columns)

    print(f"\U0001f4ca Trace logged to ClickHouse: {trace_id}")
