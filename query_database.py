import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    Create a connection to the Dungeon Character SQLite database
    :param db_file: the database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def select_row(conn, table_name, character_name):
    """
    Queries rows in the specified table with the given name and returns the data.
    :param conn: the Connection object
    :param table_name: the name of the table to query
    :param character_name: the name of the character to select
    :return: a list of tuples, each representing a row in the table
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE name=?", (character_name,))
    row = cur.fetchone()
    if row:
        column_names = [description[0] for description in cur.description]
        return dict(zip(column_names, row))
    else:
        return None
