from Monster_s import Monster
from Hero_s import Warrior, Priestess, Thief
import query_database


class DungeonCharacterFactory:
    """
    Creates and returns Dungeon Characters for Dungeon Adventure 2.0.
    All Dungeon Characters should be created via the DungeonCharacterFactory.

    Contains two methods: create_hero(), which creates a Hero, and create_monster(), which creates a Monster.
    """

    @staticmethod
    def create_character(table_name, character_name):
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


# w = DungeonCharacterFactory.create_character("warrior", "Warrior")
# p = DungeonCharacterFactory.create_character("priestess", "Priestess")
# t = DungeonCharacterFactory.create_character("thief", "Thief")
# o = DungeonCharacterFactory.create_character("ogre", "Throg")
# g = DungeonCharacterFactory.create_character("gremlin", "Spike")
# s = DungeonCharacterFactory.create_character("skeleton", "Rattlebones")
# tr = DungeonCharacterFactory.create_character("troll", "Ragnok")
# c = DungeonCharacterFactory.create_character("chimera", "Thrawn")
# d = DungeonCharacterFactory.create_character("dragon", "Fafnir")
#
# print(t)
# print(s)
# print(c)
# print(w)
