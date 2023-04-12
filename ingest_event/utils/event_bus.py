import boto3
import json

from .logger import logger


event_bus = boto3.client('events')

def sent_event_to_bus(event: dict) -> None:
    response = event_bus.put_events(
        Entries=[
            {
                'Source': 'event101',
                'DetailType': 'event101_type',
                'Detail': json.dumps(event),
                'EventBusName': 'CentralBroker'
            },
        ]
    )
    logger.info(f'Event sent to event bus: {response}')