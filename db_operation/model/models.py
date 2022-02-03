import mysql.connector as con, datetime
import sqlite3


class my_sql_db(con.MySQLConnection):
    def __init__(self):
        self.__config = {
            "host": "localhost",
            "user": "root",
            "password": "arnab",
            "database": "todo",
        }
        super().__init__(**self.__config)  # connection class needs the values.
        self.table = "todo"
        self.cursor = self.cursor()  # cursor object

    def insert(self, task):
        try:
            self.cursor.execute(
                f"insert into todo (task,date) values ('{task}','{datetime.date.today()}')"
            )
            self.commit()
            return True
        except:
            return False

    def update(self, sl, todo):
        try:
            self.cursor.execute(f"update {self.table} set todo = {todo} where id={sl}")
            self.commit()
            return True
        except:
            return False

    def delete(self, sl):
        try:
            self.cursor.execute(f"delete from {self.table} where id={sl}")
            self.commit()
            return True
        except:
            return False

    def fetch(self):
        self.cursor.execute(f"select * from {self.table}")
        return self.cursor.fetchall()

    def __repr__(self):
        return str({"host": self._host, "database": self._database})


class sql_lite_db(sqlite3.Connection, my_sql_db):  # multiple inheritance
    def __init__(self):
        self.__config = "todo.db"
        super().__init__(self.__config)
        self.cursor = self.cursor()

    def create_table(self):
        self.cursor.execute(
            """
        CREATE TABLE todo
(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    task VARCHAR(100) NOT NULL,
    date DATE NOT NULL
)
        """
        )

a = sql_lite_db()
a.create_table()