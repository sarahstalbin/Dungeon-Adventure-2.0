from abc import ABC, abstractmethod


class DungeonCharacter(ABC):
    """ DungeonCharacter class is an abstract class used to override methods in Hero and Monster subclasses"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage, h_potion_ct, v_potion_ct, pillar_ct):
        # self._name = name
        # self._hit_points = hit_points
        # self._attack_speed = attack_speed
        # self._chance_to_hit = chance_to_hit
        # self._min_damage = min_damage
        # self._max_damage = max_damage
        # self._h_potion_ct = h_potion_ct
        # self._v_potion_ct = v_potion_ct
        # self._pillar = pillar_ct

        self.stats = {"name": name, "hit_points": hit_points, "attack_speed": attack_speed,
                      "chance_to_hit": chance_to_hit, "min_damage": min_damage,
                      "max_damage": max_damage, "h_potion_ct": h_potion_ct, "v_potion_ct": v_potion_ct,
                      "pillar_ct": pillar_ct}

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

    @abstractmethod
    def get_damage(self):
        """ abstract method for get_damage method used in subclasses """
        pass
