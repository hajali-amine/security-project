from Crypto.Cipher import DES

from security.helpers.encryption_helpers.encryption_helper import EncryptionHelper


class DataEncryptionStandard:
    # The key has to be of size 8
    key = "defaultk"

    @staticmethod
    def get_name():
        return "DES"

    @staticmethod
    def set_key(key):
        if len(key) == 8:
            DataEncryptionStandard.key = key
        else:
            print("The key provided has a non-compatible size\n")

    # Electronic Code Book (ECB) is a simple mode of operation
    # with a block cipher that's mostly used with symmetric
    # key encryption
    @staticmethod
    def encrypt(msg):
        des = DES.new(DataEncryptionStandard.key.encode(), DES.MODE_ECB)
        padded_text = EncryptionHelper.pad(msg, 8)
        return des.encrypt(plaintext=padded_text).hex()

    @staticmethod
    def decrypt(msg):
        des = DES.new(DataEncryptionStandard.key.encode(), DES.MODE_ECB)
        decrypted_text = des.decrypt(bytes.fromhex(msg))
        return decrypted_text.decode("utf-8").strip()
