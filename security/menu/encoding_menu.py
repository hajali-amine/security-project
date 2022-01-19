from security.encoding.encode import Encode
from security.menu.generic_menu import GenericMenu


class EncodingMenu(GenericMenu):
    def init_menu(self):
        pass

    def start_menu(self):
        while True:
            print("---------- Encoding Menu ----------\n"
                  "Choose an option:\n"
                  "1 - Encode a message\n"
                  "2 - Decode a message\n"
                  "0 - Exit\n")

            option = int(input("Option: "))

            if option == 0:
                break

            switcher = {
                1: Encode.encode,
                2: Encode.decode,
            }

            msg = input("Message: ")

            option_func = switcher.get(option, "Invalid option")

            print(option_func(msg))
