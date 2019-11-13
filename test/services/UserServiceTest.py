import os
import unittest

from main.data.pacingmode.PacingModeBuilder import PacingModeBuilder, PacingModes
from main.services.UserService import UserService, UserBuilder, User


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

    def setUp(self) -> None:
        self.sut.create(self.test_user)

    def tearDown(self) -> None:
        self.sut.delete(self.test_username)

    def test_create_creates_user(self) -> None:
        user: User = self.sut.read(self.test_username)
        self.assertIsNotNone(user)
        self.assertEqual(self.test_username, user.username)

    def test_update_pacing_mode_updates_user(self) -> None:
        self.sut.update_pacing_mode(self.test_username,
                                    PacingModeBuilder.empty_specific(PacingModes.VVI))
        user: User = self.sut.read(self.test_username)
        self.assertIsNotNone(user)
        self.assertEqual(user.pacing_mode, PacingModes.VVI.name)

    def test_delete_deletes_user(self) -> None:
        self.assertTrue(self.sut.exists(self.test_username))
        self.sut.delete(self.test_username)
        self.assertFalse(self.sut.exists(self.test_username))

if __name__ == '__main__':
    unittest.main()
