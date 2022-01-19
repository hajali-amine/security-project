from security.encryption.symmetric.aes import AdvancedEncryptionStandard
from security.encryption.symmetric.des import DataEncryptionStandard
from security.menu.generic_menu import GenericMenu


class SymmetricEncryptionMenu(GenericMenu):
    def __init__(self):
        self.algorithm_option = 0
        self.algorithm = {
            1: DataEncryptionStandard,
            2: AdvancedEncryptionStandard
        }

    def init_menu(self):
        while self.algorithm_option not in self.algorithm.keys():
            print("Which algorithm do you want to work with?\n"
                  "1 - DES\n"
                  "2 - AES\n")
            self.algorithm_option = int(input("Option: "))

        key = input("Give a key: ")
        self.algorithm[self.algorithm_option].set_key(key)

    def start_menu(self):
        while True:
            print("---------- Symmetrical Encryption Menu ----------\n"
                  "Choose an option:\n"
                  "1 - Encrypt a message using " + self.algorithm[self.algorithm_option].get_name() + "\n"
                  "2 - Decrypt a message using " + self.algorithm[self.algorithm_option].get_name() + "\n"
                  "0 - Exit\n")

            option = int(input("Option: "))

            if option == 0:
                break

            switcher = {
                1: self.algorithm[self.algorithm_option].encrypt,
                2: self.algorithm[self.algorithm_option].decrypt,
            }

            msg = input("Message: ")

            option_func = switcher.get(option, "Invalid option")

            print(option_func(msg))
