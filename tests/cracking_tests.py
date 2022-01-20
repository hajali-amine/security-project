import unittest

from security.hashing.hash import Hash
from security.hashing.hash_cracker import HashCracker


class CrackingTests(unittest.TestCase):
    def setUp(self):
        self.file_path = "../security/hashing/emails.txt"

    def test_md5(self):
        hashed_pwd = Hash.md5("aaaaaa.aaaaa@insat.ucar.tn")
        self.assertEqual("aaaaaa.aaaaa@insat.ucar.tn", HashCracker.crack_hash(hashed_pwd, Hash.md5, self.file_path))

    def test_sha1(self):
        hashed_pwd = Hash.sha1("aaaaaa.aaaaa@insat.ucar.tn")
        self.assertEqual("aaaaaa.aaaaa@insat.ucar.tn", HashCracker.crack_hash(hashed_pwd, Hash.sha1, self.file_path))

    def test_sha256(self):
        hashed_pwd = Hash.sha256("aaaaaa.aaaaa@insat.ucar.tn")
        self.assertEqual("aaaaaa.aaaaa@insat.ucar.tn", HashCracker.crack_hash(hashed_pwd, Hash.sha256, self.file_path))