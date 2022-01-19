from jedi.inference.gradual.base import GenericClass

from security.authentication.sign_in.sign_in import SignIn
from security.authentication.sign_up.sign_up import SignUp
from security.encoding.encode import Encode
from security.encryption.asymmetric.rsa import RSA
from security.encryption.symmetric.des import DataEncryptionStandard
from security.hashing.hash import Hash
from security.menu.encoding_menu import EncodingMenu
from security.menu.hash_menu import HashMenu
from security.menu.symmetric_encryption_menu import SymmetricEncryptionMenu

if __name__ == '__main__':
    user = None

    while user is None:
        print("Choose an option:\n"
              "1 - Sign up\n"
              "2 - Sign in\n")

        option = int(input("Option: "))
        switcher = {
            1: SignUp.signup,
            2: SignIn.signin,
        }

        option_func = switcher.get(option, "Invalid option")
        user = option_func()

    while user is not None:
        menu = None
        print("---------- General Menu ----------\n"
              "Choose an option:\n"
              "1 - Encode a message\n"
              "2 - Hash a message\n"
              "3 - Crack a hash\n"
              "41 - Encrypt a message symmetrically\n"
              "0 - Logout")

        option = int(input("Option: "))

        if option == 0:
            user = SignIn.logout()

        switcher = {
            1: EncodingMenu,
            2: HashMenu,
            41: SymmetricEncryptionMenu,
        }

        option_menu = switcher.get(option, "Invalid option")

        if option in switcher.keys():
            menu = option_menu()
            menu.launch()

