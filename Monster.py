from DungeonCharacter import DungeonCharacter
from abc import ABC, abstractmethod


class Monster(DungeonCharacter, ABC):
    """ Monster class inherits from DungeonCharacter and is an abstract base class.

    All subclasses of Monster must implement its abstract methods."""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage, max_damage, heal_points, has_fainted):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage, max_damage, heal_points, has_fainted)
        self.__heal_points = 0
        self.__has_fainted = False

    @abstractmethod
    @property
    def heal_points(self):
        pass

    @abstractmethod
    @property
    def has_fainted(self):
        pass

    @abstractmethod
    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
        pass

    @abstractmethod
    def chance_to_heal(self):
        """ chance a Monster has to heal after an attack if Monster has not fainted """
        pass

    @abstractmethod
    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass

    @abstractmethod
    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        pass

    @abstractmethod
    def attack(self, opponent):
        """ abstract method for attack method used in subclasses """
        pass

    @abstractmethod
    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in subclasses """
        pass


class Ogre(Monster):

    @property
    def heal_points(self):
        return self._Monster__heal_points

    @property
    def has_fainted(self):
        return self._Monster__has_fainted

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
        pass

    def chance_to_heal(self):
        """ chance a Monster has to heal after an attack if Monster has not fainted """
        pass

    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass

    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        pass

    def attack(self, opponent):
        """ abstract method for attack method used in subclasses """
        pass

    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in subclasses """
        pass


class Gremlin(Monster):
    @property
    def heal_points(self):
        return self._Monster__heal_points

    @property
    def has_fainted(self):
        return self._Monster__has_fainted

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
        pass

    def chance_to_heal(self):
        """ chance a Monster has to heal after an attack if Monster has not fainted """
        pass

    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass

    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        pass

    def attack(self, opponent):
        """ abstract method for attack method used in subclasses """
        pass

    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in subclasses """
        pass


class Skeleton(Monster):
    @property
    def heal_points(self):
        return self._Monster__heal_points

    @property
    def has_fainted(self):
        return self._Monster__has_fainted

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
        pass

    def chance_to_heal(self):
        """ chance a Monster has to heal after an attack if Monster has not fainted """
        pass

    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass

    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        pass

    def attack(self, opponent):
        """ abstract method for attack method used in subclasses """
        pass

    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in subclasses """
        pass
