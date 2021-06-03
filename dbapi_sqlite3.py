# module import
import sqlite3, os
from sqlite3 import Error

# connection function
def create_connection(db_file):
    # ./database : directory created
    if not os.path.exists("./database"):    # current directory ->database (x)
        os.makedirs("./database")

    # connect
    try:
        conn = sqlite3.connect(db_file)     # -> Connection obj return
        print(sqlite3.version)
    except Error as e:
        print(e, type(e))
        return None                         # connection fail -> NONE
    return conn


# using parameter-> insert
def test_insert_data(db_file, name, category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    # anonymous parameter binding
    sql = """INSERT INTO customer (name, category, region)
    VALUES(?, ?, ?)"""
    res = conn.execute(sql, (name, category, region))

    # INSERT, UPDATE, DELETE -> affected no.of record -> .rowcount return
    print("{} records affected".format(res.rowcount))
    conn.commit()
    conn.close()


def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()


def test_create_table(db_file):
    # connect
    conn = create_connection(db_file)   # Connection
    # cursor got
    cursor = conn.cursor()  # Cursor
    # sql
    ddl = """CREATE TABLE IF NOT EXISTS
    customer (
        id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10)) 
    """
    # sql execute
    cursor.execute(ddl)
    # disconnect
    conn.close()


def test_delete_all(db_file):
    conn = create_connection(db_file)
    sql = "DELETE FROM customer"
    res = conn.execute(sql)

    print("{} records deleted".format(res.rowcount))
    conn.commit()
    conn.close()


def test_insert_bulk_data(db_file):
    # text data insert
    test_delete_all(db_file)    # empty
    test_insert_data(db_file, "A", 1, "city a")
    test_insert_data(db_file, "B", 2, "city a")
    test_insert_data(db_file, "C", 2, "city b")
    test_insert_data(db_file, "D", 1, "city a")
    test_insert_data(db_file, "E", 2, "city b")


def test_select_data(db_file):
    # conn = create_connection(db_file)
    with create_connection(db_file) as conn:    # recommend -> with finish-> auto close()
        # select query execute
        sql = "SELECT * FROM customer"
        cursor = conn.execute(sql)

        # print(type(cursor))
        # result execute
        print(cursor.fetchone())    # 1 record recall
        print(cursor.fetchmany(2))  # 2
        print(cursor.fetchall())    # from current cursor -> the rest recall
    # conn.close()


def test_search_data(db_file):
    conn = create_connection(db_file)

    # palceholder
    #               :key
    #   data -> dic
    sql = """\
    SELECT name, category, region FROM customer
    WHERE region=:region OR category=:category
    """
    cursor = conn.execute(sql, {
        "region": "city a",
        "category": 2
    })

    for customer in cursor.fetchall():  # entire record loop
        print(customer)

# class import
from mysqlite import *

def test_mysqlite_class(db_file):
    # new ojb created
    mydb = Database(db_file)
    sql = """SELECT * FROM customer 
    WHERE region=:region
    """
    res = mydb.execute_select(sql, {
        "region": "city b"
    })

    for customer in res:
        print(customer)


if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    # test_connection(db_file)
    # test_create_table(db_file)
    # test_insert_data(db_file, 'A', 2, 'city a')
    # test_insert_bulk_data(db_file)
    # test_select_data(db_file)
    # test_search_data(db_file)
    test_mysqlite_class(db_file)
