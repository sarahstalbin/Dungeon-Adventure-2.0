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


def select_all_ogre_rows(conn):
    """
    Queries all rows in the ogres table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM ogre")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_gremlin_rows(conn):
    """
    Queries all rows in the gremlin table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM gremlin")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_skeleton_rows(conn):
    """
    Queries all rows in the skeleton table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM skeleton")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_troll_rows(conn):
    """
    Queries all rows in the troll table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM troll")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_chimera_rows(conn):
    """
    Queries all rows in the chimera table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM chimera")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_dragon_rows(conn):
    """
    Queries all rows in the dragon table and displays the data.
    :param conn: the Connection object
    :return: None
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM dragon")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_monster_attribute(conn, monster_type, attribute, monster_name):
    """
    Queries a specific attribute for a given monster type and name.
    :param conn: the Connection object
    :param monster_type: the type of monster
    :param attribute: the attribute to query
    :param monster_name: the name of the monster
    :return: The value of the specified attribute for the given monster
    """
    cur = conn.cursor()
    sql = f"SELECT {attribute} FROM {monster_type} WHERE name=?"
    cur.execute(sql, (monster_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return None
