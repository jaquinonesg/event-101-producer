import json

from .utils.logger import logger
from .utils.database import insert_event_in_db
from .utils.event_bus import sent_event_to_bus
from .utils.metadata import add_metadata


def ingest_event(event: dict, context: dict) -> dict:
    logger.info(f'Received event: {event}')
    # Check if the event is in the expected format
    
    if not isinstance(event, dict) or 'body' not in event:
        error_msg = f'Event is not in expected format: {event}'
        logger.error(error_msg)

        return {
            "statusCode": 400,
            "body": json.dumps({"message": error_msg})
        }
    
    filled_event = add_metadata(event['body'])
    insert_event_in_db(filled_event)
    sent_event_to_bus(filled_event)

    return {
        "statusCode": 200,
        "body": json.dumps({"updated_event": filled_event})
    }