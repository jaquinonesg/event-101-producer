import json
import uuid
import datetime

from .logger import logger

def add_metadata(event_body: str) -> dict:
    event = json.loads(event_body)
    # Check if the event is in the expected format
    if not isinstance(event, dict) or 'data' not in event:
        error_msg = f'Event is not in expected format: {event_body}'
        logger.error(error_msg)
        raise ValueError(error_msg)

    now = datetime.datetime.now()
    metadata = {
        "received_time": now.strftime("%Y-%m-%d %H:%M:%S")
    }

    event["pk"] = str(uuid.uuid4())
    event["metadata"] = metadata

    return event
