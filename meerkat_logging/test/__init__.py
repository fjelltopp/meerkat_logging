#!/usr/bin/env python3
"""
Meerkat API Tests

Unit tests for the Meerkat API
"""
import json, os
import unittest
from datetime import datetime
from meerkat_logging.app import app, db
from meerkat_logging.model import Log

class MeerkatLoggingTestCase(unittest.TestCase):

    def setUp(self):
        """Setup for testing"""
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        """Check the index page loads"""
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Meerkat Logging', rv.data)

    def test_event(self):
        db.session.query(Log).delete()
        db.session.commit()
        self.app.post("/event", data=json.dumps({
                "timestamp": "2017-01-01",
                "type": "user_event",
                "source": "test-source",
                "source_type": "test",
                "implementation": "null_island",
                "event_data": {"test1": "test",
                               "test2": "test"}
            }),
            content_type='application/json'
        )
        records = db.session.query(Log).all()
        self.assertEqual(len(records), 1)

        
if __name__ == '__main__':
    unittest.main()
