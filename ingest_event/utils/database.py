import os 
import boto3

from .logger import logger

dynamo_db_client_params = {}

#If running on local
# if os.environ.get('IS_OFFLINE'):
#     dynamo_db_client_params = {
#         'endpoint_url': 'http://localhost:8000',
#         'aws_access_key_id': 'DEFAULT_ACCESS_KEY',
#         'aws_secret_access_key': 'DEFAULT_SECRET'
#     }

dynamodb = boto3.resource('dynamodb', **dynamo_db_client_params)
table = dynamodb.Table('event101Table')

def insert_event_in_db(event: dict) -> None:
    table.put_item(Item=event)
    logger.info(f'Event inserted in database: {event}')