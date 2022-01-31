import mysql.connector as con


class DB(con):
    def __init__(self):
        super().__init__()
        self.__config = {
            "host": "localhost",
            "user": "root",
            "password": "arnab",
            "database": "arnab",
        }
