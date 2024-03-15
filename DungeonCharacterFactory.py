from Monster import Monster
from Hero import Warrior, Priestess, Thief
import query_database


class DungeonCharacterFactory:
    """
    Creates and returns Dungeon Characters for Dungeon Adventure 2.0.
    All Dungeon Characters should be created via the DungeonCharacterFactory.

    Contains one method, create_character, which returns either a Hero (Warrior, Priestess, Thief) or a Monster.
    """

    @staticmethod
    def create_character(table_name, character_name):
        """
        Static method that returns Dungeon Character objects. Queries the Dungeon Character SQLite database
        and passes parameter data required to create an instance of Monster, Warrior, Priestess, or Thief.
        :param table_name: the name of the table to query
        :param character_name: name of character that corresponds to database information
        :return: the Dungeon Character object (Monster, Warrior, Priestess, Thief).
        """
        conn = query_database.create_connection("dungeon_character_db.sqlite")
        if table_name.lower() == "warrior":
            warrior_data = query_database.select_row(conn, table_name, character_name)
            return Warrior(**warrior_data)
        elif table_name.lower() == "priestess":
            priestess_data = query_database.select_row(conn, table_name, character_name)
            return Priestess(**priestess_data)
        elif table_name.lower() == "thief":
            thief_data = query_database.select_row(conn, table_name, character_name)
            return Thief(**thief_data)
        elif table_name.lower() == "ogre":
            monster_type = table_name
            ogre_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **ogre_data)
        elif table_name.lower() == "gremlin":
            monster_type = table_name
            gremlin_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **gremlin_data)
        elif table_name.lower() == "skeleton":
            monster_type = table_name
            skeleton_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **skeleton_data)
        elif table_name.lower() == "troll":
            monster_type = table_name
            troll_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **troll_data)
        elif table_name.lower() == "chimera":
            monster_type = table_name
            chimera_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **chimera_data)
        elif table_name.lower() == "dragon":
            monster_type = table_name
            dragon_data = query_database.select_row(conn, table_name, character_name)
            return Monster(monster_type, **dragon_data)
        else:
            raise ValueError("Invalid Dungeon Character type")
