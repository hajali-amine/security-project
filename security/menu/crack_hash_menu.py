import re
from getpass import getpass

from security.hashing.hash import Hash
from security.hashing.hash_cracker import HashCracker
from security.menu.generic_menu import GenericMenu


class CrackHashMenu(GenericMenu):
    def init_menu(self):
        pass

    def start_menu(self):
        while True:
            print("---------- Crack Hash Menu ----------\n"
                  "Choose an option:\n"
                  "1 - Crack hash a message using md5\n"
                  "2 - Crack hash a message using sha1\n"
                  "3 - Crack hash a message using sha256\n"
                  "0 - Exit\n")

            option = int(input("Option: "))

            if option == 0:
                break

            switcher = {
                1: Hash.md5,
                2: Hash.sha1,
                3: Hash.sha256
            }

            pwd = ""
            while not re.match(r"[a-z]{6}\.[a-z]{5}@insat\.ucar\.tn", pwd):
                pwd = getpass("Password: ")

            option_func = switcher.get(option, "Invalid option")

            hashed_pwd = option_func(pwd)
            result_pwd = HashCracker.crack_hash(hashed_pwd, option_func, "/security/hashing/emails.txt")

            print("the password is {}".format(result_pwd))