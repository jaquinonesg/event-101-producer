import json
from .logger import logger

def error_in_event_format(event: dict) -> dict:
    error_msg = f'Event is not in expected format: {event}'
    logger.error(error_msg)
    return {
        "statusCode": 400,
        "body": json.dumps({"message": error_msg})
    }

def event_ingested_correctly(event: dict) -> dict:
    return {
        "statusCode": 200,
        "body": json.dumps({"event_ingested": event})
    }