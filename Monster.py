import random
from DungeonCharacter import DungeonCharacter
from abc import ABC, abstractmethod
import sqlite_insert_update
import sqlite_query


class Monster(DungeonCharacter, ABC):
    """ Monster class inherits from DungeonCharacter and is an abstract base class.

    All subclasses of Monster must implement its abstract methods."""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, damage, min_damage, max_damage, chance_to_heal,
                 minimum_heal_points, maximum_heal_points, heal_points):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage,
                         max_damage)
        self._damage = damage
        self._chance_to_heal = chance_to_heal
        self._minimum_heal_points = minimum_heal_points
        self._maximum_heal_points = maximum_heal_points
        self._heal_points = heal_points
        self._has_fainted = False
        self._name = name
        self._conn = sqlite_insert_update.create_connection("monster_db.sqlite")

    def get_attribute(self, attribute):
        """
        Gets the data of the provided attribute
        :param attribute: the attribute whose data will be returned
        :return: the data of the provided attribute
        """
        return sqlite_query.select_monster_attribute(self._conn, self.__class__.__name__.lower(), attribute, self._name)

    def update_monster_data(self, attribute_type, data):
        """
        Sets (or updates) the data in the desired Monster attribute.
        :param attribute_type: the attribute type to be updated
        :param data: the data with which the attribute will be updated
        :return: None
        """
        if isinstance(self, Ogre):
            sqlite_insert_update.update_ogre_data(self._conn, self.name, attribute_type, data)
        elif isinstance(self, Gremlin):
            sqlite_insert_update.update_gremlin_data(self._conn, self.name, attribute_type, data)
        elif isinstance(self, Skeleton):
            sqlite_insert_update.update_skeleton_data(self._conn, self.name, attribute_type, data)
        elif isinstance(self, Troll):
            sqlite_insert_update.update_troll_data(self._conn, self.name, attribute_type, data)
        elif isinstance(self, Chimera):
            sqlite_insert_update.update_chimera_data(self._conn, self.name, attribute_type, data)
        elif isinstance(self, Dragon):
            sqlite_insert_update.update_dragon_data(self._conn, self.name, attribute_type, data)
        else:
            print("Unknown Monster type")

    def get_random_heal_points(self):
        """ Returns a random integer between the range of a Monsters minimum and maximum heal points """
        min_heal_points = self.minimum_heal_points
        max_heal_points = self.maximum_heal_points
        return random.randint(min_heal_points, max_heal_points)

    def get_damage(self):
        """ Returns random amount of damage to Monster """
        min_damage = self.minimum_damage
        max_damage = self.maximum_damage
        return random.randint(min_damage, max_damage)

    def can_attack(self):
        """ Returns the chance of a Monster attacking """
        chance_to_hit = self.chance_to_hit
        return random.random() < chance_to_hit

    def calculate_damage(self, damage):
        """ Decrements Monster's hit point count after damage is incurred """
        previous_hit_points = self.hit_points
        updated_hit_points = previous_hit_points - damage
        self.update_monster_data("hit_points", updated_hit_points)

    def faint(self):
        """ Changes Monster's has_fainted boolean to True when below minimum hit point count """
        self.has_fainted = True

    @property
    def name(self):
        """ Returns Monster's name """
        return self.get_attribute("name")

    @name.setter
    def name(self, new_name):
        """ Sets new name """
        if isinstance(new_name, str):
            self.update_monster_data("name", new_name)
        else:
            raise ValueError("name must be a string")

    @property
    def hit_points(self):
        """ Returns current hit point count """
        return self.get_attribute("hit_points")

    @hit_points.setter
    def hit_points(self, value):
        """ Sets new hit point value """
        if isinstance(value, int):
            self.update_monster_data("hit_points", value)
        else:
            raise ValueError("hit_points value must be an int")

    @property
    def attack_speed(self):
        """ Returns attack speed """
        return self.get_attribute("attack_speed")

    @attack_speed.setter
    def attack_speed(self, value):
        """ Sets new attack speed """
        if isinstance(value, int):
            self.update_monster_data("attack_speed", value)
        else:
            raise ValueError("attack_speed value must be an int")

    @property
    def chance_to_hit(self):
        """ Returns chance to hit """
        return self.get_attribute("chance_to_hit")

    @chance_to_hit.setter
    def chance_to_hit(self, value):
        """ Sets new chance to hit percentage """
        if isinstance(value, float):
            self.update_monster_data("chance_to_hit", value)
        else:
            raise ValueError("chance_to_hit value must be a float")

    @property
    def damage(self):
        """ Returns damage value """
        return self.get_attribute("damage")

    @damage.setter
    def damage(self, value):
        """ Sets new damage value """
        if isinstance(value, int):
            self.update_monster_data("damage", value)
        raise ValueError("damage value must be an int")

    @property
    def minimum_damage(self):
        """ Returns minimum damage value """
        return self.get_attribute("minimum_damage")

    @minimum_damage.setter
    def minimum_damage(self, value):
        """ Sets new minimum damage value """
        if isinstance(value, int):
            self.update_monster_data("minimum_damage", value)
        else:
            raise ValueError("minimum_damage value must be an int")

    @property
    def maximum_damage(self):
        """ Returns maximum damage """
        return self.get_attribute("maximum_damage")

    @maximum_damage.setter
    def maximum_damage(self, value):
        """ Sets new maximum damage value """
        if isinstance(value, int):
            self.update_monster_data("maximum_damage", value)
        else:
            raise ValueError("maximum_damage value must be an int")

    @property
    def chance_to_heal(self):
        """ Returns chance to heal """
        return self.get_attribute("chance_to_heal")

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """ Sets new chance to heal percentage """
        if isinstance(value, float):
            self.update_monster_data("chance_to_heal", value)
        else:
            raise ValueError("chance_to_heal value must be a float")

    @property
    def minimum_heal_points(self):
        """ Returns current minimum heal point value """
        return self.get_attribute("minimum_heal_points")

    @minimum_heal_points.setter
    def minimum_heal_points(self, value):
        """ Sets new minimum heal point value """
        if isinstance(value, int):
            self.update_monster_data("minimum_heal_points", value)
        else:
            raise ValueError("minimum_heal_points value must be an int")

    @property
    def maximum_heal_points(self):
        """ Returns current maximum heal point value"""
        return self.get_attribute("maximum_heal_points")

    @maximum_heal_points.setter
    def maximum_heal_points(self, value):
        """ Sets new maximum heal point value """
        if isinstance(value, int):
            self.update_monster_data("maximum_heal_points", value)
        else:
            raise ValueError("maximum_heal_points value must be an int")

    @property
    def heal_points(self):
        """ Returns current heal point value """
        return self.get_attribute("heal_points")

    @heal_points.setter
    def heal_points(self, value):
        """ Sets new heal point value"""
        if isinstance(value, int):
            self.update_monster_data("heal_points", value)
        else:
            raise ValueError("heal_point value must be an int")

    @property
    def has_fainted(self):
        """ Returns the status of whether a Monster has fainted or not (boolean) """
        return self.get_attribute("has_fainted")

    @has_fainted.setter
    def has_fainted(self, boolean):
        """ Updates the Monster's fainting status """
        if isinstance(boolean, bool):
            self._has_fainted = boolean
            self.update_monster_data("has_fainted", boolean)
        else:
            raise ValueError("has_fainted must be a boolean value")

    @abstractmethod
    def heal(self):
        """ Abstract method based on chance to heal and then range of heal points for the monster """
        pass

    @abstractmethod
    def attack(self, opponent):
        """ Abstract method for attack method used in subclasses """
        pass


class Ogre(Monster):

    def __init__(self, name):

        """ Creates an instance of an Ogre. Attributes are added to the Monster database. """
        super().__init__(name, 200, 2, 0.6, 0, 30, 60,
                         0.1, 30, 60, 60)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_ogre_data(conn,
                                              name=name, hit_points=200, attack_speed=2, chance_to_hit=0.6,
                                              damage=0, minimum_damage=30, maximum_damage=60,
                                              chance_to_heal=0.1, minimum_heal_points=30, maximum_heal_points=60,
                                              heal_points=60, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        if self.can_attack():
            print(f"The Ogre {self.name} is attacking {opponent.hero_name}")
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"{self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals Ogre based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Ogre {self.name} has healed itself!")
        else:
            print(f"The Ogre {self.name} cannot heal itself, you're safe!")


class Gremlin(Monster):

    def __init__(self, name):
        """ Creates an instance of a Gremlin. Attributes are added to the Monster database. """
        super().__init__(name, 70, 5, 0.8, 0, 15, 30,
                         0.4, 20, 40, 40)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_gremlin_data(conn,
                                                 name=name, hit_points=70, attack_speed=5, chance_to_hit=0.8,
                                                 damage=0, minimum_damage=15, maximum_damage=30,
                                                 chance_to_heal=0.4, minimum_heal_points=20, maximum_heal_points=40,
                                                 heal_points=40, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        print(f"{self.name} is attacking {opponent.hero_name}")
        if self.can_attack():
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"{self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals Gremlin based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Gremlin {self.name} has healed itself!")
        else:
            print(f"The Gremlin {self.name} cannot heal itself, you're safe!")


class Skeleton(Monster):

    def __init__(self, name):
        """ Creates an instance of a Skeleton. Attributes are added to the Monster database. """
        super().__init__(name, 100, 3, 0.8, 0, 30, 50,
                         0.3, 30, 50, 50)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_skeleton_data(conn,
                                                  name=name, hit_points=100, attack_speed=3, chance_to_hit=0.8,
                                                  damage=0, minimum_damage=30, maximum_damage=50,
                                                  chance_to_heal=0.3, minimum_heal_points=30, maximum_heal_points=50,
                                                  heal_points=50, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        print(f"{self.name} is attacking {opponent.hero_name}")
        if self.can_attack():
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"{self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals Skeleton based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Skeleton {self.name} has healed itself!")
        else:
            print(f"The Skeleton {self.name} cannot heal itself, you're safe!")


class Troll(Monster):
    def __init__(self, name):
        """ Creates an instance of a Dragon. Attributes are added to the Monster database. """
        super().__init__(name, 850, 4, 0.9, 0, 40, 200,
                         0.7, 50, 100, 100)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_troll_data(conn,
                                                 name=name, hit_points=850, attack_speed=4, chance_to_hit=0.9,
                                                 damage=0, minimum_damage=40, maximum_damage=200,
                                                 chance_to_heal=0.7, minimum_heal_points=50, maximum_heal_points=100,
                                                 heal_points=100, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        print(f"The Troll {self.name} is attacking {opponent.hero_name}")
        if self.can_attack():
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"The Troll {self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals Troll based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Troll {self.name} has healed itself! Watch out!")
        else:
            print(f"You defeated the Troll {self.name}! You win!")


class Chimera(Monster):
    def __init__(self, name):
        """ Creates an instance of a Dragon. Attributes are added to the Monster database. """
        super().__init__(name, 800, 8, 0.9, 0, 45, 180,
                         0.5, 50, 100, 100)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_chimera_data(conn,
                                                 name=name, hit_points=800, attack_speed=8, chance_to_hit=0.9,
                                                 damage=0, minimum_damage=45, maximum_damage=180,
                                                 chance_to_heal=0.5, minimum_heal_points=50, maximum_heal_points=100,
                                                 heal_points=100, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        print(f"The Chimera {self.name} is attacking {opponent.hero_name}")
        if self.can_attack():
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"The Chimera {self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals the Chimera based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Chimera {self.name} has healed itself! Watch out!")
        else:
            print(f"You defeated the Chimera {self.name}! You win!")


class Dragon(Monster):

    def __init__(self, name):
        """ Creates an instance of a Dragon. Attributes are added to the Monster database. """
        super().__init__(name, 1000, 7, 0.9, 0, 50, 200,
                         0.75, 50, 100, 100)
        conn = sqlite_insert_update.create_connection("monster_db.sqlite")
        sqlite_insert_update.insert_dragon_data(conn,
                                                name=name, hit_points=1000, attack_speed=7, chance_to_hit=0.9,
                                                damage=0, minimum_damage=40, maximum_damage=200,
                                                chance_to_heal=0.6, minimum_heal_points=50, maximum_heal_points=100,
                                                heal_points=100, has_fainted=False)

    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        print(f"The Dragon {self.name} is attacking {opponent.hero_name}")
        if self.can_attack():
            damage = self.get_damage()
            self.calculate_damage(damage)
            print(f"The Dragon {self.name} attacks {opponent.hero_name} for {damage} damage points")
            return True

    def heal(self):
        """ Heals the Dragon based on chance to heal within range of its min/max heal points """
        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            print(f"The Dragon {self.name} has healed itself! Watch out!")
        else:
            print(f"You defeated the Dragon {self.name}! You win!")
