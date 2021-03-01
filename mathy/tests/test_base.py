from flask_testing import TestCase
from flask import url_for
import json

from mathy.app import *
import os
basedir = os.path.abspath(os.path.dirname(__file__))


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    print(script_dir)
    rel_path = "stream_json"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, 'r') as json_data:
        d = json.loads(json_data.read())
        json_data.close()

    return MockResponse(d, 200)


class TestBase(TestCase):
    def create_app(self):
        return app

    def test_access_math(self):

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        print(script_dir)
        rel_path = "stream_json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, 'r') as json_data:
            d = json.loads(json_data.read())
            json_data.close()

        response = self.client.get(url_for('average'), json=d)
        self.assertEqual(response.status_code, 200)
