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


def select_hero_attribute(conn, hero_name, hero_type, attribute):
    """
        Queries a specific attribute for a given hero_name.
        :param conn: the Connection object
        :param hero_type: the type of hero
        :param attribute: the attribute to query
        :param hero_name: the name of the hero
        :return: The value of the specified attribute for the given hero
        """
    cur = conn.cursor()
    sql = f"SELECT {attribute} FROM {hero_type} WHERE name=?"
    cur.execute(sql, (hero_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return None
