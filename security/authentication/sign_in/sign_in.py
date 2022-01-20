from getpass import getpass

from security.helpers.auth_helpers.email_helper import EmailHelper
from security.helpers.auth_helpers.password_helper import PasswordHelper
from security.config.db_config.db_config import DbConfig
from security.models.user import User


class SignIn:
    @staticmethod
    def signin():
        email = input("email:\n")
        if EmailHelper.is_valid(email):
            sql = "SELECT * FROM user WHERE email LIKE %s"
            DbConfig.get_instance().cursor.execute(sql, (email,))
            # user = (email, first_name, last_name, hashed_pwd)
            user = DbConfig.get_instance().cursor.fetchall()
            if user:
                pwd = getpass("pwd:\n")
                if user[0][3] == PasswordHelper.hash(pwd):
                    print("Hello {} {}\n\n".format(user[0][1], user[0][2]))
                    return User(first_name=user[0][1], last_name=user[0][2], email=user[0][0])
                else:
                    print("Wrong password\n")
            else:
                print("No such email exists\n")

    @staticmethod
    def logout():
        return None
