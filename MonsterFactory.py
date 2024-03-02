from Monster import Ogre, Gremlin, Skeleton, Troll, Chimera, Dragon


class MonsterFactory:
    """
    Creates and returns Monster objects for Dungeon Adventure 2.0.
    All Monsters should be created via the MonsterFactory.

    Contains one method: create_monster(), which creates a Monster object of a specified type using relevant data for
    creating that Monster.

    """

    @staticmethod
    def create_monster(monster_type, name):
        """
        Creates an instance of a Monster.
        :param monster_type: the type of Monster to create.
        :param name: the name of the Monster.
        :return: the Monster object.
        """
        if monster_type.lower() == "ogre":
            return Monster.Ogre(name)
        elif monster_type.lower() == "gremlin":
            return Monster.Gremlin(name)
        elif monster_type.lower() == "skeleton":
            return Monster.Skeleton(name)
        elif monster_type.lower() == "troll":
            return Monster.Troll(name)
        elif monster_type.lower() == "chimera":
            return Monster.Chimera(name)
        elif monster_type.lower() == "dragon":
            return Monster.Dragon(name)
        else:
            raise ValueError("Invalid monster type.")
