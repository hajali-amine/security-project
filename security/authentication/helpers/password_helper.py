import re
import hashlib


class PasswordHelper:
    test = True

    @staticmethod
    def is_valid(pwd):
        # The password should follow the pattern LastName.FirstName@insat.ucar.tn
        # with len(LastName) = 6 and Len(FirstName) = 5
        pattern = r"\"?(\w{6}\.\w{5}@insat.ucar.tn)\"?"
        if not PasswordHelper.test and not re.match(pattern, pwd):
            print("this password is not valid\n")
            return False
        else:
            return True

    @staticmethod
    def hash(pwd):
        return hashlib.sha224(pwd.encode('utf-8')).hexdigest()
