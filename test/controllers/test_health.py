import unittest
import json

from env.infra import app


class TestHealthController(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_doc_response(self):
        response = self.client.get('/')
        data = str(response.data)
        status_code = response.status_code

        self.assertTrue("swaggerui" in data)
        self.assertTrue(status_code == 200)

    def test_health_response(self):
        response = self.client.get('/api/v1/health')
        data = json.loads(response.data)
        status_code = response.status_code

        self.assertTrue(data['status'] == 'ok')
        self.assertTrue(status_code == 200)
