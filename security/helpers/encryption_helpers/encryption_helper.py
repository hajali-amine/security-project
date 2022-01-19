class EncryptionHelper:
    @staticmethod
    def pad(text: str, modulo: int):
        n = len(text) % modulo
        return text.encode() + (b" " * (modulo - n))
