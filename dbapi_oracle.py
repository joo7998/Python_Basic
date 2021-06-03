# pip install cx_Oracle
import cx_Oracle    # module import

def create_connection():
    # dsn
    dsn = cx_Oracle.makedsn("localhost",
                            1521,
                            "orcl")   # server address, port, SID(service id)
    # connect
    db = cx_Oracle.connect("hr", "hr", dsn) # account, password, data source name
    return db


def test_connect():
    # connect
    conn = create_connection()
    print(type(conn))
    conn.close()


def test_basic_query():
    # hr.employees -> all records return
    conn = create_connection()  # Connection
    cursor = conn.cursor()  # Cursor

    # SQL execute
    sql = "SELECT * FROM employees"
    cursor.execute(sql)

    # print(cursor)
    print("fetchone")
    print(cursor.fetchone())
    print("fetchmany")
    print(cursor.fetchmany(2))

    for row in cursor.fetchall():
        print(row)

    conn.close()


def test_placeholder():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM employees WHERE last_name=:1 or last_name=:2"
    cursor.execute(sql, ("King", "Grant"))

    for record in cursor:
        print(record)

    conn.close()


def test_dictionary():
    conn = create_connection()
    cursor = conn.cursor()
    # SQL execute
    sql = "SELECT * FROM employees"
    cursor.execute(sql)

    print(cursor.description)   # cursor status check

    # column info, record -> zip -> dic
    for record in cursor:
        # created dic
        record_dct = dict(zip([d[0] for d in cursor.description], record))
        print(record_dct)

    conn.close()


if __name__ == "__main__":
    # test_connect()
    # test_basic_query()
    # test_placeholder()
    test_dictionary()
