from DungeonCharacter_new import DungeonCharacter
from abc import ABC, abstractmethod
import random


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage, chance_to_block, h_potion_ct, v_potion_ct, pillar_ct):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage,
                         max_damage)
        # self._chance_to_block = chance_to_block

        self.stats["chance_to_block"] = chance_to_block
        self.stats["health_potion_count"] = h_potion_ct
        self.stats["vision_potion_count"] = v_potion_ct
        self.stats["pillar_count"] = pillar_ct

    @abstractmethod
    def hero_name(self):
        """
        abstract method for hero_name method used in child classes
        """
        pass

    @abstractmethod
    def hit_points(self):
        """
        abstract method for get_hit-points method used in child classes
        """
        pass

    @abstractmethod
    def healing_potion_count(self):
        """
        abstract method for healing potion count method used in child classes
        """
        pass

    @abstractmethod
    def vision_potion_count(self):
        """
        abstract method for vision potion count method used in child classes
        """
        pass

    @abstractmethod
    def pillar_count(self):
        """
        abstract method for pillar count method used in child classes
        """
        pass

    @abstractmethod
    def can_attack(self):
        """ abstract method for can_attack method used in child classes """
        pass

    @abstractmethod
    def attack(self, opponent):
        """ abstract method for attack method used in child classes """
        pass

    @abstractmethod
    def get_damage(self):
        """ abstract method for get_damage method used in child classes """
        pass

    @abstractmethod
    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in child classes """
        pass

    @abstractmethod
    def special_skill(self, opponent):
        """ abstract method for special_skill method used in child classes """
        pass


class Warrior(Hero):
    """ Warrior class is the child class of Hero """

    def __init__(self):
        super().__init__("Warrior", 125, 4, 0.8, 35, 60,
                         0.2, 0, 0, 0)

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

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

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.hero_name} is battling against {opponent.hero_name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.hero_name} attacks {opponent.hero_name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.hero_name} couldn't attack {opponent.hero_name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Warrior's special skill """
        if random.random() < 0.4:  # 40% chance for Crushing Blow
            damage = random.randint(75, 175)  # causes damage for 75 to 175 points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            print(f"{self.hero_name} performs a Crushing Blow for {damage} damage.")
        else:
            print(f"{self.hero_name} couldn't perform Crushing Blow")


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def __init__(self):
        super().__init__("Priestess", 75, 5, 0.7, 25, 45,
                         0.3, 0, 0, 0)

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

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
    def vision_potion_count(self, v_potion):
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

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.hero_name} is battling against {opponent.hero_name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.hero_name} attacks {opponent.hero_name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.hero_name} couldn't attack {opponent.hero_name}  ")
            return False  # else return False

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

    def __str__(self):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

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
    def vision_potion_count(self, v_potion):
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

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.hero_name} is battling against {opponent.hero_name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.hero_name} attacks {opponent.hero_name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.hero_name} couldn't attack {opponent.hero_name}  ")
            return False  # else return False

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
o = Thief()
p = Priestess()
w.attack(p)
o.attack(w)
p.attack(o)
