from DungeonCharacter import DungeonCharacter
from abc import ABC, abstractmethod


class Monster(DungeonCharacter, ABC):
    """ Monster class inherits from DungeonCharacter and is an abstract base class.

    All subclasses of Monster must implement its abstract methods."""

    def __init__(self, heal_points, chance_to_heal):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage, max_damage)
        self._heal_points = heal_points
        self._chance_to_heal = chance_to_heal
        self._has_fainted = False

    @property
    def heal_points(self):
        """ returns current value (int) of Monster's current hit points """
        return self._heal_points

    @property
    def has_fainted(self):
        """ returns True if Monster has fainted, False if not """
        return self._has_fainted

    @property
    def chance_to_heal(self):
        """ chance a Monster has to heal after an attack if Monster has not fainted """
        return self._chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        self._chance_to_heal = value

    @has_fainted.setter
    def has_fainted(self, value):
        self._has_fainted = value

    @abstractmethod
    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
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
        """ Getter that returns the Ogre's current heal point """
        return super().heal_points

    @property
    def has_fainted(self):
        """ Getter that returns True if Ogre has fainted, False if not """
        return super().has_fainted

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """ Returns the chance to heal  """
        super().__setattr__('chance_to_heal', value)

    @heal_points.setter
    def heal_points(self, value):
        """ sets the Monsters heal points """
        super().__setattr__('heal_points', value)

    @has_fainted.setter
    def has_fainted(self, value):
        """ changes the Boolean value of self._has_fainted """
        super().__setattr__('has_fainted', value)

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
        if not super().has_fainted:
            # Check the chance to heal --> database
            # Check the minimum and maximum range of heal points for Ogre --> database
            # Restore hit points to maximum --> database
            pass
        else:
            print("The Ogre has fainted and can't heal itself!")

    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass

    def can_attack(self):
        """ abstract method for can_attack method used in subclasses """
        pass

    def attack(self, opponent):
        """ abstract method for attack method used in subclasses """
        # After an attack and loss of hit points, check to see if Monster fainted
        # No? Then check chance to heal
        pass

    def calculate_damage(self, damage):
        """ abstract method for calculate_damage method used in subclasses """
        pass


class Gremlin(Monster):
    @property
    def heal_points(self):
        """ Getter that returns the Ogre's current heal point """
        return super().heal_points

    @property
    def has_fainted(self):
        """ Getter that returns True if Ogre has fainted, False if not """
        return super().has_fainted

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """ Returns the chance to heal  """
        super().__setattr__('chance_to_heal', value)

    @heal_points.setter
    def heal_points(self, value):
        """ sets the Monsters heal points """
        super().__setattr__('heal_points', value)

    @has_fainted.setter
    def has_fainted(self, value):
        """ changes the Boolean value of self._has_fainted """
        super().__setattr__('has_fainted', value)

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
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
        """ Getter that returns the Ogre's current heal point """
        return super().heal_points

    @property
    def has_fainted(self):
        """ Getter that returns True if Ogre has fainted, False if not """
        return super().has_fainted

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """ Returns the chance to heal  """
        super().__setattr__('chance_to_heal', value)

    @heal_points.setter
    def heal_points(self, value):
        """ sets the Monsters heal points """
        super().__setattr__('heal_points', value)

    @has_fainted.setter
    def has_fainted(self, value):
        """ changes the Boolean value of self._has_fainted """
        super().__setattr__('has_fainted', value)

    def heal(self):
        """ based on chance to heal and then range of heal points for the monster """
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
