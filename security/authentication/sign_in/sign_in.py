from security.authentication.helpers.email_helper import EmailHelper
from security.authentication.helpers.password_helper import PasswordHelper
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
                pwd = input("pwd:\n")
                if user[0][3] == PasswordHelper.hash(pwd):
                    print("Hello {} {}".format(user[0][1], user[0][2]))
                    return User(first_name=user[0][1], last_name=user[0][2], email=user[0][0])
                else:
                    print("Wrong password\n")
            else:
                print("No such email exists\n")

    @staticmethod
    def logout():
        return None
