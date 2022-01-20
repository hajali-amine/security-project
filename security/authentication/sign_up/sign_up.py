from getpass import getpass

from security.config.email_config.email_config import EmailConfig
from security.helpers.auth_helpers.email_helper import EmailHelper
from security.helpers.auth_helpers.password_helper import PasswordHelper
from security.config.db_config.db_config import DbConfig
from security.models.user import User


class SignUp:
    @staticmethod
    def signup():
        fname = input("first name:\n")
        lname = input("last name:\n")
        email = input("email:\n")
        sql = "SELECT * FROM user WHERE email LIKE %s"
        DbConfig.get_instance().cursor.execute(sql, (email,))
        # user = (email, first_name, last_name, hashed_pwd)
        user = DbConfig.get_instance().cursor.fetchall()

        if user:
            print("The email already exists")

        elif EmailHelper.is_valid(email):
            pwd = getpass("pwd:\n")
            hashed_pwd = PasswordHelper.hash(pwd)
            confirm_pwd = getpass("confirm_pwd:\n", )

            if hashed_pwd == PasswordHelper.hash(confirm_pwd):
                code = EmailHelper.generate_random_code()
                EmailConfig.send_email(email, str(code))
                input_code = int(input("Verification code: "))

                if code == input_code:
                    sql = "INSERT INTO user (email, first_name, last_name, pwd) VALUES (%s, %s, %s, %s)"
                    val = (email, fname, lname, hashed_pwd)
                    DbConfig.get_instance().cursor.execute(sql, val)
                    DbConfig.get_instance().connection.commit()
                    return User(first_name=fname, last_name=lname, email=email)
                else:
                    print("Codes don't match")
            else:
                print("Passwords don't match\n")
        return None
