import unittest
import unittest, builtins

from DungeonItems import HealingPotion, VisionPotion, Pit
from Dungeon import Dungeon

"""
Dungeon Adventure Unit Test. Must delete at end of DungeonAdventure.py 
game_play = DungeonAdventure()
game_play.play_whole_game()

for unit test to run properly.
"""


class TestItems(unittest.TestCase):
    """ Test cases for the child classes of DungeonItems """
    def setUp(self):
        """
        Set up DungeonAdventure and room. Also blocks printouts
        """
        pass

        def block_print(*args,**kwargs):
            """ Prevents printing to console"""
            pass
        builtins.print = block_print

    def test_healing_potion(self):
        """ Tests HealingPotion class get_name and the abstract method use_item"""
        healing_potion = HealingPotion(1, 10)
        self.assertEqual("H", healing_potion.get_name())
        self.assertGreaterEqual(healing_potion.use_item(), 1)
        self.assertLessEqual(healing_potion.use_item(), 10)

    def test_pit(self):
        """ Tests Pit class get_name and the abstract method use_item"""
        pit = Pit(1, 10)
        self.assertEqual("X", pit.get_name())
        self.assertGreaterEqual(pit.use_item(), -10)
        self.assertLessEqual(pit.use_item(), -1)

    def test_vision_rm_corner_no_cornerNW(self):
        """
        Tests NW corner of an area without a NW corner (coordinates are 0,0).
        """

        dungeon = Dungeon(5,5)
        vision_rooms = VisionPotion()
        current_row = 2
        current_col = 2

        vision_rooms.use_vision(current_row, current_col, dungeon)

        dungeon_max_row = dungeon.get_row_length()
        dungeon_max_col = dungeon.get_col_length()



        row = 1
        col = 1

        top_t = []
        mid_t = []
        bottom_t = []
        space = " "


        if current_row > 0 and current_col > 0:  # upper left
            top_t.append(str(dungeon.get_room_str((current_row - 1, current_col - 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row - 1, current_col - 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row - 1, current_col - 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row - 1, current_col - 1)))[-3:] + (space * 10))

        if current_row > 0:  # directly up
            top_t.append(str(dungeon.get_room_str((current_row - 1, current_col)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row - 1, current_col)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row - 1, current_col)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row - 1, current_col)))[-3:] + (space * 10))

            # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col)))
            row += 1

            if current_col + 1 < dungeon_max_col:  # upper right
                top_t.append(str(dungeon.get_room_str((current_row - 1, current_col + 1)))[0:3] + space * 10)
                mid_len = len(str(dungeon.get_room_str((current_row - 1, current_col + 1)))[4:-4])
                mid_t.append(
                    str(dungeon.get_room_str((current_row - 1, current_col + 1)))[4:-4] + space * (13 - mid_len))
                bottom_t.append(str(dungeon.get_room_str((current_row - 1, current_col + 1)))[-3:] + (space * 10))

                # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col+1)))
        if current_col > 0:  # left
            top_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row, current_col - 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row, current_col - 1)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row, current_col - 1)))
            col += 1

        # vision_rooms.append(dungeon.get_room_str((current_row, current_col))) #current room
        top_t.append(str(dungeon.get_room_str((current_row, current_col)))[0:3] + space * 10)
        mid_len = len(str(dungeon.get_room_str((current_row, current_col)))[4:-4])
        current = str(dungeon.get_room_str((current_row, current_col)))[4]
        current += "@"
        current += str(dungeon.get_room_str((current_row, current_col)))[-5:-4] + space * (13 - mid_len)
        mid_t.append(current)
        # mid_t.append(str(dungeon.get_room_str((current_row, current_col)))[4:-4] + space * (13 - mid_len))
        bottom_t.append(str(dungeon.get_room_str((current_row, current_col)))[-3:] + (space * 10))

        if current_col + 1 < dungeon_max_col:  # right
            top_t.append(str(dungeon.get_room_str((current_row, current_col + 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row, current_col + 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row, current_col + 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row, current_col + 1)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row, current_col+1)))
            col += 1
        if current_col > 0 and current_row + 1 < dungeon_max_row:  # below left
            top_t.append(str(dungeon.get_room_str((current_row + 1, current_col - 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row + 1, current_col - 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row + 1, current_col - 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row + 1, current_col - 1)))[-3:] + (space * 10))

            # vision_rooms.append(dungeon.get_room_str((current_row - 1, current_col - 1)))

        if current_row + 1 < dungeon_max_row:  # directly below
            top_t.append(str(dungeon.get_room_str((current_row + 1, current_col)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row + 1, current_col)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row + 1, current_col)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row + 1, current_col)))[-3:] + (space * 10))
            # vision_rooms.append(dungeon.get_room_str((current_row+1, current_col)))
            row += 1
        if current_col + 1 < dungeon_max_col and current_row + 1 < dungeon_max_row:  # below right
            top_t.append(str(dungeon.get_room_str((current_row + 1, current_col + 1)))[0:3] + space * 10)
            mid_len = len(str(dungeon.get_room_str((current_row + 1, current_col + 1)))[4:-4])
            mid_t.append(str(dungeon.get_room_str((current_row + 1, current_col + 1)))[4:-4] + space * (13 - mid_len))
            bottom_t.append(str(dungeon.get_room_str((current_row + 1, current_col + 1)))[-3:] + (space * 10))
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
        self.assertEqual(vision_str, vision_rooms.use_vision(current_row, current_col, dungeon), "Test Vision failed")


if __name__ == '__main__':
    unittest.main()
