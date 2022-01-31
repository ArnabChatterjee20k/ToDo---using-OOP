import mysql.connector as con , datetime
class DB(con.MySQLConnection):
    def __init__(self):
        self.__config = {
            "host": "localhost",
            "user": "root",
            "password": "arnab",
            "database": "todo",
        }
        super().__init__(**self.__config) # connection class needs the values.
        self.__table = "todo"
        self.cursor = self.cursor() # cursor object

    def insert(self,task):
        try:
            self.cursor.execute(f"insert into todo (task,date) values ('{task}','{datetime.date.today()}')")
            self.commit()
            return True
        except:
            return False

    def update(self , sl , todo):
        try:
            self.cursor.execute(f"update {self.__table} set todo = {todo} where id={sl}")
            self.commit()
            return True
        except:
            return False

    def delete(self,sl):
        try:
            self.cursor.execute(f"delete from {self.__table} where id={sl}")
            self.commit()
            return True
        except:
            return False

    def fetch(self):
        self.cursor.execute(f"select * from {self.__table}")
        return self.cursor.fetchall()

    def __repr__(self):
        return str({"host":self._host,"database":self._database})