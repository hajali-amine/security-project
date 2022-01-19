from security.hashing.hash import Hash
from security.menu.generic_menu import GenericMenu


class HashMenu(GenericMenu):
    def init_menu(self):
        pass

    def start_menu(self):
        while True:
            print("---------- Hash Menu ----------\n"
                  "Choose an option:\n"
                  "1 - Hash a message using md5\n"
                  "2 - Hash a message using sha1\n"
                  "3 - Hash a message using sha256\n"
                  "0 - Exit\n")

            option = int(input("Option: "))

            if option == 0:
                break

            switcher = {
                1: Hash.md5,
                2: Hash.sha1,
                3: Hash.sha256
            }

            msg = input("Message: ")

            option_func = switcher.get(option, "Invalid option")

            print(option_func(msg))
