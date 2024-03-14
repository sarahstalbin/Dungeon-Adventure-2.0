"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from Room import (Room)
from Dungeon import Dungeon
from Monster import Monster
import random


class DungeonTests(unittest.TestCase):

    def test_init_valid_input(self):
        """ Tests the __init__ constructor """

        rows, cols = 5, 5

        dungeon = Dungeon(rows, cols)

        self.assertIsInstance(dungeon, Dungeon)
        self.assertEqual(dungeon.get_row_length(), rows)
        self.assertEqual(dungeon.get_col_length(), cols)

        self.assertEqual(len(dungeon.get_maze_array()), rows)
        self.assertEqual(len(dungeon.get_maze_array()), cols)

        for row in dungeon.get_maze_array():
            self.assertEqual(len(row), 5)
            for room in row:
                self.assertIsInstance(room, Room)

    def test_init_invalid_input(self):
        """ Verifies the __init__ raises an error if input is invalid """

        rows, cols = 1, 1
        with self.assertRaises(ValueError):
            Dungeon(rows, cols)

    @patch('Dungeon.Dungeon._place_items')
    @patch('Dungeon.Dungeon._place_pillars')
    @patch('Dungeon.Dungeon._is_traversable')
    @patch('Dungeon.Dungeon._make_impassable')
    @patch('Dungeon.Dungeon._set_entrance_exit')
    @patch('Dungeon.Dungeon._create_maze')
    def test_build_dungeon(self, mock_create_maze, mock_set_entrance_exit, mock_make_impassable, mock_is_traversable,
                           mock_place_pillars, mock_place_items):
        """ Tests the build_dungeon method. Verifies that the starting row and column are successfully chosen,
        the _create_maze method is called, the entrance and exit are set, some rooms are set as impassable,
        the maze is traversed and if traversable is set as traversable, that self.__items is populated with
        coordinates and Room objects, pillars and items are placed, and if the maze is not traversable then
        it is regenerated. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        random.seed(42)

        dungeon.build_dungeon()

        random.seed(42)

        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - 1)
        start_room = dungeon.get_maze_array()[start_row][start_col]

        mock_create_maze.assert_called_with(start_room, start_row, start_col)

        mock_set_entrance_exit.assert_called()

        mock_make_impassable.assert_called()

        random.seed(42)

        mock_is_traversable.return_value = True

        expected_items = {(row, col): dungeon.get_maze_array()[row][col] for row in range(rows) for col in range(cols)}
        self.assertEqual(dungeon.get_maze_dictionary(), expected_items)
        mock_place_pillars.assert_called()
        mock_place_items.assert_called()

        mock_is_traversable.return_value = False
        mock_create_maze.assert_called_with(start_room, start_row, start_col)

    def test_get_entrance(self):
        """ Verifies that the entrance of the Dungeon's maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_entrance()
        self.assertEqual(result, dungeon.get_maze_array()[0][0])

    def test_get_maze_array(self):
        """ Verifies that the list of Rooms is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_maze_array()
        self.assertEqual(result, dungeon.get_maze_array())

    def test_get_room_str(self):
        """ Verifies that method returns the Room value associated with its location coordinates. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        key = (1, 0)
        result = dungeon.get_room_str(key)
        self.assertEqual(result, dungeon.get_maze_dictionary().get(key))

    def test_get_col_length(self):
        """ Verifies that the number of columns in the maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_col_length()
        self.assertEqual(result, cols)

    def test_get_row_length(self):
        """ Verifies that the number of rows in the maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_row_length()
        self.assertEqual(result, rows)

    def test_get_doors_north(self):
        """ Verifies that method gets attributes of a Room using North door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 0)
        next = (0, 0)
        direction = "N"
        is_current_room_north_door = dungeon.get_room_str(current).north_door
        is_next_room_north_door = dungeon.get_room_str(next).south_door
        results = dungeon.show_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors north true failed")
        else:
            self.assertFalse(results, "Test get doors north false failed")

    #
    def test_get_doors_south(self):
        """ Verifies that method gets attributes of a Room using South door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (2, 1)
        direction = "S"
        is_current_room_north_door = dungeon.get_room_str(current).south_door
        is_next_room_north_door = dungeon.get_room_str(next).north_door
        results = dungeon.show_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors south true failed")
        else:
            self.assertFalse(results, "Test get doors south false failed")

    def test_get_doors_east(self):
        """ Verifies that method gets attributes of a Room using East door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (1, 2)
        direction = "E"
        is_current_room_north_door = dungeon.get_room_str(current).east_door
        is_next_room_north_door = dungeon.get_room_str(next).west_door
        results = dungeon.show_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors east true failed")
        else:
            self.assertFalse(results, "Test get doors east false failed")

    def test_get_doors_west(self):
        """ Verifies that method gets attributes of a Room using West door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (1, 0)
        direction = "W"
        is_current_room_north_door = dungeon.get_room_str(current).west_door
        is_next_room_north_door = dungeon.get_room_str(next).east_door
        results = dungeon.show_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors west true failed")
        else:
            self.assertFalse(results, "Test get doors west false failed")

    def test_is_valid_room(self):
        """ Verifies that method returns True if Room is valid """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        row = 1
        col = 0

        result = dungeon.is_valid_room(row, col)
        self.assertEqual(result, True)

    @patch('random.shuffle')
    @patch('random.choice')
    def test_create_maze(self, mock_shuffle, mock_choice):
        """ Verifies that _create_maze generates the maze for the Dungeon. Mocks internal methods
        to control randomness. """
        mock_shuffle.side_effect = lambda x: x[0]
        mock_choice.side_effect = lambda x: x

        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        # Mock the _get_neighbor_coords method to return specific coordinates
        with patch.object(dungeon, '_return_neighbor_coordinates', side_effect=[(1, 0), (2, 0), (1, 1), (0, 1)]):
            # Mock the is_valid_room method to always return True
            with patch.object(dungeon, 'is_valid_room', return_value=True):
                # Mock the _opposite_direction method to return the opposite direction
                with patch.object(dungeon, '_opposite_direction', side_effect=lambda x: {"N": "S", "S": "N", "E": "W",
                                                                                         "W": "E"}[x]):
                    # Mock the _knock_down_door method to do nothing during the test
                    with patch.object(dungeon, '_create_doors', Mock()):
                        # Call the _create_maze method
                        dungeon._create_maze(dungeon.get_maze_array()[0][0], 0, 0)

    def test_return_neighbor_coordinates(self):
        """ Verifies that method returns the integer coordinates of neighboring Rooms depending on direction."""
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        row = 2
        col = 1
        direction = "N"

        new_row, new_col = dungeon._return_neighbor_coordinates(row, col, direction)
        self.assertEqual((new_row, new_col), (1, 1))

    def test_opposite_direction(self):
        """ Verifies that method returns the String representation of the opposite direction based on parameter """
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        direction = "N"

        result = dungeon._opposite_direction(direction)
        self.assertEqual(result, {"N": "S", "S": "N", "E": "W", "W": "E"}[direction])

    @patch.object(Room, 'north_door', new_callable=PropertyMock)
    def test_create_doors_north(self, mock_north_door):
        """ Verifies that a north door can be set """
        dungeon = Dungeon(5, 5)
        room = Room()
        direction = "N"

        dungeon._create_doors(room, direction)

        mock_north_door.assert_called()

    @patch.object(Room, 'south_door', new_callable=PropertyMock)
    def test_create_doors_south(self, mock_south_door):
        """ Verifies that a south door can be set """
        dungeon = Dungeon(5, 5)
        room = Room()
        direction = "S"

        dungeon._create_doors(room, direction)

        mock_south_door.assert_called()

    @patch.object(Room, 'east_door', new_callable=PropertyMock)
    def test_knock_down_door_east(self, mock_east_door):
        """ Verifies that a east door can be set """
        dungeon = Dungeon(5, 5)
        room = Room()
        direction = "E"

        dungeon._create_doors(room, direction)

        mock_east_door.assert_called()

    @patch.object(Room, 'west_door', new_callable=PropertyMock)
    def test_knock_down_door_west(self, mock_west_door):
        """ Verifies that a west door can be set """
        dungeon = Dungeon(5, 5)
        room = Room()
        direction = "W"

        dungeon._create_doors(room, direction)

        mock_west_door.assert_called()

    def test_create_doors_invalid_direction(self):
        """ Verifies that an error is raised if any input other than N, S, E, W is passed """
        dungeon = Dungeon(5, 5)
        room = Room()

        with self.assertRaises(ValueError):
            direction = "Z"
            dungeon._create_doors(room, direction)

    def test_create_doors_invalid_input_non_string(self):
        """ Verifies that an error will be raised if a non-string is passed as the direction """
        dungeon = Dungeon(5, 5)
        room = Room()

        with self.assertRaises(ValueError):
            direction = 2
            dungeon._create_doors(room, direction)

    def test_create_doors_invalid_input_object(self):
        """ Verifies that an error will be raised if a non-Room object is passed """
        dungeon = Dungeon(5, 5)
        mock_data = {'monster_type': 'chimera', 'name': 'Thrawn', 'hit_points': 1000, 'attack_speed': 10,
                     'chance_to_hit': 0.9, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        with self.assertRaises(ValueError):
            direction = "N"
            dungeon._create_doors(monster, direction)

    def test_set_entrance_exit(self):
        """ Verifies that method sets the entrance and exit, including setting them as passable and empty. Also
        tests whether method sets a west door for the entrance and an east door for the exit. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        dungeon._set_entrance_exit()

        dungeon.get_maze_array()[0][0].entrance = True
        dungeon.get_maze_array()[rows - 1][cols - 1].exit = True

        dungeon.get_maze_array()[0][0].impasse = False
        dungeon.get_maze_array()[rows - 1][cols - 1].impasse = False

        dungeon.get_maze_array()[0][0].empty_room = True
        dungeon.get_maze_array()[rows - 1][cols - 1].empty_room = True

        dungeon.get_maze_array()[0][0].west_door = True
        dungeon.get_maze_array()[rows - 1][cols - 1].east_door = True

        entrance_row, entrance_col = 0, 0
        exit_row, exit_col = rows - 1, cols - 1

        # Assertions
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].entrance,
                        'Entrance should be set at (0, 0)')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].exit,
                        f'Exit should be set at ({exit_row}, {exit_col})')
        self.assertFalse(dungeon.get_maze_array()[entrance_row][entrance_col].impasse,
                         'Entrance should be passable')
        self.assertFalse(dungeon.get_maze_array()[exit_row][exit_col].impasse,
                         'Exit should be passable')
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].empty_room,
                        'Entrance should be empty')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].empty_room,
                        'Exit should be empty')
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].west_door,
                        'Entrance should have a west door')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].east_door,
                        'Exit should have an east door')

    def test_make_impassable(self):
        """ Tests that method can make some Rooms impassable. Randomness controlled by deterministic seed. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        random.seed(42)

        dungeon._make_impassable()

        for row in range(rows):
            for col in range(cols):
                room = dungeon.get_maze_array()[row][col]

                if room.impasse:
                    self.assertTrue(room.impasse, f"Room at ({row}, {col}) should have impasse set to True")
                else:
                    self.assertFalse(room.impasse, f"Room at ({row}, {col}) should have impasse set to False")

    def test_is_traversable(self):
        """ Tests that method returns True if maze is found traversable or False if not. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        start_row = 0
        start_col = 0

        result = dungeon._is_traversable(start_row, start_col)

        self.assertTrue(isinstance(result, bool), f"Expected boolean, got {type(result)}")

        if result:
            self.assertTrue(dungeon._is_traversable(start_row, start_col))
        else:
            self.assertFalse(dungeon._is_traversable(start_row, start_col))

    def test_traverse_the_maze(self):
        """ Verifies that test_traverse_the_maze traverses the maze and returns True if it finds the exit or
        False if not. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        start_row = 0
        start_col = 0

        result = dungeon._traverse_the_maze(start_row, start_col)

        self.assertTrue(isinstance(result, bool), f"Expected boolean, got {type(result)}")

        target_room = dungeon.get_maze_array()[rows - 1][cols - 1]

        if result:
            self.assertTrue(dungeon.is_valid_room(start_row, start_col))
            self.assertTrue(target_room.visited)
        else:
            self.assertFalse(result, "Expected _traverse_the_maze to return False")

    def test__str__(self):
        """ Verifies that __str__ method returns a String with information about the entire Dungeon. """
        """
        Testing str function
        """
        d = Dungeon(5, 5)

        space = " "
        top = []
        mid = []
        bottom = []

        for row in range(d.get_row_length()):
            for col in range(d.get_col_length()):
                # Top string
                top.append(str(d.get_room_str((row, col)))[0:3] + space * 10)
                # Mid string
                mid_len = len(str(d.get_room_str((row, col)))[4:-4])
                if d.get_room_str((row, col)).current_room:

                    current = str(d.get_room_str((row, col)))[4]
                    current += "@"
                    current += str(d.get_room_str((row, col)))[-5:-4] + space * (13 - mid_len)
                    mid.append(current)
                else:
                    mid.append(str(d.get_room_str((row, col)))[4:-4] + space * (13 - mid_len))

                bottom.append(str(d.get_room_str((row, col)))[-3:] + (space * 10))

        expected_dungeon_str = ""
        for i in range(0, d.get_row_length()):
            for room in range(i * d.get_col_length(), (i + 1) * d.get_col_length()):
                expected_dungeon_str += top[room]
            expected_dungeon_str += "\n"
            for room in range(i * d.get_col_length(), (i + 1) * d.get_col_length()):
                expected_dungeon_str += mid[room]
            expected_dungeon_str += "\n"
            for room in range(i * d.get_col_length(), (i + 1) * d.get_col_length()):
                expected_dungeon_str += bottom[room]
            expected_dungeon_str += "\n\n"

        self.assertEqual(expected_dungeon_str, d.__str__(), "Test Dungeon __str__ failed")

    def test_place_pillars(self):
        """
        Testing for one instance of each pillar polymorphism, inheritance, encapsulation, abstraction within the maze
        """
        d = Dungeon(10, 10)

        polymorphism = sum(room.polymorphism_pillar for room in d.get_maze_dictionary().values())
        abstraction = sum(room.abstraction_pillar for room in d.get_maze_dictionary().values())
        encapsulation = sum(room.encapsulation_pillar for room in d.get_maze_dictionary().values())
        inheritance = sum(room.inheritance_pillar for room in d.get_maze_dictionary().values())

        self.assertEqual(polymorphism, 1)
        self.assertEqual(abstraction, 1)
        self.assertEqual(encapsulation, 1)
        self.assertEqual(inheritance, 1)

    def test_place_items(self):
        """ Verifies that place_items successfully places items throughout the maze """

        d = Dungeon(5, 5)

        vision = 0
        healing = 0
        pit = 0
        multiple = 0

        d._place_items()

        for room in d.get_maze_dictionary().values():
            if room.entrance or room.exit or room.abstraction_pillar \
                    or room.polymorphism_pillar or room.inheritance_pillar or room.encapsulation_pillar:
                continue

            if room.healing_potion:
                healing += 1
            elif room.vision_potion:
                vision += 1
            elif room.pit:
                pit += 1
            elif room.multiple_items:
                multiple += 1

        self.assertIsNotNone(vision, healing)
        self.assertIsNotNone(pit, multiple)

    def test_place_items_correct_rooms(self):
        """ Verifies that items are not placed in the entrance, exit, or in Rooms with Pillars """

        d = Dungeon(5, 5)

        d._place_items()

        for room in d.get_maze_dictionary().values():
            if room.entrance or room.exit:
                self.assertFalse(room.vision_potion)
                self.assertFalse(room.healing_potion)
                self.assertFalse(room.pit)
            else:
                self.assertFalse(room.abstraction_pillar and room.vision_potion)
                self.assertFalse(room.abstraction_pillar and room.healing_potion)
                self.assertFalse(room.abstraction_pillar and room.pit)
                self.assertFalse(room.abstraction_pillar and room.multiple_items)
                self.assertFalse(room.polymorphism_pillar and room.vision_potion)
                self.assertFalse(room.polymorphism_pillar and room.healing_potion)
                self.assertFalse(room.polymorphism_pillar and room.pit)
                self.assertFalse(room.polymorphism_pillar and room.multiple_items)
                self.assertFalse(room.encapsulation_pillar and room.vision_potion)
                self.assertFalse(room.encapsulation_pillar and room.healing_potion)
                self.assertFalse(room.encapsulation_pillar and room.pit)
                self.assertFalse(room.encapsulation_pillar and room.multiple_items)
                self.assertFalse(room.inheritance_pillar and room.vision_potion)
                self.assertFalse(room.inheritance_pillar and room.healing_potion)
                self.assertFalse(room.inheritance_pillar and room.pit)
                self.assertFalse(room.inheritance_pillar and room.multiple_items)


if __name__ == '__main__':
    unittest.main()
