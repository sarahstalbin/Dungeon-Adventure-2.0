from DungeonCharacter_s import DungeonCharacter
from abc import ABC, abstractmethod
import random


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                 maximum_damage, chance_to_block, healing_potion_count, vision_potion_count, pillar_count):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                         maximum_damage)
        self._chance_to_block = chance_to_block
        self._healing_potion_count = healing_potion_count
        self._vision_potion_count = vision_potion_count
        self._pillar_count = pillar_count

    def __str__(self):
        """
        Returns a string representation of the Hero class.
        :return: string
        """
        hero_info = ""
        hero_info += f"{self.name}\n"
        hero_info += f"Hit Points: {self.hit_points}\n"
        hero_info += f"Attack Speed: {self.attack_speed}\n"
        hero_info += f"Chance to Hit: {self.chance_to_hit}\n"
        hero_info += f"Minimum Damage: {self.minimum_damage}\n"
        hero_info += f"Maximum Damage: {self.maximum_damage}\n"
        hero_info += f"Chance to Block: {self.chance_to_block}\n"
        hero_info += f"Healing Potion Count: {self.healing_potion_count}\n"
        hero_info += f"Vision Potion Count: {self.vision_potion_count}\n"
        hero_info += f"Pillar Count: {self.pillar_count}\n"

        return hero_info

    @abstractmethod
    def special_skill(self, opponent):
        """ Abstract method to be tailored and implemented by child classes """
        pass
    @property
    def chance_to_block(self):
        """ Returns the chance to block """
        return self._chance_to_block

    @chance_to_block.setter
    def chance_to_block(self, chance_to_block):
        """ Sets new chance to block """
        if isinstance(chance_to_block, float) and chance_to_block > 0:
            self._chance_to_block = chance_to_block
        else:
            raise ValueError("Chance to block must be a float")

    @property
    def pillar_count(self):
        """ Returns pillar count """
        return self._pillar_count

    @pillar_count.setter
    def pillar_count(self, pillar_count):
        """ Sets new pillar count """
        if isinstance(pillar_count, int) and pillar_count > 0:
            self._pillar_count = pillar_count
        else:
            raise ValueError("Pillar count must be an integer")

    @property
    def vision_potion_count(self):
        return self._vision_potion_count

    @vision_potion_count.setter
    def vision_potion_count(self, vision_potion_count):
        """ Sets new vision potion count """
        if isinstance(vision_potion_count, int) and vision_potion_count > 0:
            self._vision_potion_count = vision_potion_count
        else:
            raise ValueError("Vision potion count must be an integer")

    @property
    def healing_potion_count(self):
        return self._healing_potion_count

    @healing_potion_count.setter
    def healing_potion_count(self, healing_potion_count):
        """ Sets new healing potion count """
        if isinstance(healing_potion_count, int) and healing_potion_count > 0:
            self._healing_potion_count = healing_potion_count
        else:
            raise ValueError("Healing potion count must be an integer")

class Warrior(Hero):
    """ Warrior class is the child class of Hero """

    def special_skill(self, opponent):
        """ This method is the Warrior's special skill """
        if random.random() < 0.4:  # 40% chance for Crushing Blow
            damage = random.randint(75, 175)  # causes damage for 75 to 175 points
            opponent.calculate_damage(damage)  # passes the damage points to calculate_damage method
            print(f"{self.name} performs a Crushing Blow for {damage} damage.")
        else:
            print(f"{self.name} couldn't perform Crushing Blow")


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def special_skill(self, opponent):
        """ This method is the Priestess special_skill"""
        heal = random.randint(25, 50)
        opponent.calculate_damage(-heal)  # heals the damage points
        print(f" {self.name} steals gains {heal} healing points from {opponent.name} ")
        self.hit_points = + heal
        print(f" {self.name} how has {self.hit_points} ")


class Thief(Hero):
    """ Thief class is the child class of Hero """

    def special_skill(self, opponent):
        """ This method is the Thief's special_skill """
        chance = random.random()
        if chance < 0.4:  # 40% chance for Surprise Attack
            self.attack(opponent)
            self.attack(opponent)
            print(f" {self.name} attacked twice")
        elif chance < 0.8:
            self.attack(opponent)
            print(f" {self.name} attacked once")
        else:
            print(f"{self.name} couldn't attack")


