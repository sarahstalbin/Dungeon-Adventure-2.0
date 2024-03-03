from DungeonCharacter import DungeonCharacter
from View import View
from abc import ABC, abstractmethod
import random


class Hero(DungeonCharacter, ABC):
    """ Hero class inherits from DungeonCharacter parent class, and it is an abstract base class"""

    def __init__(self, name, hit_points, attack_speed, chance_to_hit, min_damage,
                 max_damage, chance_to_block, h_potion_ct, v_potion_ct, pillar_ct):
        super().__init__(name, hit_points, attack_speed, chance_to_hit, min_damage,
                         max_damage, h_potion_ct, v_potion_ct, pillar_ct)

        #self.view = View()
        self.stats["chance_to_block"] = chance_to_block

    @abstractmethod
    def hero_name(self):
        pass

    @abstractmethod
    def hit_points(self):
        pass

    @abstractmethod
    def healing_potion_count(self):
        pass

    @abstractmethod
    def vision_potion_count(self):
        pass

    @abstractmethod
    def pillar_count(self):
        pass

    @abstractmethod
    def can_attack(self):
        pass

    @abstractmethod
    def attack(self, opponent):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def calculate_damage(self, damage):
        pass

    @abstractmethod
    def special_skill(self, opponent):
        pass


class Warrior(Hero):
    """ Warrior class is the child class of Hero """

    def __init__(self):
        super().__init__("Warrior", 125, 4, 0.8, 35, 60,
                         0.2, 0, 0, 0)

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
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        self.stats["hit_points"] -= damage

    def can_attack(self):
        return random.random() < self.stats["chance_to_hit"]

    def attack(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "damage": 0}

        if self.can_attack():
            damage = self.get_damage()
            opponent.calculate_damage(damage)
            result["success"] = True
            result["damage"] = damage

        #self.view.display_attack_result(result)
        return result

    def special_skill(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False}

        if random.random() < 0.4:
            damage = random.randint(75, 175)
            opponent.calculate_damage(damage)
            result["success"] = True
            result["damage"] = damage
        #self.view.warrior_attack_result(result)

        return result


class Priestess(Hero):
    """ Priestess class is the child class of Hero """

    def __init__(self):
        super().__init__("Priestess", 75, 5, 0.7, 25, 45,
                         0.3, 0, 0, 0)

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
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        self.stats["hit_points"] -= damage

    def can_attack(self):
        return random.random() < self.stats["chance_to_hit"]

    def attack(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "damage": 0}

        if self.can_attack():
            damage = self.get_damage()
            opponent.calculate_damage(damage)
            result["success"] = True
            result["damage"] = damage

        #View.display_attack_result(result)
        return result

    def special_skill(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "heal": 0}

        heal = random.randint(25, 50)
        opponent.calculate_damage(-heal)

        result["success"] = True
        result["heal"] = heal

        #View.priestess_attack_result(result)
        return result


class Thief(Hero):
    """ Thief class is the child class of Hero """

    def __init__(self):
        super().__init__("Thief", 75, 6, 0.8, 20, 40,
                         0.4, 0, 0, 0)

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
        return random.randint(self.stats["min_damage"], self.stats["max_damage"])

    def calculate_damage(self, damage):
        self.stats["hit_points"] -= damage

    def can_attack(self):
        return random.random() < self.stats["chance_to_hit"]

    def attack(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "damage": 0}

        if self.can_attack():
            damage = self.get_damage()
            opponent.calculate_damage(damage)
            result["success"] = True
            result["damage"] = damage

        View.display_attack_result(result)
        return result

    def special_skill(self, opponent):
        result = {"attacker": self.hero_name, "opponent": opponent.hero_name, "success": False, "attacks": 0,
                  "damage": 0}

        chance = random.random()
        if chance < 1:
            # if self.can_attack():
            #     damage = self.get_damage()
            #     opponent.calculate_damage(damage)
            #     result["success"] = True
            #     result["damage"] = damage
            res = self.attack(opponent)
            result["damage"] += res["damage"]
            res = self.attack(opponent)
            result["damage"] += res["damage"]
            print(result)

            #self.attack(opponent)

            # print(f" {self.hero_name} attacked twice")
            result["success"] = True
            result["attacks"] = 2
            # result["damage"] = damage
            # self.view.thief_special_attack_result(result)
        elif chance < 0.8:
            result=self.attack(opponent)
            # print(f" {self.hero_name} attacked once")
            result["success"] = True
            result["attacks"] = 1

            # self.view.thief_special_attack_result(result)

        View.thief_special_attack_result(result)
        # else:
        #     self.view.thief_special_attack_result(result)
        #     #print(f"{self.hero_name} couldn't attack")

        return result


w = Warrior()
p = Priestess()
t = Thief()
p.attack(w)
w.special_skill(t)
t.special_skill(w)
