from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_user_crud(self):
        with self.app_context():
            user = UserModel('test', 'password')

            self.assertIsNone(UserModel.find_by_username('test'),
                              f"Expected not to find the object in the database.")
            self.assertIsNone(UserModel.find_by_id(1),
                              f"Expected not to find the object in the database.")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'),
                                 f"Expected to find the object in the database, but did not.")
            self.assertIsNotNone(UserModel.find_by_id(1),
                             f"Expected to find the object in the database, but did not.")

            # user.remove_from_db()

            # self.assertIsNone(UserModel.find_by_username('test'),
            #                   f"Expected not to find the object in the database.")
            # self.assertIsNone(UserModel.find_by_id(1),
            #                   f"Expected not to find the object in the database.")
