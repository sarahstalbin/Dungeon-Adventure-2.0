import random
from DungeonCharacter import DungeonCharacter


class Monster(DungeonCharacter):
    """ Monster class inherits from DungeonCharacter and is used to create various Monsters for Dungeon Adventure
    2.0."""

    def __init__(self, monster_type, name, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage,
                 chance_to_heal, minimum_heal_points, maximum_heal_points, heal_points, has_fainted):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, minimum_damage,
                         maximum_damage)
        self._monster_type = monster_type
        self._chance_to_heal = chance_to_heal
        self._minimum_heal_points = minimum_heal_points
        self._maximum_heal_points = maximum_heal_points
        self._heal_points = heal_points
        self._has_fainted = has_fainted
        self._name = name

    def __str__(self):
        """
        Returns a string representation of the Monster class.
        :return: string
        """
        monster_info = ""
        monster_info += f"{self.name}\n"
        monster_info += f"Hit Points: {self.hit_points}\n"
        monster_info += f"Heal Points: {self.heal_points}\n"
        monster_info += f"Attack Speed: {self.attack_speed}\n"
        monster_info += f"Chance to Hit: {self.chance_to_hit}\n"
        monster_info += f"Minimum Damage: {self.minimum_damage}\n"
        monster_info += f"Maximum Damage: {self.maximum_damage}\n"
        monster_info += f"Chance to Heal: {self.chance_to_heal}\n"
        monster_info += f"Minimum Heal Points: {self.minimum_heal_points}\n"
        monster_info += f"Maximum Heal Points: {self.maximum_heal_points}\n"
        monster_info += f"Heal Points: {self.heal_points}\n"
        if self.has_fainted():
            monster_info += f"Fainted: Yes\n"
        else:
            monster_info += f"Fainted: No\n"
        return monster_info

    def heal(self):
        """ Heals the Monster based on chance to heal within range of its min/max heal points """
        result = {"name": self.name, "success": False, "heal_amount": 0}
        # chance_to_heal = random.random() < self.chance_to_heal
        # heal_points = self.get_random_heal_points()  # Get random heal points to increment hit point count
        # has_fainted = self.has_fainted()  # Grab the has_fainted variable for reference
        # print(f"I am in heal and this is heal {chance_to_heal} and not fainted {has_fainted}")
        # if not has_fainted and chance_to_heal:  # If the monster has NOT fainted and chance_to_heal returned True
        #     print("we are a success")
        #     heal_amount = self.hit_points + heal_points
        #     self.hit_points = heal_amount  # Increment hit points by heal_points

        chance_to_heal = self.chance_to_heal
        heal_points = self.get_random_heal_points()
        has_fainted = self.has_fainted()

        if not has_fainted and chance_to_heal:
            hit_point_count = self.hit_points
            heal_amount = hit_point_count + heal_points
            self.hit_points = heal_amount
            result["success"] = True
            result["heal_amount"] = heal_amount
        return result

    def get_random_heal_points(self):
        """ Returns a random integer between the range of a Monster's minimum and maximum heal points """
        min_heal_points = self.minimum_heal_points
        max_heal_points = self.maximum_heal_points
        return random.randint(min_heal_points, max_heal_points)

    def faint(self):
        """ Changes Monster's has_fainted boolean to True when below minimum hit point count """
        self.has_fainted = True

    @property
    def chance_to_heal(self):
        """ Returns chance to heal """
        return self._chance_to_heal

    @chance_to_heal.setter
    def chance_to_heal(self, value):
        """ Sets new chance to heal percentage """
        if isinstance(value, float) and value > 0:
            self._chance_to_heal = value
        else:
            raise ValueError("chance_to_heal value must be a float")

    @property
    def minimum_heal_points(self):
        """ Returns current minimum heal point value """
        return self._minimum_heal_points

    @minimum_heal_points.setter
    def minimum_heal_points(self, value):
        """ Sets new minimum heal point value """
        if isinstance(value, int) and value > 0:
            self._minimum_heal_points = value
        else:
            raise ValueError("minimum_heal_points value must be an int")

    @property
    def maximum_heal_points(self):
        """ Returns current maximum heal point value"""
        return self._maximum_heal_points

    @maximum_heal_points.setter
    def maximum_heal_points(self, value):
        """ Sets new maximum heal point value """
        if isinstance(value, int) and value > self.minimum_heal_points:
            self._maximum_heal_points = value
        else:
            raise ValueError("maximum_heal_points value must be an int")

    @property
    def heal_points(self):
        """ Returns current heal point value """
        return self._heal_points

    @heal_points.setter
    def heal_points(self, value):
        """ Sets new heal point value"""
        if isinstance(value, int) and value > 0:
            self._heal_points = value
        else:
            raise ValueError("heal_point value must be an int")

    # @property
    # def has_fainted(self):
    #     """ Returns the status of whether a Monster has fainted or not (boolean) """
    #     return self._has_fainted

    # @has_fainted.setter
    def has_fainted(self):
        """ Updates the Monster's fainting status """
        if self.hit_points <= 0:
            self._has_fainted = True
        else:
            self._has_fainted = False
        return self._has_fainted
