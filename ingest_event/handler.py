from .utils.logger import logger
from .utils.metadata import add_metadata
from .utils.database import insert_event_in_db
from .utils.event_bus import sent_event_to_bus
from .utils.response import (
    error_in_event_format, event_ingested_correctly
    )


def ingest_event(event: dict, context: dict) -> dict:
    '''
    Insert an event with the expected JSON schema into database
    and send it to the central event bus.

        Parameters:
            event (dict)
            context (dict)

        Returns:
            response (dict): Returns the event proccesed
    '''
    logger.info(f'Received event: {event}')
    
    if not isinstance(event, dict) or 'body' not in event:
        return error_in_event_format(event)

    filled_event = add_metadata(event['body'])
    insert_event_in_db(filled_event)
    sent_event_to_bus(filled_event)

    return event_ingested_correctly(filled_event)