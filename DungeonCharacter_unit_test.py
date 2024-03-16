import unittest
from unittest.mock import patch

from Hero import Warrior, Thief


class TestDungeonCharacter(unittest.TestCase):

    def test_can_attack(self):
        """ Test for can_attack method in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        # Setting random.random to return 0.5 (which is less than 0.8) using patch
        with patch('random.random', return_value=0.5):
            self.assertTrue(hero.can_attack())

        # Setting random.random to return 0.9 (which is greater than 0.8) using patch
        with patch('random.random', return_value=0.9):
            self.assertFalse(hero.can_attack())

    def test_hero_attack(self):
        """ Test for attack method in Dungeon Character class"""

        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        opponent = Thief("Thief", 200, 1, 0.8, 30, 60, 0.5, 4, 5, 6)

        with patch.object(hero, 'can_attack', return_value=True), \
                patch.object(hero, 'get_damage', return_value=30):
            result = hero.attack(opponent)

        self.assertEqual(result["damage"], 30)
        self.assertTrue(result["success"])

    def test_hero_calculate_damage(self):
        """ Test for calculate_damage method in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        hero.calculate_damage(10)
        self.assertEqual(hero.hit_points, 90)

    def test_attack_unsuccessful(self):
        """ Test if the attack is unsuccessful"""
        hero = Warrior("Warrior", 100, 1, 0.0, 20, 40, 0.5, 2, 1, 3)
        opponent = Thief("Thief", 200, 1, 1, 30, 60, 0.5, 4, 5, 6)

        #  Setting the random number generation to ensure attack always fails using patch
        with patch('random.random', return_value=0.5):
            result = hero.attack(opponent)

        self.assertFalse(result["success"])
        self.assertEqual(result["damage"], 0)

    def test_get_damage(self):
        """ Test for get_damage method in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 10, 20, 0.5, 2, 1, 3)

        damage = hero.get_damage()
        self.assertGreaterEqual(damage, 10)
        self.assertLessEqual(damage, 20)

    def test_name_property(self):
        """ Test for name property in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.name, "Warrior")

        hero.name = "Warrior"
        self.assertEqual(hero.name, "Warrior")

        with self.assertRaises(ValueError):
            hero.name = ""  # Empty name should raise ValueError

    def test_hit_points_property(self):
        """ Test for hit_points property in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.hit_points, 100)

        hero.hit_points = 200
        self.assertEqual(hero.hit_points, 200)

        with self.assertRaises(ValueError):
            hero.hit_points = -1  # Empty name should raise ValueError

    def test_attack_speed_property(self):
        """ Test for attack_speed property in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.attack_speed, 1)

        hero.attack_speed = 2
        self.assertEqual(hero.attack_speed, 2)

        with self.assertRaises(ValueError):
            hero.hit_points = 2.0  # Float should raise ValueError

    def test_chance_to_hit_property(self):
        """ Test for chance_to_hit property in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.chance_to_hit, 0.8)

        hero.chance_to_hit = 0.7
        self.assertEqual(hero.chance_to_hit, 0.7)

        with self.assertRaises(ValueError):
            hero.chance_to_hit = 2  # Int should raise ValueError

    def test_minimum_damage_property(self):
        """ Test for minimum_damage property in Dungeon Character class"""
        hero = Warrior("Warrior", 100, 1, 0.8, 10, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.minimum_damage, 10)

        hero.minimum_damage = 20
        self.assertEqual(hero.minimum_damage, 20)

        with self.assertRaises(ValueError):
            hero.minimum_damage = 2.0  # Float should raise ValueError

    def test_maximum_damage_property(self):
        """ Test for maximum property in Dungeon Character class"""
        hero = Warrior("Conan", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        self.assertEqual(hero.maximum_damage, 40)

        hero.maximum_damage = 25
        self.assertEqual(hero.maximum_damage, 25)

        with self.assertRaises(ValueError):
            hero.maximum_damage = 2.0  # Float should raise ValueError


if __name__ == '__main__':
    unittest.main()
