from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'password')

        self.assertIsNotNone(user)
        self.assertEqual('test', user.username,
                         f"Expected user to have username 'test', but received {user.username} instead.")
        self.assertEqual('password', user.password,
                         f"Expected user to have password 'password', but received {user.password} instead.")
