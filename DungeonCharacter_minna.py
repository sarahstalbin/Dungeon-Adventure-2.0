from abc import ABC, abstractmethod
import random


class DungeonCharacter(ABC):
    """ DungeonCharacter class is an abstract class used to override methods in Hero and Monster subclasses"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage):

        # self.stats = {"Name": name, "Hit Points": hit_points, "Attack Speed": attack_speed,
        #               "Chance to Hit": chance_to_hit, "Min Damage": min_damage,
        #               "Max Damage": max_damage}
        self._name = name
        self._hit_points = hit_points
        self._attack_speed = attack_speed
        self._chance_to_hit = chance_to_hit
        self._min_damage = min_damage
        self._max_damage = max_damage

    # @abstractmethod

    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        # chance_to_hit = self.chance_to_hit
        return random.random() < self._chance_to_hit

    # @abstractmethod
    def attack(self, opponent):
        """ Attacks and causes damage to a Hero """
        # if isinstance(opponent, Hero) --> not sure where to put this method
        print(f"The {self._name} is attacking {opponent.name}")
        print(f"The {self._name} hitpoints is {self._hit_points} and the {opponent.name} is {opponent.hit_points}")
        print(self)
        print(opponent)
        if self.can_attack():
            damage = self.get_damage()
            self._hit_points -= damage
            # self.calculate_damage(damage)
            print(f"The {self._name} attacks {opponent._name} for {damage} damage points")
            print(f"The {self._name} hitpoints is {self._hit_points} and the {opponent.name} is {opponent.hit_points}")
            return True
        else:
            print(f" {self._name} couldn't attack {opponent.name}  ")
            print(f"The {self._name} hitpoints is {self._hit_points} and the {opponent.name} is {opponent.hit_points}")
        return False  # else return False

    # @abstractmethod
    # def calculate_damage(self, damage):
    #     """ abstract method for calculate_damage method used in subclasses """
    #     if isinstance(damage, int) and damage >= 0:
    #         self._hit_points -= damage
    #     raise ValueError("damage value must be an int")

    @abstractmethod
    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass
