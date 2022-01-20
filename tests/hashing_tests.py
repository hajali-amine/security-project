import unittest

from security.hashing.hash import Hash


class HashingTests(unittest.TestCase):
    def test_md5(self):
        phrase_without_space_hash = Hash.md5("This is a test")
        phrase_with_space_hash = Hash.md5("This is a test ")
        self.assertEqual("ce114e4501d2f4e2dcea3e17b546f339", phrase_without_space_hash)
        self.assertEqual("e5eb40a5cac6cca6a4019aeeeb068db1", phrase_with_space_hash)
        self.assertEqual(len(phrase_with_space_hash), len(phrase_without_space_hash))

    def test_sha1(self):
        phrase_without_space_hash = Hash.sha1("This is a test")
        phrase_with_space_hash = Hash.sha1("This is a test ")
        self.assertEqual("a54d88e06612d820bc3be72877c74f257b561b19", phrase_without_space_hash)
        self.assertEqual("e9d3e1bf55ddbc028c818557ada10e3c5ad1e60d", phrase_with_space_hash)
        self.assertEqual(len(phrase_with_space_hash), len(phrase_without_space_hash))

    def test_sha256(self):
        phrase_without_space_hash = Hash.sha256("This is a test")
        phrase_with_space_hash = Hash.sha256("This is a test ")
        self.assertEqual("c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e", phrase_without_space_hash)
        self.assertEqual("5caf55470241ab8d00393a98f90c9a84f20c1c85ae94d55479c1f566055f15d9", phrase_with_space_hash)
        self.assertEqual(len(phrase_with_space_hash), len(phrase_without_space_hash))