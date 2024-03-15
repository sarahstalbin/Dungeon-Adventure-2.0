from abc import ABC
import random


class DungeonCharacter(ABC):
    """ DungeonCharacter class is an abstract class used to override methods in Hero and Monster subclasses"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                 maximum_damage):
        self._name = name
        self._hit_points = hit_points
        self._attack_speed = attack_speed
        self._chance_to_hit = chance_to_hit
        self._minimum_damage = minimum_damage
        self._maximum_damage = maximum_damage

    def can_attack(self):
        """ Returns the chance of a Dungeon Character attacking """
        return random.random() < self.chance_to_hit

    def attack(self, opponent):
        result = {"attacker": self.name, "opponent": opponent.name, "success": False, "damage": 0}

        if self.can_attack():
            damage = self.get_damage()
            opponent.calculate_damage(damage)

            result["success"] = True
            result["damage"] = damage

        return result

    def calculate_damage(self, damage):
        """ Decrements Character's hit point count after damage is incurred """
        if isinstance(damage, int):
            previous_hit_points = self.hit_points
            updated_hit_points = previous_hit_points - damage
            if updated_hit_points <= 0:
                self.hit_points = 0
            else:
                self.hit_points = updated_hit_points
        else:
            raise ValueError("Damage must be an integer")

    def get_damage(self):
        """ Returns random amount of damage to Dungeon Character """
        min_damage = self.minimum_damage
        max_damage = self.maximum_damage
        return random.randint(min_damage, max_damage)

    @property
    def name(self):
        """ Returns Monster's name """
        return self._name

    @name.setter
    def name(self, new_name):
        """ Sets new name """
        # No empty string (check)
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hit_points(self):
        """ Returns current hit point count """
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        """ Sets new hit point value """
        if isinstance(value, int) and value >= 0:
            self._hit_points = value
        else:
            raise ValueError("hit_points value must be an int greater than zero")

    @property
    def attack_speed(self):
        """ Returns attack speed """
        return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value):
        """ Sets new attack speed """
        if isinstance(value, int) and value > 0:
            self._attack_speed = value
        else:
            raise ValueError("attack_speed value must be an int")

    @property
    def chance_to_hit(self):
        """ Returns chance to hit """
        return self._chance_to_hit

    @chance_to_hit.setter
    def chance_to_hit(self, value):
        """ Sets new chance to hit percentage """
        if isinstance(value, float) and value > 0:
            self._chance_to_hit = value
        else:
            raise ValueError("chance_to_hit value must be a float")

    @property
    def minimum_damage(self):
        """ Returns minimum damage value """
        return self._minimum_damage

    @minimum_damage.setter
    def minimum_damage(self, value):
        """ Sets new minimum damage value """
        if isinstance(value, int) and value > 0:
            self._minimum_damage = value
        else:
            raise ValueError("minimum_damage value must be an int")

    @property
    def maximum_damage(self):
        """ Returns maximum damage """
        return self._maximum_damage

    @maximum_damage.setter
    def maximum_damage(self, value):
        """ Sets new maximum damage value """
        if isinstance(value, int) and value > self.minimum_damage:
            self._maximum_damage = value
        else:
            raise ValueError("maximum_damage value must be an int")

