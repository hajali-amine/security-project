import re
import hashlib


class PasswordHelper:
    @staticmethod
    def is_valid(pwd):
        pattern = r"\"?(\w{6}\.\w{5}@insat.ucar.tn)\"?"
        if not re.match(pattern, pwd):
            print("this password is not valid")
            return False
        else:
            return True

    @staticmethod
    def hash(pwd):
        return hashlib.sha224(pwd.encode('utf-8')).hexdigest()
