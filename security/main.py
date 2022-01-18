from config.db_config.db_config import DbConfig

# DbConfig.get_instance().cursor.execute("SELECT * FROM user")
# res = DbConfig.get_instance().cursor.fetchall()
#
# for row in res:
#     print(row)
from authentication.sign_up.sign_up import SignUp

SignUp.signup()