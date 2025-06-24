import os
import json
import datetime
from uuid import uuid4

USE_CLICKHOUSE = os.getenv("USE_CLICKHOUSE", "false").lower() == "true"

# Optional: install client only if ClickHouse is used
if USE_CLICKHOUSE:
    from clickhouse_driver import Client

    CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
    CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB", "verbotix")
    CLICKHOUSE_TABLE = os.getenv("CLICKHOUSE_TABLE", "trace_logs")

    client = Client(host=CLICKHOUSE_HOST, database=CLICKHOUSE_DB)

def log_trace(trace_id, agent_id, channel, token_used=None, fallback_path=None):
    timestamp = datetime.datetime.utcnow().isoformat()

    if USE_CLICKHOUSE:
        try:
            client.execute(f"""
                INSERT INTO {CLICKHOUSE_TABLE} (timestamp, trace_id, agent_id, channel, token_used, fallback_path)
                VALUES (%(timestamp)s, %(trace_id)s, %(agent_id)s, %(channel)s, %(token_used)s, %(fallback_path)s)
            """, {
                "timestamp": timestamp,
                "trace_id": trace_id,
                "agent_id": agent_id,
                "channel": channel,
                "token_used": token_used,
                "fallback_path": fallback_path
            })
        except Exception as e:
            print("ClickHouse Logging Error:", e)

    else:
        # Local fallback logging
        log_data = {
            "timestamp": timestamp,
            "trace_id": trace_id,
            "agent_id": agent_id,
            "channel": channel,
            "token_used": token_used,
            "fallback_path": fallback_path
        }
        log_path = "trace_logs.jsonl"
        with open(log_path, "a") as f:
            f.write(json.dumps(log_data) + "\n")
