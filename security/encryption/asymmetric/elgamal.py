from security.encryption.generic.generic_asymmetric import GenericAsymmetric
from security.modules.elgamal import elgamal


class ElGamal(GenericAsymmetric):
    # The key has to be of size 16
    private_key = None
    public_key = None

    @staticmethod
    def get_name():
        return "ElGamal"

    @staticmethod
    def set_keys():
        elgamal_keys = elgamal.generate_keys(128)
        ElGamal.public_key = elgamal_keys["publicKey"]
        ElGamal.private_key = elgamal_keys["privateKey"]

    @staticmethod
    def encrypt(msg, pub_key):
        return elgamal.encrypt(pub_key, msg)

    @staticmethod
    def decrypt(msg):
        return elgamal.decrypt(ElGamal.private_key, msg)

    @staticmethod
    def get_pub_key():
        return ElGamal.public_key
