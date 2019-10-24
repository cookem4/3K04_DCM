import unittest
from datetime import datetime

from main.exceptions.SingletonInstantiationException import SingletonInstantiationException
from main.services.SessionService import SessionService


def try_and_get_singleton():
    return SessionService()


class SessionServiceTest(unittest.TestCase):
    username: str = "USERNAME"
    sut: SessionService = SessionService.get_instance()

    def test_throws_eror_on_double_instantiation(self):
        success = False
        try:
            SessionService()
        except SingletonInstantiationException:
            success = True
        assert success

    def test_start_session_starts_session(self) -> None:
        self.sut.start_session(self.username)
        session = self.sut.get()
        self.assertEqual(self.username, session.username)
        self.assertAlmostEqual(datetime.now(), session.datetime)

    def test_invalidate_clears_session(self):
        self.sut.start_session(self.username)
        session_before = self.sut.get()
        self.sut.invalidate()
        session_after = self.sut.get()
        self.assertNotEqual(session_before,session_after)
        self.assertIsNone(session_after)


if __name__ == '__main__':
    unittest.main()
