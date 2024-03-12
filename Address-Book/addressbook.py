'''
importing all the required libraries
'''
import sqlite3
from sqlite3 import Error

list_of_names = []

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        r_set = conn.execute('''SELECT * from tasks''')
        for student in r_set:
            list_of_names.append(student[1])
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    return

database = r"./Address-Book/addressbook.db"
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    status_id integer NOT NULL
                                );"""
