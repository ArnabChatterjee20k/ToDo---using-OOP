from ..model import models
sqllite = models.sql_lite_db()
def create_table():
    sqllite.create_table()