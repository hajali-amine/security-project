import re


class EmailHelper:
    @staticmethod
    def is_valid(email):
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@insat.ucar.tn)\"?"
        if not re.match(pattern, email):
            print("this is not an INSAT email\n")
            return False
        else:
            return True
