import os

from dotenv import load_dotenv


from security.authentication.sign_in.sign_in import SignIn
from security.authentication.sign_up.sign_up import SignUp
from security.config.email_config.email_config import EmailConfig
from security.menu.asymmetric_encryption_menu import AsymmetricEncryptionMenu
from security.menu.crack_hash_menu import CrackHashMenu
from security.menu.encoding_menu import EncodingMenu
from security.menu.hash_menu import HashMenu
from security.menu.symmetric_encryption_menu import SymmetricEncryptionMenu


load_dotenv(".env")
if __name__ == '__main__':
    EmailConfig.setup(
        sender_email=os.environ.get("EMAIL_LOGIN"),
        sender_password=os.environ.get("EMAIL_PASSWORD")
    )
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
              "42 - Encrypt a message asymmetrically\n"
              "0 - Logout")

        option = int(input("Option: "))

        if option == 0:
            user = SignIn.logout()

        switcher = {
            1: EncodingMenu,
            2: HashMenu,
            3: CrackHashMenu,
            41: SymmetricEncryptionMenu,
            42: AsymmetricEncryptionMenu,
        }

        option_menu = switcher.get(option, "Invalid option")

        if option in switcher.keys():
            menu = option_menu()
            menu.launch()

