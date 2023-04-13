import json
import uuid
import datetime

def add_metadata(event_body: str) -> dict:
    event = json.loads(event_body)

    now = datetime.datetime.now()
    metadata = {
        "received_time": now.strftime("%Y-%m-%d %H:%M:%S")
    }

    event["pk"] = str(uuid.uuid4())
    event["metadata"] = metadata

    return event
