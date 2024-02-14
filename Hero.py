from DungeonCharacter_m import DungeonCharacter
from abc import ABC, abstractmethod
import random


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage, chance_to_block, h_potion_ct, v_potion_ct, pillar_ct):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage,
                         max_damage, h_potion_ct, v_potion_ct, pillar_ct)
        # self._chance_to_block = chance_to_block
        self.stats["chance_to_block"] = chance_to_block

    @abstractmethod
    def current_name(self, name):
        """
        abstract method for current_name method used in child classes
        """
        pass

    @abstractmethod
    def hit_points(self, hit_points):
        """ 
        abstract method for get_hit-points method used in child classes
        """
        pass

    @abstractmethod
    def healing_potion_count(self, h_potion):
        """
        abstract method for get_hit-points method used in child classes
        """
        pass

    @abstractmethod
    def vision_potion_count(self, v_potion):
        """
        abstract method for get_hit-points method used in child classes
        """
        pass

    @abstractmethod
    def pillar_count(self, pillar):
        """
        abstract method for get_hit-points method used in child classes
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
    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in child classes """
        pass

    @abstractmethod
    def get_damage(self):
        """ abstract method for get_damage method used in child classes """
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
        formatted_list = ["   " +str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def current_name(self, name):
        """
        Sets character name
        """
        self.stats["name"] = name


    def hit_points(self, hit_points):
        """
        Sets character hitpoints
        """
        self.stats["hit_points"] += hit_points

    def healing_potion_count(self, h_potion):
        """
        Sets healing potion count
        """
        self.stats["h_potion_ct"] += h_potion

    def vision_potion_count(self, v_potion):
        """
        Sets and gets vision potion count
        return: int vision potion count
        """
        self.stats["v_potion_ct"] += v_potion

    def pillar_count(self, pillar):
        """
        Sets and gets pillar count
        return: int pillar count
        """
        self.stats["pillar"] += pillar

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.stats["name"]} is battling against {opponent._name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.stats["name"]} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.stats["name"]} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Warrior's special skill """
        if random.random() < 0.4:  # 40% chance for Crushing Blow
            damage = random.randint(75, 175)  # causes damage for 75 to 175 points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            print(f"{self.stats["name"]} performs a Crushing Blow for {damage} damage.")
        else:
            print(f"{self.stats["name"]} couldn't perform Crushing Blow")


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def __init__(self):
        super().__init__("Priestess", 75, 5, 0.7, 25, 45,
                         0.3, 0, 0, 0)

    def __str__(self):
        formatted_list = ["   " +str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def current_name(self, name):
        """
        Sets character name
        """
        self.stats["name"] = name

    def hit_points(self, hit_points):
        """
        Sets character hitpoints
        """
        self.stats["hit_points"] += hit_points

    def healing_potion_count(self, h_potion):
        """
        Sets healing potion count
        """
        self.stats["h_potion_ct"] += h_potion

    def vision_potion_count(self, v_potion):
        """
        Sets and gets vision potion count
        return: int vision potion count
        """
        self.stats["v_potion_ct"] += v_potion

    def pillar_count(self, pillar):
        """
        Sets and gets pillar count
        return: int pillar count
        """
        self.stats["pillar"] += pillar

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.stats["name"]} is battling against {opponent._name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.stats["name"]} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.stats["name"]} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Priestess special_skill"""
        heal = random.randint(25, 50)
        opponent.calculate_damage(-heal)  # heals the damage points


class Thief(Hero):
    """ Thief class is the child class of Hero """

    def __init__(self):
        super().__init__("Thief", 75, 6, 0.8, 20, 40,
                         0.4, 0, 0, 0)

    def __str__(self):
        formatted_list = ["   " +str(item) + " : " + str(values) for item, values in self.stats.items()]
        return "\n" + "\n".join(formatted_list) + "\n"

    def current_name(self, name):
        """
        Sets character name
        """
        self.stats["name"] = name

    def hit_points(self, hit_points):
        """
        Sets character hitpoints
        """
        self.stats["hit_points"] += hit_points

    def healing_potion_count(self, h_potion):
        """
        Sets healing potion count
        """
        self.stats["h_potion_ct"] += h_potion

    def vision_potion_count(self, v_potion):
        """
        Sets and gets vision potion count
        return: int vision potion count
        """
        self.stats["v_potion_ct"] += v_potion

    def pillar_count(self, pillar):
        """
        Sets and gets pillar count
        return: int pillar count
        """
        self.stats["pillar"] += pillar

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self.stats["hit_points"] -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self.stats["chance_to_hit"]  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self.stats["name"]} is battling against {opponent._name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self.stats["name"]} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self.stats["name"]} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Thief's special_skill """
        chance = random.random()
        if chance < 0.4:  # 40% chance for Surprise Attack
            self.attack(opponent)
            self.attack(opponent)
            print(f" {self.stats["name"]} attacked twice")
        elif chance < 0.8:
            self.attack(opponent)
            print(f" {self.stats["name"]} attacked once")
        else:
            print(f"{self.stats["name"]} couldn't attack")


# usage
# w = Warrior()
# o = Thief()
# w.attack(o)