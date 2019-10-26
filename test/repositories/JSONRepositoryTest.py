import json
import os
import unittest

from main.repositories.JSONRepository import JSONRepository

FILENAME: str = "testrepo.txt"


class JSONRepositoryTest(unittest.TestCase):
    TEST_STRING_ONE: str = "{\"test\": \"TEST TEST TEST\"}"
    TEST_STRING_TWO: str = "{\"another\": \"TEST TEST TEST\"}"

    sut: JSONRepository = JSONRepository(FILENAME)

    def setUpClass() -> None:
        with open(FILENAME, 'a'):
            os.utime(FILENAME, None)

    def tearDownClass() -> None:
        os.remove(FILENAME)

    def test_get_returns_empty_dict_when_file_is_empty(self) -> None:
        text_repo = self.sut.get()
        self.assertEqual(text_repo, {})

    def test_save_saves_string_value_into_repo(self) -> None:
        self.sut.save(self.TEST_STRING_ONE)
        result = self.sut.get()
        self.assertEqual(result, json.loads(self.TEST_STRING_ONE))

    def test_save_replaces_existing_data(self) -> None:
        self.sut.save(self.TEST_STRING_ONE)
        result1 = self.sut.get()
        self.sut.save(self.TEST_STRING_TWO)
        result2 = self.sut.get()
        self.assertNotEqual(result1, result2)
        self.assertEqual(result2, json.loads(self.TEST_STRING_TWO))


if __name__ == '__main__':
    unittest.main()
