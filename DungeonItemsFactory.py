"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

from DungeonItems import HealingPotion, VisionPotion, Pit
from random import randint
import random


class DungeonItemsFactory:
    """
    Creates and returns Item objects for the Dungeon Adventure Game.
    All Items should be created via the DungeonItemsFactory.

    Contains two methods: create_item(), which creates an Item object of a specified type using relevant data for
    creating that Item, and create_multiple_items(), which creates multiple Item objects.

    """

    @staticmethod
    def create_item(item_type, *args):
        """
        Static method that returns Items for the Dungeon.
        :param item_type (Str): The type of Item to be instantiated.
        :param args: Variable arguments based on the Item to be instantiated.
        :return: an Item object for the Dungeon Adventure Game.
        """
        if item_type == "V":
            return VisionPotion()
        elif item_type == "H":
            return HealingPotion(*args)
        elif item_type == "X":
            return Pit(*args)
        else:
            raise ValueError("Invalid item type")
