import re
from random import randint


class EmailHelper:
    @staticmethod
    def is_valid(email):
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@insat.ucar.tn)\"?"
        if not re.match(pattern, email):
            print("this is not an INSAT email\n")
            return False
        else:
            return True

    @staticmethod
    def generate_random_code():
        return randint(1000, 9999)

