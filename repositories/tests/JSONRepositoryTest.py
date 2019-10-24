import os
import unittest
import json

from repositories.JSONRepository import JSONRepository

FILENAME: str = "testrepo.txt"


class JSONRepositoryTest(unittest.TestCase):
    TEST_STRING: str = "{\"test\": \"TEST TEST TEST\"}"
    sut: JSONRepository = JSONRepository(FILENAME)

    def setUpClass() -> None:
        with open(FILENAME, 'a'):
            os.utime(FILENAME, None)

    def tearDownClass() -> None:
        os.remove(FILENAME)

    def test_get_returns_empty_dict_when_file_is_empty(self) -> None:
        text_repo = self.sut.get()
        self.assertEqual(text_repo,{})

    def test_save_saves_string_value_into_repo(self) -> None:
        self.sut.save(self.TEST_STRING)
        result = self.sut.get()
        self.assertEqual(result, json.loads(self.TEST_STRING))


if __name__ == '__main__':
    unittest.main()
