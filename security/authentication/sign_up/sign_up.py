import getpass

from security.authentication.helpers.email_helper import EmailHelper

from security.authentication.helpers.password_helper import PasswordHelper


class SignUp:
    @staticmethod
    def signup():
        email = input("email:")
        if EmailHelper.is_valid(email):
            print("good")
        pwd = input("pwd:")
        if PasswordHelper.is_valid(pwd):
            print("good")
        confirm_pwd = input("confirm_pwd:", )
        if PasswordHelper.hash(pwd) == PasswordHelper.hash(confirm_pwd):
            print("all set")
