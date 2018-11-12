from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        # For the lifetime of this app, we are in testing mode
        app.testing = True
        self.app = app.test_client
