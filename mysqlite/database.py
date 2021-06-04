import sqlite3

class Database:

    def __init__(self, db = None):
        self.conn = None
        self.cursor = None

        if db:
            self.open(db)


    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database connection failed")


    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


    def execute_select(self, sql, parameter=None):
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else:
            self.cusor.execute(sql)

        data = list(self.cursor.fetchall())
        return data


    def execute_cud(self, sql, parameter=None):
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else:
            self.cursor.execute(sql)

        return self.cursor.rowcount