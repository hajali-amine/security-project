import rsa

from security.encryption.generic.generic_asymmetric import GenericAsymmetric


class RSA(GenericAsymmetric):
    # The key has to be of size 16
    private_key = None
    public_key = None

    @staticmethod
    def get_name():
        return "RSA"

    @staticmethod
    def set_keys():
        RSA.public_key, RSA.private_key = rsa.newkeys(512)

    @staticmethod
    def encrypt(msg, pub_key):
        return rsa.encrypt(msg.encode(), pub_key).hex()

    @staticmethod
    def decrypt(msg):
        return rsa.decrypt(bytes.fromhex(msg), RSA.private_key).decode("utf-8")

    @staticmethod
    def get_pub_key():
        return RSA.public_key

