from flask_testing import TestCase
from flask import url_for
import json

from ..app import app
import os
basedir = os.path.abspath(os.path.dirname(__file__))



class TestBase(TestCase):
    def create_app(self):
        return app

    def test_access_index(self):

        settings = {'block_size': 100}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        settings = json.dumps(settings)
        response = self.client.get(url_for('stream', epic='EURUSD'), json=settings, headers=headers)
        self.assertEqual(response.status_code, 200)
