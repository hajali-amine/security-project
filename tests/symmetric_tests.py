import unittest

from security.encryption.symmetric.aes import AdvancedEncryptionStandard
from security.encryption.symmetric.des import DataEncryptionStandard


class SymmetricTests(unittest.TestCase):
    def setUp(self):
        DataEncryptionStandard.set_key("unittest")
        AdvancedEncryptionStandard.set_key("unittestunittest")

    def test_des(self):
        word = "Test Message"
        hashed_word = DataEncryptionStandard.encrypt(word)
        self.assertNotEqual(word, hashed_word)
        self.assertEqual(word, DataEncryptionStandard.decrypt(hashed_word))

    def test_aes(self):
        word = "Test Message"
        hashed_word = AdvancedEncryptionStandard.encrypt(word)
        self.assertNotEqual(word, hashed_word)
        self.assertEqual(word, AdvancedEncryptionStandard.decrypt(hashed_word))
