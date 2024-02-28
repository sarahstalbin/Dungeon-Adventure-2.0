import sqlite3
from sqlite3 import Error

""" Establishes connection and setup to Monster SQLite Database """


def create_connection(db_file):
    """ Creates a database connection to the Monster database.
    :param db_file: database file
    :return: Connection object or None"""
    conn = None
    try:
        # Pass a string that is the name of the file we want to connect to
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return: None
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    """
    Create tables for Ogres, Gremlins, Skeletons, Dungeon Trolls, Chimeras, and Dragons.
    :return:
    """
    database = r"monster_db.sqlite"

    sql_create_ogre_table = """ CREATE TABLE IF NOT EXISTS ogre (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    sql_create_gremlin_table = """ CREATE TABLE IF NOT EXISTS gremlin (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    sql_create_skeleton_table = """ CREATE TABLE IF NOT EXISTS skeleton (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    sql_create_troll_table = """ CREATE TABLE IF NOT EXISTS troll (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    sql_create_chimera_table = """ CREATE TABLE IF NOT EXISTS chimera (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    sql_create_dragon_table = """ CREATE TABLE IF NOT EXISTS dragon (
                                    name TEXT,
                                    hit_points INTEGER,
                                    attack_speed INTEGER,
                                    chance_to_hit REAL,
                                    damage INTEGER,
                                    minimum_damage INTEGER,
                                    maximum_damage INTEGER,
                                    chance_to_heal REAL,
                                    minimum_heal_points INTEGER,
                                    maximum_heal_points INTEGER,
                                    heal_points INTEGER,
                                    has_fainted INTEGER
                            );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_ogre_table)
        create_table(conn, sql_create_gremlin_table)
        create_table(conn, sql_create_skeleton_table)
        create_table(conn, sql_create_troll_table)
        create_table(conn, sql_create_chimera_table)
        create_table(conn, sql_create_dragon_table)
    else:
        print("Error! Cannot create the database connection")


if __name__ == '__main__':
    main()
