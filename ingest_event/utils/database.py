import boto3

from .logger import logger

dynamo_db_client_params = {}
dynamodb = boto3.resource('dynamodb', **dynamo_db_client_params)
table = dynamodb.Table('event101Table')

def insert_event_in_db(event: dict) -> None:
    table.put_item(Item=event)
    logger.info(f'Event inserted in database: {event}')