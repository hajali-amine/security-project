class GenericAsymmetric:
    @staticmethod
    def get_name():
        """ Gets name of the algorithm """
        raise Exception("Not defined")

    @staticmethod
    def set_keys():
        """ Sets the key """
        raise Exception("Not defined")

    @staticmethod
    def encrypt(msg, pub_key):
        """ Encrypts a message """
        raise Exception("Not defined")

    @staticmethod
    def decrypt(msg):
        """ Decrypts a message """
        raise Exception("Not defined")

    @staticmethod
    def get_pub_key():
        """ Provides the public key """
        raise Exception("Not defined")