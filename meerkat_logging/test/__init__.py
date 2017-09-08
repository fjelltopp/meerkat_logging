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
from passlib.hash import pbkdf2_sha256
import calendar
import time
import jwt
import os

filename = os.environ.get('MEERKAT_AUTH_SETTINGS')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

# We need to authenticate our tests using the dev/testing rsa keys
token_payload = {
    u'acc': {
        u'meerkat': [u'logging'],
    },
    u'data': {u'name': u'Testy McTestface'},
    u'usr': u'testUser',
    u'exp': calendar.timegm(time.gmtime()) + 1000,  # Lasts for 1000 seconds
    u'email': u'test@test.org.uk'
}
token = jwt.encode(token_payload,
                   JWT_SECRET_KEY,
                   algorithm=JWT_ALGORITHM).decode("utf-8")

header = {'Authorization': JWT_HEADER_PREFIX + token}
header_non_authorised = {'Authorization': ''}

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
        """ Test post event"""
        db.session.query(Log).delete()
        db.session.commit()
        
        self.app.post("/event",
                          data=json.dumps({
                              "timestamp": "2017-01-01",
                              "type": "user_event",
                              "source": "test-source",
                              "source_type": "test",
                              "implementation": "null_island",
                              "event_data": {"test1": "test",
                                             "test2": "test"}
                          }),
                          content_type='application/json',
                          headers=header
        )
        records = db.session.query(Log).all()
        self.assertEqual(len(records), 1)

        
if __name__ == '__main__':
    unittest.main()
