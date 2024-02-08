from DungeonCharacter import DungeonCharacter
from abc import ABC, abstractmethod
import random


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage, chance_to_block):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage,
                         max_damage)
        self._chance_to_block = chance_to_block

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
        super().__init__("Warrior", 125, 4, 0.8, 35, 60, 0.2)

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self._hit_points -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self._min_damage, self._max_damage)

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self._chance_to_hit  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self._name} is battling against {opponent._name}")
        if self.can_attack():  # if Warrior can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self._name} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self._name} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Warrior's special skill """
        if random.random() < 0.4:  # 40% chance for Crushing Blow
            damage = random.randint(75, 175)  # causes damage for 75 to 175 points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            print(f"{self._name} performs a Crushing Blow for {damage} damage.")
        else:
            print(f"{self._name} couldn't perform Crushing Blow")


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def __init__(self):
        super().__init__("Priestess", 75, 5, 0.7, 25, 45, 0.3)

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self._hit_points -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self._min_damage, self._max_damage)

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self._chance_to_hit  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        """ This method attacks the opponent and causes damage to the opponent"""
        print(f"{self._name} is battling against {opponent._name}")
        if self.can_attack():  # if Priestess can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self._name} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self._name} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Priestess special_skill"""
        heal = random.randint(25, 50)
        opponent.calculate_damage(-heal)  # heals the damage points


class Thief(Hero):
    """ Thief class is the child class of Hero """

    def __init__(self):
        super().__init__("Thief", 75, 6, 0.8, 20, 40, 0.4)

    def calculate_damage(self, damage):
        """ This method decrements hit_points to calculate damage """
        self._hit_points -= damage

    def get_damage(self):
        """ This method gets damage points """
        return random.randint(self._min_damage, self._max_damage)

    def can_attack(self):
        """ This method gives the chance or probability of chance_to_hit"""
        return random.random() < self._chance_to_hit  # random.random() generates a float value from 0 to 1

    def attack(self, opponent):
        print(f"{self._name} is battling against {opponent._name}")
        if self.can_attack():  # if Thief can attack
            damage = self.get_damage()  # gets minimum amd maximum damage points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            # and reduce the points of the opponent
            print(f" {self._name} attacks {opponent._name} for {damage} damage points")
            return True  # return True if the attack is successful

        else:
            print(f" {self._name} couldn't attack {opponent._name}  ")
            return False  # else return False

    def special_skill(self, opponent):
        """ This method is the Thief's special_skill """
        chance = random.random()
        if chance < 0.4:  # 40% chance for Surprise Attack
            self.attack(opponent)
            self.attack(opponent)
            print(f" {self._name} attacked twice")
        elif chance < 0.8:
            self.attack(opponent)
            print(f" {self._name} attacked once")
        else:
            print(f"{self._name} couldn't attack")


# usage
w = Warrior()
o = Thief()
w.attack(o)
