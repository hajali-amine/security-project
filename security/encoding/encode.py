class Encode:
    @staticmethod
    def encode(msg):
        return msg.encode("utf-8").hex()

    @staticmethod
    def decode(encoded_msg):
        return bytes.fromhex(encoded_msg).decode("utf-8")
