#!/usr/bin/env python3
"""
Meerkat API Tests

Unit tests for the Meerkat API
"""
import unittest
from meerkat_logging.app import app
from meerkat_logging import send_log
from unittest import mock


class MeerkatLoggingSendingTestCase(unittest.TestCase):

    def setUp(self):
        """Setup for testing"""
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @mock.patch('meerkat_logging.requests')
    def test_send_log(self, mock_requests):
        """Check the index page loads"""
        send_log("http://test",
                 "user_event",
                 "test-source",
                 "test",
                 "null_island",
                 {"test1": "test",
                  "test2": "test"},
                 timestamp="2017-01-01")

        mock_requests.post.assert_called_with(
            "http://test/event",
            data={
                "timestamp": "2017-01-01",
                "type": "user_event",
                "source": "test-source",
                "source_type": "test",
                "implementation": "null_island",
                "event_data": {"test1": "test",
                               "test2": "test"}
            }
        )
if __name__ == '__main__':
    unittest.main()
