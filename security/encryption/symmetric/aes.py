from Crypto.Cipher import AES

from security.helpers.encryption_helpers.encryption_helper import EncryptionHelper


class AdvancedEncryptionStandard:
    # The key has to be of size 16
    key = "defaultkdefaultk"

    @staticmethod
    def get_name():
        return "AES"

    @staticmethod
    def set_key(key):
        if len(key) == 16:
            AdvancedEncryptionStandard.key = key
        else:
            print("The key provided has a non-compatible size\n")

    # Electronic Code Book (ECB) is a simple mode of operation
    # with a block cipher that's mostly used with symmetric
    # key encryption
    @staticmethod
    def encrypt(msg):
        des = AES.new(AdvancedEncryptionStandard.key.encode(), AES.MODE_ECB)
        padded_text = EncryptionHelper.pad(msg, 16)
        return des.encrypt(plaintext=padded_text).hex()

    @staticmethod
    def decrypt(msg):
        des = AES.new(AdvancedEncryptionStandard.key.encode(), AES.MODE_ECB)
        decrypted_text = des.decrypt(bytes.fromhex(msg))
        return decrypted_text.decode("utf-8").strip()
