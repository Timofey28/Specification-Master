import psycopg2


class Database:
    def __init__(self, db_dbname: str, db_host: str, db_user: str, db_password: str):
        self.connection = psycopg2.connect(dbname=db_dbname,
                                           host=db_host,
                                           user=db_user,
                                           password=db_password)
        self.curr = self.connection.cursor()
