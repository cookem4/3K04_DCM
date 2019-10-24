import os
import unittest

from ..UserService import UserService, UserBuilder, User


class UserServiceTest(unittest.TestCase):
    test_file = "test_repo.txt"
    test_username = "test_name"
    test_pass = "test_pass"
    sut: UserService = UserService(testing_file=test_file)

    test_user: User = UserBuilder.from_user_pass(test_username, test_pass)

    def setUpClass() -> None:
        with open(UserServiceTest.test_file, 'a'):
            os.utime(UserServiceTest.test_file, None)

    def tearDownClass() -> None:
        os.remove(UserServiceTest.test_file)

    def test_create_creates_user(self) -> None:
        self.sut.create(self.test_user)
        user: User = self.sut.read(self.test_username)
        self.assertIsNotNone(user)
        self.assertEqual(self.test_username, user.username)


if __name__ == '__main__':
    unittest.main()
