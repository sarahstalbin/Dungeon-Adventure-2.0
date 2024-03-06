import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    Create a connection to the Monster SQLite database
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


def select_dungeon_character_attribute(conn, character_name, character_type, attribute):
    """
    Queries a specific attribute for a given monster type and name.
    :param conn: the Connection object
    :param character_name: the name of the Dungeon Character
    :param attribute: the attribute to query
    :param character_type: the type of Dungeon Character
    :return: The value of the specified attribute for the given monster
    """
    cur = conn.cursor()
    sql = f"SELECT {attribute} FROM {character_type} WHERE name=?"
    cur.execute(sql, (character_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return None


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
        # Assuming the column names match the attribute names of the Hero class
        column_names = [description[0] for description in cur.description]
        return dict(zip(column_names, row))
    else:
        return None
