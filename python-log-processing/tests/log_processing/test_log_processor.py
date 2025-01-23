import unittest
import pandas as pd

from app.log_processing.log_processor import not_null, validate_log_entries, flatten_fields, \
    calculate_events_per_event_type, calculate_most_active_user


class TestLogProcessor(unittest.TestCase):
    def test_not_null(self):
        self.assertEqual(not_null("user_id", None), "user_id has None value")
        self.assertEqual(not_null("metadata", None), None)
        self.assertEqual(not_null("user_id", "valid_id"), None)

    def test_validate_log_entries(self):
        logs = [
            {'user_id': None, 'timestamp': '2023-10-01T12:00:00Z', 'event_type': 'login'},
            {'user_id': '1234', 'timestamp': None, 'event_type': 'logout'},
            {'user_id': '5678', 'timestamp': '2023-10-01T12:05:00Z', 'event_type': None},
            {'user_id': '91011', 'timestamp': '2023-10-01T12:10:00Z', 'event_type': 'purchase'}
        ]
        expected_validations = {
            0: 'user_id has None value',
            1: 'timestamp has None value',
            2: 'event_type has None value'
        }
        self.assertDictEqual(validate_log_entries(logs), expected_validations)

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
        actual_output = flatten_fields(logs)
        self.assertCountEqual(actual_output, expected_output)

    def test_calculate_events_per_event_type(self):
        logs = [
            {'user_id': 'U123', 'timestamp': '2025-01-10T10:00:00Z', 'event_type': 'view'},
            {'user_id': 'U124', 'timestamp': '2025-01-10T10:05:00Z', 'event_type': 'click'},
            {'user_id': 'U125', 'timestamp': '2025-01-10T10:10:00Z', 'event_type': 'view'},
            {'user_id': 'U126', 'timestamp': '2025-01-10T10:15:00Z', 'event_type': 'purchase'},
            {'user_id': 'U127', 'timestamp': '2025-01-10T10:20:00Z', 'event_type': 'click'},
            {'user_id': 'U128', 'timestamp': '2025-01-10T10:25:00Z', 'event_type': 'view'}
        ]
        expected_output = pd.DataFrame({
            'event_type': ['click', 'purchase', 'view'],
            'count': [2, 1, 3]}).to_dict(orient="records")
        actual_output = calculate_events_per_event_type(logs).to_dict(orient="records")
        self.assertEqual(expected_output, actual_output)

    def test_calculate_most_active_user(self):
        logs = [
            {'user_id': 'U123', 'timestamp': '2025-01-10T10:00:00Z', 'event_type': 'view'},
            {'user_id': 'U124', 'timestamp': '2025-01-10T10:05:00Z', 'event_type': 'click'},
            {'user_id': 'U125', 'timestamp': '2025-01-10T10:10:00Z', 'event_type': 'view'},
            {'user_id': 'U126', 'timestamp': '2025-01-10T10:15:00Z', 'event_type': 'purchase'},
            {'user_id': 'U127', 'timestamp': '2025-01-10T10:20:00Z', 'event_type': 'click'},
            {'user_id': 'U128', 'timestamp': '2025-01-10T10:25:00Z', 'event_type': 'view'},
            {'user_id': 'U123', 'timestamp': '2025-01-10T10:30:00Z', 'event_type': 'click'},
            {'user_id': 'U123', 'timestamp': '2025-01-10T10:35:00Z', 'event_type': 'purchase'}
        ]
        expected_output = 'U123'
        actual_output = calculate_most_active_user(logs)['user_id'].iloc[0]
        self.assertEqual(expected_output, actual_output)

