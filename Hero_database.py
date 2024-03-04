from DungeonCharacter_new import DungeonCharacter
from abc import ABC, abstractmethod
import random
import insert_update_database_dc
import query_database_dc


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                 maximum_damage, chance_to_block, h_potion_ct, v_potion_ct, pillar_ct):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                         maximum_damage)
        # self._chance_to_block = chance_to_block

        self.stats["chance_to_block"] = chance_to_block
        self.stats["health_potion_count"] = h_potion_ct
        self.stats["vision_potion_count"] = v_potion_ct
        self.stats["pillar_count"] = pillar_ct
        self._conn = insert_update_database_dc.create_connection("dungeon_character_db.sqlite")
        self._name = name

    def get_attribute(self, attribute):
        """
        Gets the data of the provided attribute
        :param attribute: the attribute whose data will be returned
        :return: the data of the provided attribute
        """
        if isinstance(attribute, str):
            return query_database_dc.select_hero_attribute(self._conn, self.__class__.__name__.lower(), attribute,
                                                        self._name)
        else:
            raise ValueError("Attribute must be a string")

    def update_hero_data(self, attribute_type, data):
        """
        Sets (or updates) the data in the desired Monster attribute.
        :param attribute_type: the attribute type to be updated
        :param data: the data with which the attribute will be updated
        :return: None
        """
        if not isinstance(attribute_type, str):
            raise ValueError("Attribute type must be a string.")

        if not isinstance(data, (int, float, bool)):
            raise ValueError("Invalid data type")

        if isinstance(self, Warrior):
            insert_update_database_dc.update_warrior_data(self._conn, self._name, attribute_type, data)
        elif isinstance(self, Priestess):
            insert_update_database_dc.update_priestess_data(self._conn, self._name, attribute_type, data)
        elif isinstance(self, Thief):
            insert_update_database_dc.update_thief_data(self._conn, self._name, attribute_type, data)

        else:
            raise ValueError("Invalid hero type.")

    def get_damage(self):
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        self.stats["hit_points"] -= damage

    def can_attack(self):
        return random.random() < self.stats["chance_to_hit"]

    def attack(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "damage": 0}

        if self.can_attack():
            damage = self.get_damage()
            opponent.calculate_damage(damage)
            result["success"] = True
            result["damage"] = damage

        # self.view.display_attack_result(result)
        return result

    @property
    def hero_name(self):
        """
        returns player name
        """
        return self.stats["name"]

    @hero_name.setter
    def hero_name(self, name):
        """
        Sets character name
        """
        self.stats["name"] = name

    @property
    def hit_points(self):
        """
        returns character hit-points
        """
        return self.stats["hit_points"]

    @hit_points.setter
    def hit_points(self, hit_points):
        """
        Sets character hit-points
        """
        try:
            self.stats["hit_points"] = hit_points
        except ValueError:
            print("\nMust be an int.")

    @property
    def healing_potion_count(self):
        """
        returns healing potion count
        """
        return self.stats["h_potion_ct"]

    @healing_potion_count.setter
    def healing_potion_count(self, h_potion):
        """
        Sets vision potion count
        """
        try:
            self.stats["h_potion_ct"] = h_potion
        except ValueError:
            print("\nMust be an int.")

    @property
    def vision_potion_count(self):
        """
        return: int vision potion count
        """
        return self.stats["v_potion_ct"]

    @vision_potion_count.setter
    def vision_potion_count(self, v_potion=0):
        """
        Sets vision potion count
        """
        try:
            self.stats["v_potion_ct"] = v_potion
        except ValueError:
            print("\nMust be an int.")

    @property
    def pillar_count(self):
        """
        return: int pillar count
        """
        return self.stats["pillar_ct"]

    @pillar_count.setter
    def pillar_count(self, pillar):
        """
        Sets pillar count
        """
        try:
            self.stats["pillar_ct"] = pillar
        except ValueError:
            print("\nMust be an int.")

    @abstractmethod
    def special_skill(self, opponent):
        """ abstract method for special_skill method used in child classes """
        pass


class Warrior(Hero):
    """ Warrior class is the child class of Hero """

    def __init__(self):
        super().__init__("Warrior", 125, 4, 0.8, 35, 60,
                         0.2, 0, 0, 0)
        conn = insert_update_database_dc.create_connection("dungeon_character_db.sqlite")
        insert_update_database_dc.insert_warrior_data(conn,
                                                   name="Warrior", hit_points=125, attack_speed=4, chance_to_hit=0.8,
                                                   minimum_damage=35, maximum_damage=60,
                                                   chance_to_block=0.2, h_potion_ct=0, v_potion_ct=0, pillar_ct=0)

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def special_skill(self, opponent):
        """ This method is the Warrior's special skill """
        if random.random() < 0.4:  # 40% chance for Crushing Blow
            damage = random.randint(75, 175)  # causes damage for 75 to 175 points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            print(f"{self.hero_name} performs a Crushing Blow for {damage} damage.")
        else:
            print(f"{self.hero_name} couldn't perform Crushing Blow")

    # def special_skill(self, opponent):
    #     result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False}
    #
    #     if random.random() < 0.4:
    #         damage = random.randint(75, 175)
    #         opponent.calculate_damage(damage)
    #         result["success"] = True
    #         result["damage"] = damage
    #     #self.view.warrior_attack_result(result)
    #
    #     return result


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def __init__(self):
        super().__init__("Priestess", 75, 5, 0.7, 25, 45,
                         0.3, 0, 0, 0)
        conn = insert_update_database_dc.create_connection("dungeon_character_db.sqlite")
        insert_update_database_dc.insert_priestess_data(conn,
                                                     name="Priestess", hit_points=75, attack_speed=5, chance_to_hit=0.7,
                                                     min_damage=25, max_damage=45,
                                                     chance_to_block=0.3, h_potion_ct=0, v_potion_ct=0, pillar_ct=0)

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def special_skill(self, opponent):
        """ This method is the Priestess special_skill"""
        heal = random.randint(25, 50)
        opponent.calculate_damage(-heal)  # heals the damage points
        print(f" {self.hero_name} performs healing on {opponent.hero_name} for {heal} heal points ")


class Thief(Hero):
    """ Thief class is the child class of Hero """

    def __init__(self):
        super().__init__("Thief", 75, 6, 0.8, 20, 40,
                         0.4, 0, 0, 0)
        conn = insert_update_database_dc.create_connection("dungeon_character_db.sqlite")
        insert_update_database_dc.insert_thief_data(conn,
                                                 name="Thief", hit_points=75, attack_speed=6, chance_to_hit=0.8,
                                                 min_damage=20, max_damage=40,
                                                 chance_to_block=0.4, h_potion_ct=0, v_potion_ct=0, pillar_ct=0)

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def special_skill(self, opponent):
        """ This method is the Thief's special_skill """
        chance = random.random()
        if chance < 0.4:  # 40% chance for Surprise Attack
            self.attack(opponent)
            self.attack(opponent)
            print(f" {self.hero_name} attacked twice")
        elif chance < 0.8:
            self.attack(opponent)
            print(f" {self.hero_name} attacked once")
        else:
            print(f"{self.hero_name} couldn't attack")

# usage
w = Warrior()
# o = Thief()
# p = Priestess()
# w.special_skill(p)
# o.attack(w)
# p.attack(o)
