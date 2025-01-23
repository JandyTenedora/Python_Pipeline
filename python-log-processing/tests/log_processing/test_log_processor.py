import unittest

from app.log_processing.log_processor import not_null, validate_log_entries, flatten_fields


class TestLogProcessor(unittest.TestCase):
    def test_not_null(self):
        pass

    def test_validate_log_entries(self):
        logs = [
            {'user_id': None, 'timestamp': '2023-10-01T12:00:00Z', 'event_type': 'login'},
            {'user_id': '1234', 'timestamp': None, 'event_type': 'logout'},
            {'user_id': '5678', 'timestamp': '2023-10-01T12:05:00Z', 'event_type': None},
            {'user_id': '91011', 'timestamp': '2023-10-01T12:10:00Z', 'event_type': 'purchase'}
        ]
        expected_validations = {
            0: 'user_id has value None',
            1: 'timestamp has value None',
            2: 'event_type has value None'
        }
        pass

    def test_flatten_fields(self):
        logs = [
            {
                "user_id": "U123",
                "timestamp": "2025-01-10T10:00:00Z",
                "event_type": "view",
                "metadata": {
                    "product_id": "P456",
                    "device": "mobile",
                    "category": "electronics"
                }
            },
            {
                "user_id": "U124",
                "timestamp": "2025-01-10T10:05:00Z",
                "event_type": "click",
                "metadata": {
                    "product_id": "P789",
                    "device": "desktop",
                    "category": "books"
                }
            }
        ]
        expected_output = [
            {
                'user_id': 'U123',
                'timestamp': '2025-01-10T10:00:00Z',
                'event_type': 'view',
                'metadata.product_id': 'P456',
                'metadata.device': 'mobile',
                'metadata.category': 'electronics'
            },
            {
                'user_id': 'U124',
                'timestamp': '2025-01-10T10:05:00Z',
                'event_type': 'click',
                'metadata.product_id': 'P789',
                'metadata.device': 'desktop',
                'metadata.category': 'books'
            }
        ]
        pass
