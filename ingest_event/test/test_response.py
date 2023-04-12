import unittest
from ..utils.response import event_ingested_correctly

class TestResponse(unittest.TestCase):
    
    def test_event_ingested_correctly(self):
        event = {"id": 1, "name": "Event 1"}
        expected_output = {
                "statusCode": 200,
                "body": '{"event_ingested": {"id": 1, "name": "Event 1"}}'
            }
        self.assertEqual(event_ingested_correctly(event), expected_output)
