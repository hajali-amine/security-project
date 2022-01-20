from security.encryption.asymmetric.elgamal import ElGamal
from security.encryption.asymmetric.rsa import RSA
from security.encryption.symmetric.aes import AdvancedEncryptionStandard
from security.encryption.symmetric.des import DataEncryptionStandard
from security.menu.generic_menu import GenericMenu


class AsymmetricEncryptionMenu(GenericMenu):
    def __init__(self):
        self.algorithm_option = 0
        self.algorithm = {
            1: RSA,
            2: ElGamal
        }

    def init_menu(self):
        while self.algorithm_option not in self.algorithm.keys():
            print("Which algorithm do you want to work with?\n"
                  "1 - RSA\n"
                  "2 - ElGamal\n")
            self.algorithm_option = int(input("Option: "))

        self.algorithm[self.algorithm_option].set_keys()

    def start_menu(self):
        while True:
            print("---------- Asymmetrical Encryption Menu ----------\n"
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

            if option == 1:
                print(option_func(msg, self.algorithm[self.algorithm_option].get_pub_key()))
            elif option == 2:
                print(option_func(msg))
