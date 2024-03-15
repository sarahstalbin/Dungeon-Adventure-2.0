"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 503
Dungeon Adventure: dungeon adventure unit test
"""
import io
import sys
import unittest, builtins
from unittest.mock import patch
from DungeonAdventure import DungeonAdventure
from Room import Room
from DungeonCharacterFactory import DungeonCharacterFactory

"""
Dungeon Adventure Unit Test.
"""

class DungeonAdventureTest(unittest.TestCase):

    def setUp(self):
        """
        Set up DungeonAdventure and room. Also blocks printouts
        """
        self.da = DungeonAdventure()
        self.room = Room()

        def block_print(*args,**kwargs):
            """ Prevents printing to console"""
            pass
        builtins.print = block_print

    @patch('builtins.input', side_effect=['Thief', "easy", "Minna"])
    def test_set_play_mode_easy(self, prompt):
        """
        Testing easy play mode
        """
        expect_output = {"Name": "Thief", "HP": 75, "Healing Potion Count": 3,
                                "Vision Potion Count": 0, "Pillar Count": 0}

        self.da.set_play_mode()
        self.assertEqual(expect_output["Name"], self.da.hero.name, "Testing Easy for first set "
                                                                              "name failed")
        self.assertTrue(20 <= self.da.hero.healing_potion_count <= 30,
                         "Testing Easy for health potion failed")
        self.assertTrue(15 <= self.da.hero.vision_potion_count <= 20,
                         "Testing Easy for vision potion failed")
        self.assertEqual(expect_output["HP"], self.da.hero.hit_points,"Testing Easy for HP failed")
        self.assertEqual(expect_output["Pillar Count"] ,self.da.hero.pillar_count,  "Testing Easy for "
                                                                                    "Pillar count failed")
        self.assertEqual(5, self.da.dungeon.get_col_length(), "Testing Easy for "
                                                                                 "collumn length failed")
        self.assertEqual( 5, self.da.dungeon.get_row_length(),"Testing Easy for "
                                                                                 "row length failed")


    @patch('builtins.input', side_effect=['Warrior', 'medium', "Minna"])
    def test_set_play_mode_medium(self, prompt):
        """
        Testing medium play mode
        """
        expect_output = {"Name": "Warrior", "HP": 125, "Healing Potion Count": 3,
                                "Vision Potion Count": 3, "Pillar Count": 0}
        self.da.set_play_mode()
        self.assertEqual(expect_output["Name"], self.da.hero.name, "Testing Easy for first set "
                                                                              "name failed")
        self.assertEqual(expect_output["HP"], self.da.hero.hit_points , "Testing Med for HP failed")
        self.assertTrue(3 <= self.da.hero.healing_potion_count <= 10,
                         "Testing Med for health potion failed")
        self.assertTrue(3 <= self.da.hero.vision_potion_count <= 10,
                         "Testing Easy for vision potion failed")
        self.assertEqual(self.da.hero.pillar_count, expect_output["Pillar Count"] , "Testing Easy for "
                                                                                    "Pillar count failed")
        self.assertEqual(10, self.da.dungeon.get_col_length(), "Testing Easy for "
                                                                                 "collumn length failed")
        self.assertEqual( 10, self.da.dungeon.get_row_length(),"Testing Easy for "
                                                                                 "row length failed")

    @patch('builtins.input', side_effect=['Priestess', 'hard', "Minna"])
    def test_set_play_mode_hard(self, prompt):
        """
        Testing Hard play mode
        """
        expect_output = {"Name": "Priestess", "HP": 75, "Healing Potion Count": 5,
                         "Vision Potion Count": 5, "Pillar Count": 0}

        self.da.set_play_mode()
        self.assertEqual(expect_output["Name"], self.da.hero.name, "Testing Easy for first set "
                                                                              "name failed")
        self.assertEqual(expect_output["HP"], self.da.hero.hit_points,
                         "Testing hard for HP failed")
        self.assertEqual(expect_output["Healing Potion Count"], self.da.hero.healing_potion_count,
                         "Testing hard for health potion failed")

        self.assertEqual(expect_output["Vision Potion Count"],self.da.hero.vision_potion_count,
                         "Testing hard for Vision Potion Count failed")
        self.assertEqual(expect_output["Pillar Count"], self.da.hero.pillar_count, "Testing hard for "
                                                                                    "Pillar count failed")
        self.assertEqual(15, self.da.dungeon.get_col_length(), "Testing Easy for "
                                                          "column length failed")
        self.assertEqual(15, self.da.dungeon.get_row_length(), "Testing Easy for row length failed")

    @patch('builtins.input', side_effect=['w', 'c', 50, 20, 25, 20, 20, "Minna"])
    def test_set_play_mode_player(self, prompt):
        """
        Testing User choice play mode
        """
        expect_output = {"Name": "Warrior", "HP": 50, "Healing Potion Count": 20,
                         "Vision Potion Count": 25, "Pillar Count": 0}

        self.da.set_play_mode()
        self.assertEqual(expect_output["Name"], self.da.hero.name, "Testing Easy for first set "
                                                                              "name failed")
        self.assertEqual(expect_output["HP"], self.da.hero.hit_points, "Testing hard for HP failed")
        self.assertEqual(expect_output["Healing Potion Count"],self.da.hero.healing_potion_count,
                         "Testing hard for health potion failed")

        self.assertEqual(expect_output["Vision Potion Count"], self.da.hero.vision_potion_count,
                         "Testing hard for Vision Potion Count failed")
        self.assertEqual(expect_output["Pillar Count"], self.da.hero.pillar_count, "Testing hard for "
                                                                                    "Pillar count failed")
        self.assertEqual(20, self.da.dungeon.get_col_length(), "Testing Easy for "
                                                          "column length failed")
        self.assertEqual(20, self.da.dungeon.get_row_length(), "Testing Easy for row length failed")

    def test_menu_str(self):
        """
        Tests the menu string to be printed
        """
        self.da.menu_str()
        menu = {"Action Menu": "m", "Go Up": "w", "Go Down": "s", "Go Left": "a", "Go Right": "d",
                "Use Health Potion": "h", "Use Vision": "v", "Normal Attack": "1", "Special Attack": "2",
                "View current status": "stats", "Map Display": "map", "Save Game": "save", "Quit Game": "q"}
        formatted_list = ["    " + item + " : " + values for item, values in menu.items()]
        string_test = "\n".join(formatted_list) + "\n"
        actual_string = self.da.menu_str()
        self.assertEqual(string_test, actual_string, "Menu str not equal")

    @patch('builtins.input', side_effect=['w', 'hard', 'Minna', 'h', 'q'])
    def test_player_command_health(self, prompt):
        """
        Testing player using health command.
        set_play_mode() sets default values for testing - health potion: 5 and hp 125
        Updated values are healing poitions: 4 and Hp greater than 125
        """

        self.da.set_play_mode()
        self.da.use_healing_potion()

        self.assertEqual(4, self.da.hero.healing_potion_count, "Test player command h healing count failed")
        self.assertTrue(self.da.hero.hit_points > 125, "Testing player command h HP failed")

    # @patch('builtins.input', side_effect=['kill'])
    def test_move_hero_south(self):
        """
        Testing player input for south direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        self.da.player_loc_row = 0
        self.da.player_loc_col = 0

        # print(self.da.move_hero("s"))
        real_direction = 'S'

        new_row, new_col = self.da.dungeon._return_neighbor_coordinates(self.da.player_loc_row, self.da.player_loc_col,
                                                                        real_direction)

        current_key = (self.da.player_loc_row, self.da.player_loc_col)
        new_key = (new_row, new_col)

        with patch('DungeonAdventure.DungeonAdventure.move_hero', side_effect=lambda self, menu_command: 's') as mock_method:



            #test if there is a room
            if self.da.dungeon.is_valid_room(new_row, new_col):
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), True, "Test if hero can go south "
                                                                                  "room failed")

            else:
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), False, "Test if hero can go south "
                                                                                  "room fail failed")
            #test if you go into the room
            if self.da.dungeon.show_doors(current_key, new_key, real_direction):
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                                  "hero door fail")
            else:
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                            "hero room fail failed")

    def test_move_hero_north(self):
        """
        Testing player input for north direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        self.da.player_loc_col = 1
        self.da.player_loc_row = 1
        real_direction = "N"
        current_row = self.da.player_loc_row
        current_col = self.da.player_loc_col
        new_row, new_col = self.da.dungeon._return_neighbor_coordinates(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)
        with patch('DungeonAdventure.DungeonAdventure.move_hero', side_effect=lambda self, menu_command: 'n') as mock_method:
        # test if there is a room
            if self.da.dungeon.is_valid_room(new_row, new_col):
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), True, "Test move hero next "
                                                                                   "room failed")

            else:
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), False, "Test move hero next "
                                                                                   "room fail failed")

            # test if you can go into the room
            if self.da.dungeon.show_doors(current_key, new_key, real_direction):
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                                   "hero door fail")
            else:
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                            "hero room fail failed")

    def test_move_hero_east(self):
        """
        Testing player input for east direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """

        real_direction = "E"
        current_row = 0
        current_col = 0
        new_row, new_col = self.da.dungeon._return_neighbor_coordinates(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)
        with patch('DungeonAdventure.DungeonAdventure.move_hero',
                   side_effect=lambda self, menu_command: 'e', ) as mock_method:
            # test if there is a room
            if self.da.dungeon.is_valid_room(new_row, new_col):
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), True, "Test move hero next "
                                                                                   "room failed")

            else:
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), False, "Test move hero next "
                                                                                    "room fail failed")

            # test if you can go into the room
            if self.da.dungeon.show_doors(current_key, new_key, real_direction):
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                                   "hero door fail")

            else:
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                                    "room fail failed")

    def test_move_hero_west(self):
        """
        Testing player input for west direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        self.da.player_loc_col = 1
        self.da.player_loc_row = 1
        real_direction = "W"
        current_row = self.da.player_loc_row
        current_col = self.da.player_loc_col
        new_row, new_col = self.da.dungeon._return_neighbor_coordinates(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)
        with patch('DungeonAdventure.DungeonAdventure.move_hero',
                   side_effect=lambda self, menu_command: 'w', ) as mock_method:
        # test if there is a room
            if self.da.dungeon.is_valid_room(new_row, new_col):
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), True, "Test move hero next "
                                                                                   "room failed")
            else:
                self.assertEqual(self.da.dungeon.is_valid_room(new_row, new_col), False, "Test move hero next "
                                                                                    "room fail failed")

            # test if you can go into the room
            if self.da.dungeon.show_doors(current_key, new_key, real_direction):
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), True, "Test move ")
            else:
                self.assertEqual(self.da.dungeon.show_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                            "hero door fail failed")

    def test_collect_item_health(self):
        """
        Testing collect health item in room
        """
        # Collect Health potion
        self.room.healing_potion = True
        self.da.collect_item(self.room)
        health_potion_count = self.da.hero.healing_potion_count
        self.assertEqual(1, health_potion_count, "Test healing count failed")

    def test_collect_item_vision(self):
        """
        Testing collect vision item in room
        """
        # Collect Health potion
        self.room.vision_potion = True
        self.da.collect_item(self.room)

        self.assertEqual(1, self.da.hero.vision_potion_count, "Test vision count failed")

    def test_collect_item_pit(self):
        """
        Testing collect pit item in room
        """
        # Collect Health potion
        self.room.pit = True
        self.da.collect_item(self.room)
        self.assertTrue(-15 <= self.da.item.create_item("X", 1,15).use_item() <= -1,"Testing item pit failed")

    def test_collect_item_exit(self):
        """
        Testing collect exit command in room
        """

        self.room.exit = True
        returned_room = self.da.collect_item(self.room)

        self.assertEqual(True, returned_room.exit, "Test exit failed")

    def test_collect_item_A(self):
        """
        Testing collect abstraction item in room
        """
        # Collect Health potion
        self.room.abstraction_pillar = True
        self.da.collect_item(self.room)
        pillar_count = self.da.hero.pillar_count
        self.assertEqual(pillar_count, 1)

    def test_collect_item_P(self):
        """
        Testing collect polymorphism item in room
        """
        # Collect Health potion
        self.room.polymorphism_pillar = True
        self.da.collect_item(self.room)
        pillar_count = self.da.hero.pillar_count
        self.assertEqual(pillar_count, 1)

    def test_collect_item_I(self):
        """
        Testing collect inheritance item in room
        """
        # Collect Health potion
        self.room.inheritance_pillar = True
        self.da.collect_item(self.room)
        pillar_count = self.da.hero.pillar_count
        self.assertEqual(pillar_count, 1)

    def test_collect_item_E(self):
        """
        Testing collect encapsulation item in room
        """
        # Collect Health potion
        self.room.encapsulation_pillar = True
        self.da.collect_item(self.room)
        pillar_count = self.da.hero.pillar_count
        self.assertEqual(pillar_count, 1)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_ogre(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.ogre = True
        self.da.collect_item(self.room)
        self.assertEqual(self.room.ogre, False)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_gremlin(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.gremlin = True
        self.da.collect_item(self.room)
        self.assertEqual(self.room.gremlin, False)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_skeleton(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.skeleton = True
        self.da.collect_item(self.room)
        self.assertEqual(self.room.skeleton, False)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_dragon(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.dragon = True
        self.da.collect_item(self.room)
        self.assertEqual(self.room.dragon, False)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_chimera(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.chimera = True
        self.da.collect_item(self.room)
        self.assertEqual(self.room.chimera, False)

    @patch('builtins.input', side_effect=['kill'])
    def test_collect_item_troll(self, prompt):
        """
        Testing collect ogre monster item in room
        """
        # Collect Health potion
        self.room.troll = True
        self.da.collect_item(self.room)

        self.assertEqual(self.room.troll, False)


    def test_pickle(self):
        """
        Testing pickle/save and load
        """
        #dump data
        self.da.player_name = 'Minna'
        self.hero = DungeonCharacterFactory.create_character("priestess", "Priestess")
        self.da.player_loc_col = 2
        self.da.player_loc_row = 1
        self.da.send_save_data()
        self.da.play_saved_game()
        self.assertEqual('Priestess', self.da.hero.name, "Pickle Hero Name Test Failed")
        self.assertEqual('Minna', self.da.player_name, "Pickle Name Test Failed")
        self.assertEqual(2, self.da.player_loc_col, "Pickle col Test Failed")
        self.assertEqual(1, self.da.player_loc_row,  "Pickle row Test Failed")



if __name__ == "__main__":
    unittest.main()
