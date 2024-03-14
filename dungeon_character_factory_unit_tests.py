"""
Aqueno Amalraj, Minna Chae, Sarah St. Albin
TCSS 504
Assignment: Dungeon Adventure 2.0
"""

import unittest
from unittest.mock import patch, MagicMock
from Monster import Monster
from Hero import Warrior, Priestess, Thief
from DungeonCharacterFactory import DungeonCharacterFactory


class DungeonCharacterFactoryTests(unittest.TestCase):

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_monster_chimera(self, mock_select_row, mock_create_connection):
        """ Verifies that a chimera boss Monster is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        chimera_data = {'name': 'Thrawn', 'hit_points': 300, 'attack_speed': 8,
                        'chance_to_hit': 0.9, 'minimum_damage': 50, 'maximum_damage': 65, 'chance_to_heal': 0.6,
                        'minimum_heal_points': 0, 'maximum_heal_points': 0, 'heal_points': 0, 'has_fainted': False}

        mock_select_row.return_value = chimera_data

        chimera = DungeonCharacterFactory.create_character('chimera', 'Thrawn')

        self.assertIsInstance(chimera, Monster)
        self.assertEqual(chimera.name, chimera_data['name'])
        self.assertEqual(chimera.has_fainted(), chimera_data['has_fainted'])
        self.assertEqual(chimera.heal_points, chimera_data['heal_points'])
        self.assertEqual(chimera.chance_to_heal, chimera_data['chance_to_heal'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_monster_ogre(self, mock_select_row, mock_create_connection):
        """ Verifies that an ogre Monster is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        ogre_data = {'name': 'Grommash', 'hit_points': 300, 'attack_speed': 8,
                        'chance_to_hit': 0.9, 'minimum_damage': 50, 'maximum_damage': 65, 'chance_to_heal': 0.6,
                        'minimum_heal_points': 0, 'maximum_heal_points': 0, 'heal_points': 0, 'has_fainted': False}

        mock_select_row.return_value = ogre_data

        ogre = DungeonCharacterFactory.create_character('ogre', 'Grommash')

        self.assertIsInstance(ogre, Monster)
        self.assertEqual(ogre.name, ogre_data['name'])
        self.assertEqual(ogre.has_fainted(), ogre_data['has_fainted'])
        self.assertEqual(ogre.heal_points, ogre_data['heal_points'])
        self.assertEqual(ogre.chance_to_heal, ogre_data['chance_to_heal'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_monster_gremlin(self, mock_select_row, mock_create_connection):
        """ Verifies that a gremlin Monster is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        gremlin_data = {'name': 'Gizmo', 'hit_points': 300, 'attack_speed': 8,
                        'chance_to_hit': 0.9, 'minimum_damage': 50, 'maximum_damage': 65, 'chance_to_heal': 0.6,
                        'minimum_heal_points': 0, 'maximum_heal_points': 0, 'heal_points': 0, 'has_fainted': False}

        mock_select_row.return_value = gremlin_data

        gremlin = DungeonCharacterFactory.create_character('gremlin', 'Gizmo')

        self.assertIsInstance(gremlin, Monster)
        self.assertEqual(gremlin.name, gremlin_data['name'])
        self.assertEqual(gremlin.has_fainted(), gremlin_data['has_fainted'])
        self.assertEqual(gremlin.heal_points, gremlin_data['heal_points'])
        self.assertEqual(gremlin.chance_to_heal, gremlin_data['chance_to_heal'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_monster_dragon(self, mock_select_row, mock_create_connection):
        """ Verifies that a dragon boss Monster is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        dragon_data = {'name': 'Volcanor', 'hit_points': 300, 'attack_speed': 8,
                        'chance_to_hit': 0.9, 'minimum_damage': 50, 'maximum_damage': 65, 'chance_to_heal': 0.6,
                        'minimum_heal_points': 0, 'maximum_heal_points': 0, 'heal_points': 0, 'has_fainted': False}

        mock_select_row.return_value = dragon_data

        dragon = DungeonCharacterFactory.create_character('dragon', 'Volcanor')

        self.assertIsInstance(dragon, Monster)
        self.assertEqual(dragon.name, dragon_data['name'])
        self.assertEqual(dragon.has_fainted(), dragon_data['has_fainted'])
        self.assertEqual(dragon.heal_points, dragon_data['heal_points'])
        self.assertEqual(dragon.chance_to_heal, dragon_data['chance_to_heal'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_warrior(self, mock_select_row, mock_create_connection):
        """ Verifies that a Warrior is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        warrior_data = {'name': 'Warrior', 'hit_points': 125, 'attack_speed': 4,
                        'chance_to_hit': 0.8, 'minimum_damage': 35, 'maximum_damage': 60, 'chance_to_block': 0.2,
                        'healing_potion_count': 0, 'vision_potion_count': 0, 'pillar_count': 0}

        mock_select_row.return_value = warrior_data

        warrior = DungeonCharacterFactory.create_character('warrior', 'Warrior')

        self.assertIsInstance(warrior, Warrior)
        self.assertEqual(warrior.name, warrior_data['name'])
        self.assertEqual(warrior.hit_points, warrior_data['hit_points'])
        self.assertEqual(warrior.attack_speed, warrior_data['attack_speed'])
        self.assertEqual(warrior.minimum_damage, warrior_data['minimum_damage'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_priestess(self, mock_select_row, mock_create_connection):
        """ Verifies that a Priestess is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        priestess_data = {'name': 'Priestess', 'hit_points': 125, 'attack_speed': 4,
                          'chance_to_hit': 0.8, 'minimum_damage': 35, 'maximum_damage': 60, 'chance_to_block': 0.2,
                          'healing_potion_count': 0, 'vision_potion_count': 0, 'pillar_count': 0}

        mock_select_row.return_value = priestess_data

        priestess = DungeonCharacterFactory.create_character('priestess', 'Priestess')

        self.assertIsInstance(priestess, Priestess)
        self.assertEqual(priestess.name, priestess_data['name'])
        self.assertEqual(priestess.hit_points, priestess_data['hit_points'])
        self.assertEqual(priestess.attack_speed, priestess_data['attack_speed'])
        self.assertEqual(priestess.minimum_damage, priestess_data['minimum_damage'])

    @patch('DungeonCharacterFactory.query_database.create_connection')
    @patch('DungeonCharacterFactory.query_database.select_row')
    def test_create_thief(self, mock_select_row, mock_create_connection):
        """ Verifies that a Thief is created as expected """
        mock_connection = MagicMock()
        mock_create_connection.return_value = mock_connection

        thief_data = {'name': 'Thief', 'hit_points': 125, 'attack_speed': 4,
                        'chance_to_hit': 0.8, 'minimum_damage': 35, 'maximum_damage': 60, 'chance_to_block': 0.2,
                        'healing_potion_count': 0, 'vision_potion_count': 0, 'pillar_count': 0}

        mock_select_row.return_value = thief_data

        thief = DungeonCharacterFactory.create_character('thief', 'Thief')

        self.assertIsInstance(thief, Thief)
        self.assertEqual(thief.name, thief_data['name'])
        self.assertEqual(thief.hit_points, thief_data['hit_points'])
        self.assertEqual(thief.attack_speed, thief_data['attack_speed'])
        self.assertEqual(thief.minimum_damage, thief_data['minimum_damage'])
