from .utils.logger import logger
from .utils.database import insert_event_in_db
from .utils.event_bus import sent_event_to_bus
from .utils.metadata import add_metadata
from .utils.response import (error_in_event_format, event_ingested_correctly)


def ingest_event(event: dict, context: dict) -> dict:
    logger.info(f'Received event: {event}')
    # Check if the event is in the expected format
    
    if not isinstance(event, dict) or 'body' not in event:
        return error_in_event_format(event)
    
    filled_event = add_metadata(event['body'])
    insert_event_in_db(filled_event)
    sent_event_to_bus(filled_event)

    return event_ingested_correctly(filled_event)