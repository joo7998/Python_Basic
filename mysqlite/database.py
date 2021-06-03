import sqlite3

class Database:
    # initialize, create
    def __init__(self, db = None):
        self.conn = None
        self.cursor = None

        if db:  # db parameter
            self.open(db)

    # connection method
    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database connection failed")

    # close method
    def close(self):
        if self.conn:
            self.conn.commit()  # I, U, D query commit
            self.cursor.close()
            self.conn.close()

    # __enter__ : with -> called
    def __enter__(self):
        return self

    # __exit__  : with ended -> called
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # SELECT query execute method
    def execute_select(self, sql, parameter=None):
        if parameter is not None:   # parameter (o)
            self.cursor.execute(sql, parameter)
        else:   # parameter (x)
            self.cursor.execute(sql)

        data = list(self.cursor.fetchall())
        return data

    # INSERT, UPDATE, DELETE query execute method
    def execute_cud(self, sql, parameter=None):
        if parameter is not None:   # parameter(o)
            self.cursor.execute(sql, parameter)
        else:
            self.cursor.execute(sql)

        return self.cursor.rowcount
