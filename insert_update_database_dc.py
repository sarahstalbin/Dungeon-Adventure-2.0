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
    :param attributes: the type of attribute to insert data into
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
    Insert new Skeleton data.
    :param conn: the Connection object
    :param attributes: the type of attribute to insert data into
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO skeleton ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_troll_data(conn, **attributes):
    """
    Insert new Troll data.
    :param conn: the Connection object
    :param attributes: the type of attribute to insert data into
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO troll ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_chimera_data(conn, **attributes):
    """
    Insert new Chimera data.
    :param conn: the Connection object
    :param attributes: the type of attribute to insert data into
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO chimera ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_dragon_data(conn, **attributes):
    """
    Insert new Dragon data.
    :param conn: the Connection object
    :param attributes: the type of attribute to insert data into
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO dragon ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_warrior_data(conn, **attributes):
    """
    Insert new Ogre data.
    :param conn: the Connection object
    :param attributes: a dictionary containing attribute names and corresponding data
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO warrior ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_priestess_data(conn, **attributes):
    """
    Insert new Ogre data.
    :param conn: the Connection object
    :param attributes: a dictionary containing attribute names and corresponding data
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO priestess ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, tuple(attributes.values()))
    conn.commit()


def insert_thief_data(conn, **attributes):
    """
    Insert new Ogre data.
    :param conn: the Connection object
    :param attributes: a dictionary containing attribute names and corresponding data
    :return: None
    """
    columns = ', '.join(attributes.keys())
    placeholders = ', '.join(['?'] * len(attributes))
    sql = f'INSERT INTO thief ({columns}) VALUES ({placeholders})'
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


def update_troll_data(conn, monster_name, attribute_type, data):
    """
    Update Dungeon Troll data.
    :param conn: the Connection object
    :param monster_name: the name of the Dungeon Troll
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE troll
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()


def update_chimera_data(conn, monster_name, attribute_type, data):
    """
    Update Chimera data.
    :param conn: the Connection object
    :param monster_name: the name of the Chimera
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE chimera
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()


def update_dragon_data(conn, monster_name, attribute_type, data):
    """
    Update Dragon data.
    :param conn: the Connection object
    :param monster_name: the name of the Dragon
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE dragon
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, monster_name))
    conn.commit()


def update_warrior_data(conn, hero_name, attribute_type, data):
    """
    Update Ogre data.
    :param conn: the Connection object
    :param hero_name: the name of the Ogre
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE warrior
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, hero_name))
    conn.commit()


def update_priestess_data(conn, hero_name, attribute_type, data):
    """
    Update Ogre data.
    :param conn: the Connection object
    :param hero_name: the name of the Ogre
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE priestess
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, hero_name))
    conn.commit()


def update_thief_data(conn, hero_name, attribute_type, data):
    """
    Update Ogre data.
    :param conn: the Connection object
    :param hero_name: the name of the Ogre
    :param attribute_type: the type of attribute to update
    :param data: the new data to update for the specified attribute
    """
    sql = f''' UPDATE thief
              SET {attribute_type} = ?
              WHERE name = ? '''
    cur = conn.cursor()
    cur.execute(sql, (data, hero_name))
    conn.commit()
