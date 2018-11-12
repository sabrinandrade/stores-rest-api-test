"""
Base Test

This test should be the parent test to every non-unit test.
It allows dynamic database instantiation and guarantees that
we have a new, blank database every time.

"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # Defines the database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            # Mocks the entire app
            db.init_app(app)
            db.create_all()
        # Gets a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Destroys database
        with app.app_context():
            db.session.remove()
            db.drop_all()
