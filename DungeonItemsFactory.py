"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 504
Dungeon Adventure 2.0
"""

from DungeonItems import HealingPotion, VisionPotion, Pit, MultiItem


class DungeonItemsFactory:
    """
    Creates and returns Item objects for the Dungeon Adventure Game.
    All Items should be created via the DungeonItemsFactory.

    Contains one method, create_item(), which creates an Item object of a specified type using relevant data for
    creating that Item.

    """

    @staticmethod
    def create_item(item_type, *args):
        """
        Static method that returns Items for the Dungeon.
        :param item_type: The type of Item to be instantiated.
        :param args: Variable arguments based on the Item to be instantiated.
        :return: an Item object for Dungeon Adventure 2.0.
        """
        if item_type == "V":
            return VisionPotion()
        elif item_type == "H":
            return HealingPotion(*args)
        elif item_type == "X":
            return Pit(*args)
        elif item_type == "M":
            return MultiItem()
        else:
            raise ValueError("Invalid item type")
        