from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home_status_code(self):
        # Context manager
        with self.app() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World'})
