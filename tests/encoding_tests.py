import unittest

from security.encoding.encode import Encode


class EncodingTests(unittest.TestCase):
    def test_encode(self):
        self.assertEqual("5468697320697320612074657374", Encode.encode("This is a test"))

    def test_decode(self):
        self.assertEqual("This is a test", Encode.decode("5468697320697320612074657374"))