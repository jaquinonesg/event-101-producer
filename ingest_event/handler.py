import json
import os
import boto3
import uuid
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

dynamo_db_client_params = {}

if os.environ.get('IS_OFFLINE'):
    dynamo_db_client_params = {
        'endpoint_url': 'http://localhost:8000',
        'aws_access_key_id': 'DEFAULT_ACCESS_KEY',
        'aws_secret_access_key': 'DEFAULT_SECRET'
    }

dynamodb = boto3.resource('dynamodb', **dynamo_db_client_params)
event_bus = boto3.client('events')
table = dynamodb.Table('event101Table')


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


def insert_event_in_db(event: dict) -> None:
    table.put_item(Item=event)
    logger.info(f'Event inserted in database: {event}')


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


def sent_event_to_bus(event: dict) -> None:
    response = event_bus.put_events(
        Entries=[
            {
                'Source': 'event101',
                'DetailType': 'my-event-type',
                'Detail': json.dumps(event),
            },
        ]
    )
    logger.info(f'Event sent to event bus: {response}')
