"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

import random, copy
from abc import ABC, abstractmethod


class DungeonItems(ABC):
    """ DungeonItems class implemented with abstractmethod"""

    def __init__(self, name):
        """ Initializing name
        param: name"""
        self.name = name

    def get_name(self):
        """ getter function for name"""
        return self.name

    @abstractmethod
    def use_item(self):
        """ abstract method of use_item"""
        pass


class HealingPotion(DungeonItems):
    def __init__(self, minimum, maximum):
        """ Inheriting DungeonItems class initializing name as "H" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("H")
        self.health_points = random.randint(minimum, maximum)

    def use_item(self):
        """ Implementing use_item method for HealingPotion class"""
        return self.health_points


class VisionPotion(DungeonItems):
    def __init__(self):
        """ Inheriting DungeonItems class initializing name as "H" """
        super().__init__("V")

    def use_item(self):
        pass

    def use_vision(self, current_row, current_col, dungeon): #dungeon_max_row, dungeon_max_col,
        """
        Prints a view of the surrounding rooms at current location. Used for Vision Potion
        :return: None
        """
        dungeon_max_row = dungeon.get_row_length()
        dungeon_max_col = dungeon.get_col_length()

        row = 1
        col = 1

        top_t = []
        mid_t = []
        bottom_t = []
        space = " "
        if current_row > 0 and current_col > 0: #upper left
            top_t.append(str(dungeon.get_room_str((current_row-1, current_col-1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row-1, current_col-1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row-1, current_col-1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row-1, current_col-1)))[-3:] + (space * 10))

        if current_row > 0: #directly up
            top_t.append(str(dungeon.get_room_str((current_row-1, current_col)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row-1, current_col)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row-1, current_col)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row-1, current_col)))[-3:] + (space * 10))

            # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col)))
            row += 1

            if current_col +1 < dungeon_max_col: # upper right
                top_t.append(str(dungeon.get_room_str((current_row - 1, current_col+1)))[0:3] + space * 10)
                mid_len = len(str(dungeon.get_room_str((current_row - 1, current_col+1)))[4:-4])
                mid_t.append(str(dungeon.get_room_str((current_row - 1, current_col+1)))[4:-4] + space * (13 - mid_len))
                bottom_t.append(str(dungeon.get_room_str((current_row - 1, current_col + 1)))[-3:] + (space * 10))

                # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col+1)))
        if current_col > 0: #left
            top_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row, current_col -1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row, current_col - 1)))
            col += 1

        # vision_rooms.append(dungeon.get_room_str((current_row, current_col))) #current room
        top_t.append(str(dungeon.get_room_str((current_row, current_col )))[0:3] + space * 10)
        mid_len = len(str(dungeon.get_room_str((current_row, current_col)))[4:-4])
        current = str(dungeon.get_room_str((current_row, current_col)))[4]
        current += "@"
        current += str(dungeon.get_room_str((current_row, current_col)))[-5:-4] + space * (13 - mid_len)
        mid_t.append(current)
        # mid_t.append(str(dungeon.get_room_str((current_row, current_col)))[4:-4] + space * (13 - mid_len))
        bottom_t.append(str(dungeon.get_room_str((current_row, current_col)))[-3:] + (space * 10))


        if current_col + 1 < dungeon_max_col: #right
            top_t.append(str(dungeon.get_room_str((current_row, current_col + 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row, current_col + 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row, current_col + 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row , current_col + 1)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row, current_col+1)))
            col += 1
        if current_col > 0 and current_row + 1 < dungeon_max_row:  # below left
            top_t.append(str(dungeon.get_room_str((current_row+1, current_col-1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row+1, current_col-1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row+1, current_col-1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row+1, current_col-1)))[-3:] + (space * 10))

            # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col - 1)))

        if current_row +1 < dungeon_max_row: #directly below
            top_t.append(str(dungeon.get_room_str((current_row+1, current_col)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row+1, current_col)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row+1, current_col)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row+1 , current_col)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row+1, current_col)))
            row += 1
        if current_col + 1 < dungeon_max_col and current_row + 1 < dungeon_max_row:  # below right
            top_t.append(str(dungeon.get_room_str((current_row+1, current_col + 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row+1, current_col + 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row+1, current_col + 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row+1 , current_col + 1)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row + 1, current_col + 1)))

        vision_str = ""
        for i in range(0, row):
            for room in range(i * col, (i + 1) * col):
                vision_str += top_t[room]
            vision_str += '\n'
            for room in range(i * col, (i + 1) * col):
                vision_str += mid_t[room]
            vision_str += '\n'
            for room in range(i * col, (i + 1) * col):
                vision_str += bottom_t[room]
            vision_str += '\n'
        return vision_str


class Pit(DungeonItems):
    def __init__(self, minimum, maximum):
        """ Inheriting DungeonItems class initializing name as "X" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("X")
        self.pit = -random.randint(minimum, maximum)

    def use_item(self):
        """ Implementing use_item method for Pit class"""
        return self.pit
