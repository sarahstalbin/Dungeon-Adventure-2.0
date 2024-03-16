import unittest
from unittest.mock import patch
from Hero import Warrior, Priestess, Thief


class TestHeroClasses(unittest.TestCase):

    def test_warrior_special_skill(self):
        """ Test warrior special skill method"""
        warrior = Warrior("Warrior", 200, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        opponent = Warrior("Opponent", 200, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        # Setting random.randint to return 100 using patch
        with patch('random.random',  return_value=.1), patch('random.randint', return_value=100):
            result = warrior.special_skill(opponent)

            self.assertEqual(result['damage'], 100)
            self.assertTrue(result["success"])

    def test_priestess_special_skill(self):
        """ Test priestess special skill method"""
        priestess = Priestess("Priestess", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        opponent = Warrior("Opponent", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        with patch('random.randint', return_value=30):
            result = priestess.special_skill(opponent)

            self.assertEqual(result["heal"], 30)
            self.assertTrue(result["success"])

    def test_thief_special_skill(self):
        """ Test thief special skill method"""
        thief = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        opponent = Warrior("Opponent", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)

        with patch('random.random', return_value=0.1):
            result = thief.special_skill(opponent)

            self.assertEqual(result["attacks"], 2)
            self.assertTrue(result["success"])

    def test_chance_to_block_property(self):
        """ Test for chance_to_block property in Hero class"""
        hero = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        self.assertEqual(hero.chance_to_block, 0.5)
        hero.chance_to_block = 0.8
        self.assertEqual(hero.chance_to_block, 0.8)
        with self.assertRaises(ValueError):
            hero.chance_to_block = 2  # Int should raise ValueError

    def test_pillar_count_property(self):
        """ Test for pillar_count property in Hero class"""
        hero = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        self.assertEqual(hero.pillar_count, 3)
        hero.pillar_count = 4
        self.assertEqual(hero.pillar_count, 4)
        with self.assertRaises(ValueError):
            hero.pillar_count = 2.0  # Float should raise ValueError

    def test_healing_potion_property(self):
        """ Test for healing_potion_property in Hero class"""
        hero = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        self.assertEqual(hero.healing_potion_count, 2)
        hero.healing_potion_count = 4
        self.assertEqual(hero.healing_potion_count, 4)
        with self.assertRaises(ValueError):
            hero.healing_potion_count = 2.0  # Float should raise ValueError

    def test_vision_potion_property(self):
        """ Test for vision_potion property in Hero class"""
        hero = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        self.assertEqual(hero.vision_potion_count, 1)
        hero.vision_potion_count = 4
        self.assertEqual(hero.vision_potion_count, 4)
        with self.assertRaises(ValueError):
            hero.vision_potion_count = 2.0  # Float should raise ValueError

    def test_hero_str_representation(self):
        """ Testing str method"""
        hero = Thief("Thief", 100, 1, 0.8, 20, 40, 0.5, 2, 1, 3)
        expected_str = "Thief\nHit Points: 100\nAttack Speed: 1\nChance to Hit: 0.8\nMinimum Damage: 20\nMaximum Damage: 40\nChance to Block: 0.5\nHealing Potion Count: 2\nVision Potion Count: 1\nPillar Count: 3\n"
        self.assertEqual(str(hero), expected_str)


if __name__ == '__main__':
    unittest.main()
