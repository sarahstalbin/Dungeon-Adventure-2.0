"""
Aqueno Amalraj, Minna Chae, Sarah St. Albin
TCSS 504
Assignment: Dungeon Adventure 2.0
"""

import unittest
from unittest.mock import patch
from Monster import Monster


class MonsterTests(unittest.TestCase):

    def test_init(self):
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.25,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        self.assertIsInstance(monster, Monster)
        self.assertEqual(monster.name, mock_data['name'])
        self.assertEqual(monster.minimum_damage, mock_data['minimum_damage'])
        self.assertEqual(monster.maximum_damage, mock_data['maximum_damage'])
        self.assertEqual(monster.hit_points, mock_data['hit_points'])
        self.assertEqual(monster.heal_points, mock_data['heal_points'])
        self.assertEqual(monster.chance_to_heal, mock_data['chance_to_heal'])
        self.assertEqual(monster.chance_to_hit, mock_data['chance_to_hit'])

    @patch('Monster.Monster.get_random_heal_points')
    def test_heal_success(self, mock_get_random_heal_points):
        """ Verifies that heal successfully adds hit_points when there is a chance to heal """
        # Create an instance
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.25,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        mock_get_random_heal_points.return_value = 20

        result = monster.heal()

        self.assertTrue(result["success"])
        self.assertEqual(result["heal_amount"], 85)

    @patch('Monster.Monster.get_random_heal_points')
    def test_heal_no_chance_to_heal(self, mock_get_random_heal_points):
        """ Verifies that the Monster cannot heal if chance to heal is 0.0 """

        # Create instance with NO CHANCE TO HEAL
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.0,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        mock_get_random_heal_points.return_value = 20

        result = monster.heal()

        self.assertFalse(result["success"])
        self.assertEqual(result["heal_amount"], 0)

    @patch('Monster.Monster.get_random_heal_points')
    def test_heal_when_fainted(self, mock_get_random_heal_points):
        """ Verifies that Monster cannot heal if it has fainted """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        # Mocking the return value of get_random_heal_points
        mock_get_random_heal_points.return_value = 20

        monster.hit_points = 0

        monster.has_fainted()

        # Attempting to heal the monster
        result = monster.heal()

        # Asserting that the heal method was not successful due to fainted status
        self.assertFalse(result["success"])
        self.assertEqual(result["heal_amount"], 0)

    def test_get_random_heal_points(self):
        """ Verifies that method will return random integer between min and max heal points """

        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        result = monster.get_random_heal_points()

        self.assertGreaterEqual(result, mock_data['minimum_heal_points'])
        self.assertLessEqual(result, mock_data['maximum_heal_points'])

    def test_chance_to_heal_getter(self):
        """ Verifies that getter returns the chance to heal """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        result = monster.chance_to_heal

        self.assertEqual(result, mock_data['chance_to_heal'])

    def test_chance_to_heal_setter_valid_input(self):
        """ Verifies that setter will change chance_to_heal attribute data with valid input """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        valid_input = 0.75

        result = monster.chance_to_heal = valid_input

        self.assertEqual(result, valid_input)

    def test_chance_to_heal_setter_invalid_input(self):
        """ Verifies setter will raise ValueError if invalid input is given """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        with self.assertRaises(ValueError):
            monster.chance_to_heal = -10


    def test_minimum_heal_points_getter(self):
        """ Verifies that getter returns minimum heal points """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        result = monster.minimum_heal_points

        self.assertEqual(result, mock_data['minimum_heal_points'])

    def test_minimum_heal_points_setter_valid_input(self):
        """ Verifies setter will change minimum heal_points attribute with valid input """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        valid_input = 15

        result = monster.minimum_heal_points = valid_input

        self.assertEqual(result, valid_input)

    def test_minimum_heal_points_setter_invalid_input(self):
        """ Verifies setter will change maximum heal_points attribute with valid input """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        with self.assertRaises(ValueError):
            monster.minimum_heal_points = -1

    def test_maximum_heal_points_getter(self):
        """ Verifies that getter returns maximum heal points """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        result = monster.maximum_heal_points

        self.assertEqual(result, mock_data['maximum_heal_points'])

    def test_maximum_heal_points_setter_valid_input(self):
        """ Verifies setter will change maximum heal_points attribute with valid input """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        valid_input = 50

        result = monster.maximum_heal_points = valid_input

        self.assertEqual(result, valid_input)

    def test_maximum_heal_points_setter_invalid_input(self):
        """ Verifies maximum_heal_point setter will raise ValueError if invalid input is given """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        with self.assertRaises(ValueError):
            monster.minimum_heal_points = -20

    def test_heal_points_getter(self):
        """ Verifies that getter returns heal points """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        result = monster.heal_points

        self.assertEqual(result, mock_data['heal_points'])

    def test_heal_points_setter_valid_input(self):
        """ Verifies setter will change heal_points attribute with valid input """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        valid_input = 25

        result = monster.heal_points = valid_input

        self.assertEqual(result, valid_input)

    def test_heal_points_setter_invalid_input(self):
        """ Verifies heal_point setter will raise ValueError if invalid input is given """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        with self.assertRaises(ValueError):
            monster.heal_points = -15

    def test_has_fainted(self):
        """ Verifies that method updates and returns Monster's fainting status if it loses too many hit points """
        mock_data = {'monster_type': 'gremlin', 'name': 'Gizmo', 'hit_points': 65, 'attack_speed': 5,
                     'chance_to_hit': 0.7, 'minimum_damage': 10, 'maximum_damage': 25, 'chance_to_heal': 0.7,
                     'minimum_heal_points': 10, 'maximum_heal_points': 30, 'heal_points': 30, 'has_fainted': False}

        monster = Monster(**mock_data)

        monster.hit_points = 0

        monster.has_fainted()

        self.assertTrue(monster._has_fainted)




if __name__ == '__main__':
    unittest.main()
