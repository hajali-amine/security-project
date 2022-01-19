import rsa


class RSA:
    # The key has to be of size 16
    private_key = None
    public_key = None

    @staticmethod
    def get_name():
        return "RSA"

    @staticmethod
    def set_key():
        RSA.public_key, RSA.private_key = rsa.newkeys(512)

    @staticmethod
    def encrypt(msg, pub_key):
        return rsa.encrypt(msg.encode(), pub_key).hex()

    @staticmethod
    def decrypt(msg):
        return rsa.decrypt(msg.encode(), RSA.private_key).hex()

    @staticmethod
    def get_pub_key():
        return RSA.public_key