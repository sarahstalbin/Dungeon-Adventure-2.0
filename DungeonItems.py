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
        vision_rooms = []
        current_room = copy.deepcopy(dungeon.get_room_str((current_row, current_col)))
        # self.current_room(current_room)
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


        for i in range(0, row):
            for room in range(i * col, (i + 1) * col):
                print(top_t[room], end="")
            print(end="\n")
            for room in range(i * col, (i + 1) * col):
                print(mid_t[room], end="")
            print(end="\n")
            for room in range(i * col, (i + 1) * col):
                print(bottom_t[room], end="")
            print("\n")



        #
        # if current_row > 0 and current_col > 0: #upper left
        #     vision_rooms.append(dungeon.get_room_str((current_row-1, current_col-1)))
        # if current_row > 0: #directly up
        #     vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col)))
        #     row += 1
        #
        #     if current_col +1 < dungeon_max_col: # upper right
        #         vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col+1)))
        # if current_col > 0: #left
        #     vision_rooms.append(dungeon.get_room_str((current_row, current_col - 1)))
        #     col += 1
        # print(dungeon.get_room_str((current_row, current_col)))
        # vision_rooms.append(dungeon.get_room_str((current_row, current_col))) #current room
        # if current_col + 1 < dungeon_max_col: #right
        #     vision_rooms.append(dungeon.get_room_str((current_row, current_col+1)))
        #     col += 1
        # if current_col > 0 and current_row + 1 < dungeon_max_row:  # below left
        #     print("I am here")
        #     print(dungeon.get_room_str((current_row - 1, current_col - 1)))
        #     vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col - 1)))
        #
        # if current_row +1 < dungeon_max_row: #directly below
        #     vision_rooms.append(dungeon.get_room_str((current_row+1, current_col)))
        #     row += 1
        # if current_col + 1 < dungeon_max_col and current_row + 1 < dungeon_max_row:  # below right
        #     vision_rooms.append(dungeon.get_room_str((current_row + 1, current_col + 1)))

        # top = []
        # space = " "
        #
        # for rooms in vision_rooms:
        #     # if str(rooms) != "":
        #     top.append(str(rooms)[0:3] + space * 10)
        # # mid
        # mid = []
        # for rooms in vision_rooms:
        #     mid_len = len(str(rooms)[4:-4])
        #     # if str(rooms) != "":
        #         # if len(str(rooms)) == 10:
        #     mid.append(str(rooms)[4:-4] + space * (13 - mid_len))
        #         # else:
        #             # mid.append(str(rooms)[4:7] + "    ")
        #
        # # bottom
        # bottom = []
        # for rooms in vision_rooms:
        #     # if str(rooms) != "":
        #         # if len(str(rooms)) == 10:
        #     bottom.append(str(rooms)[-3:] + (space * 10))
        #         # else:
        #             # bottom.append(str(rooms)[8:11] + "    ")
        #
        # # Printing View
        # for i in range(0, row):
        #     for room in range(i * col, (i + 1) * col):
        #         print(top[room], end="")
        #     print(end="\n")
        #     for room in range(i * col, (i + 1) * col):
        #         print(mid[room], end="")
        #     print(end="\n")
        #     for room in range(i * col, (i + 1) * col):
        #         print(bottom[room], end="")
        #     print("\n")


    # def current_room(self, room):
    #     """
    #     Sets player's current coordinates as current room. Used in vision potion
    #     """
    #     # if isinstance(room, Room):
    #     room.multiple_items = False
    #     room.healing_potion = False
    #     room.vision_potion = False
    #     room.pit = False
    #     room.entrance = False
    #     room.empty_room = False
    #     room.abstraction_pillar = False
    #     room.polymorphism_pillar = False
    #     room.inheritance_pillar = False
    #     room.encapsulation_pillar = False
    #     room.current_room = True
    #     # else:
        #     raise ValueError("Must submit a Room object")

class Pit(DungeonItems):
    def __init__(self, minimum, maximum):
        """ Inheriting DungeonItems class initializing name as "X" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("X")
        self.pit = -random.randint(minimum, maximum)

    def use_item(self):
        """ Implementing use_item method for Pit class"""
        return self.pit


class MultiItem(DungeonItems):
    def __init__(self):
        """ Inheriting DungeonItems class initializing name as "X" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("M")

    def use_item(self):
        pass
