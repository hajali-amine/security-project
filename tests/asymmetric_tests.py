import unittest

from security.encryption.asymmetric.elgamal import ElGamal
from security.encryption.asymmetric.rsa import RSA


class SymmetricTests(unittest.TestCase):
    def setUp(self):
        RSA.set_keys()
        ElGamal.set_keys()

    def test_rsa(self):
        word = "Test Message"
        hashed_word = RSA.encrypt(word, RSA.get_pub_key())
        self.assertNotEqual(word, hashed_word)
        self.assertEqual(word, RSA.decrypt(hashed_word))

    def test_elgamal(self):
        word = "Test Message"
        hashed_word = ElGamal.encrypt(word, ElGamal.get_pub_key())
        self.assertNotEqual(word, hashed_word)
        self.assertEqual(word, ElGamal.decrypt(hashed_word))
