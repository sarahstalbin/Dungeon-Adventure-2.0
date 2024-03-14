"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""
import unittest
from DungeonItemsFactory import DungeonItemsFactory
from DungeonItems import VisionPotion, HealingPotion, Pit


class TestDungeonItemsFactory(unittest.TestCase):
    def test_create_vision_potion(self):
        vision_potion = DungeonItemsFactory.create_item("V")
        self.assertIsInstance(vision_potion, VisionPotion)

    def test_create_healing_potion(self):
        healing_potion = DungeonItemsFactory.create_item("H", 1, 10)
        self.assertIsInstance(healing_potion, HealingPotion)

    def test_create_pit(self):
        pit = DungeonItemsFactory.create_item("X", 1, 10)
        self.assertIsInstance(pit, Pit)


if __name__ == '__main__':
    unittest.main()
