import unittest

from ..EncryptionService import EncryptionService


class EncryptionServiceTest(unittest.TestCase):
    sut: EncryptionService = EncryptionService()
    test_str: str = "TEST TEST TEST TEST"

    def test_encrypted_str_is_not_similar_to_original(self) -> None:
        encrypted_str = self.sut.encrypt(self.test_str)
        self.assertNotEqual(self.test_str, encrypted_str)
        self.assertNotAlmostEqual(len(self.test_str), len(encrypted_str))

    def test_decrypted_str_matches_original_and_not_encrypted_str(self) -> None:
        encrypted_str = self.sut.encrypt(self.test_str)
        decrypted_str = self.sut.decrypt(encrypted_str)
        self.assertNotEqual(encrypted_str, decrypted_str)
        self.assertEqual(self.test_str, decrypted_str)

    def test_hash_differs_from_input_and_ecrypted_str(self) -> None:
        encrypted_str = self.sut.encrypt(self.test_str)
        hashed_str = self.sut.hash(self.test_str)
        self.assertNotEqual(encrypted_str, hashed_str)
        self.assertNotEqual(self.test_str, hashed_str)


if __name__ == '__main__':
    unittest.main()
