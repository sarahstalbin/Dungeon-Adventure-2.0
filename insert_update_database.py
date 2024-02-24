import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ Creates a database connection to the Monster database.
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_ogre_data(conn, **attributes):
    """
    Insert new Ogre data.
    :param conn: the Connection object
    :param attributes: a dictionary containing attribute names and corresponding data
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO ogre ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()

def insert_gremlin_data(conn, **attributes):
    """
    Insert new Gremlin data.
    :param conn: the Connection object
    :param attribute_type: the type of attribute to insert data into
    :param data: the data to insert for the specified attribute
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO gremlin ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_skeleton_data(conn, **attributes):
    """
    Insert new Gremlin data.
    :param conn: the Connection object
    :param attribute_type: the type of attribute to insert data into
    :param data: the data to insert for the specified attribute
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO skeleton ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def update_ogre_data(conn, monster_name, attribute_type, data):
    """
    Update Ogre data.
    :param conn: the Connection object
    :param monster_name: the name of the Ogre
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE ogre
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()


def update_gremlin_data(conn, monster_name, attribute_type, data):
    """
    Update Gremlin data.
    :param conn: the Connection object
    :param monster_name: the name of the Gremlin
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE gremlin
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()


def update_skeleton_data(conn, monster_name, attribute_type, data):
    """
    Update Skeleton data.
    :param conn: the Connection object
    :param monster_name: the name of the Skeleton
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE skeleton
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()
