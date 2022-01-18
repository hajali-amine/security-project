import mysql.connector


class DbConfig:
    __instance = None

    def __init__(self):

        if DbConfig.__instance is not None:
            raise Exception("DbConfig is singleton")
        else:
            try:
                config = {
                    'user': 'user',
                    'password': 'user',
                    'host': 'localhost',
                    'port': '32000',
                    'database': 'security',
                    'raise_on_warnings': True, }

                self.connection = mysql.connector.connect(**config)
                self.cursor = self.connection.cursor()
                # cursor.execute("SELECT * FROM user")
                # result = cursor.fetchall()
                # for row in result:
                #     print(row)

            except mysql.connector.Error as e:
                print(e)

    @staticmethod
    def get_instance():
        if DbConfig.__instance is None:
            DbConfig.__instance = DbConfig()
        return DbConfig.__instance
