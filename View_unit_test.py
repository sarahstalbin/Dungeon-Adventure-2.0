import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from View import View
from Hero import Hero, Warrior, Priestess, Thief
from Monster import Monster
from Dungeon import Dungeon


class TestView(unittest.TestCase):
    """ Tests for View class """

    def setUp(self):
        """ set up for View Test class """
        self.view = View()

    def assert_stdout(self, expected_output, function_to_test):
        """ Asserts that the standard output produced by the given function matches the expected output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            function_to_test()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_introduction(self):
        """ Test for introduction method"""
        expected_output = "\nWelcome to the Dungeon Adventure Game, where you may traverse a dangerous maze in hopes of finding\nthe 4 pillars of Object Oriented Programing (OOP) - Abstraction, Encapsulation, Inheritance, and\nPolymorphism. Within the dungeon's maze you will find surprises, such as healing potions, vision\npotions, monsters, or pits. Items will be stored and healing potions can be used to increase\nyour HP, or health points. The Vision potion allows you to see through the walls of surrounding\n rooms. Falling into a pit will lower your HP. You will also battle powerful monsters.Be careful\nnot to die and lose the game. Survive, find all pillars of OOP and make it to the exit to win. \n \nTo travel, press keys w for Up, s for Down, a for Left, and d for Right. \nPress \"m\" to view menu options for legend key.\n\n"
        self.assert_stdout(expected_output, self.view.introduction)

    def test_row_col(self):
        """ Tests row_col method using patch """
        expected_output = "Row/Column dimension must not be smaller than 2\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.view.row_col()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_get_play_saved_game_yes(self):
        """ Tests get_play_saved_game method using patch for yes input """
        with patch('builtins.input', return_value='yes'):
            result = self.view.get_play_saved_game()
            self.assertEqual(result, 'yes')

    def test_get_play_saved_game_no(self):
        """ Tests get_play_saved_game method using patch for no input """
        with patch('builtins.input', return_value='no'):
            result = self.view.get_play_saved_game()
            self.assertEqual(result, 'no')

    def test_play_again_yes(self):
        """ Tests play_again method using patch for yes input"""
        with patch('builtins.input', return_value='y'):
            result = self.view.play_again()
            self.assertEqual(result, 'y')

    def test_play_again_no(self):
        """ Tests play_again method using patch for no input"""
        with patch('builtins.input', return_value='n'):
            result = self.view.play_again()
            self.assertEqual(result, 'n')

    def test_input_player_mode_easy(self):
        """ Tests input_player mode for easy input using patch"""
        with patch('builtins.input', return_value='easy'):
            result = self.view.input_player_mode()
            self.assertEqual(result, 'easy')

    def test_input_player_mode_medium(self):
        """ Tests input_player mode for medium input using patch"""
        with patch('builtins.input', return_value='medium'):
            result = self.view.input_player_mode()
            self.assertEqual(result, 'medium')

    def test_input_player_mode_hard(self):
        """ Tests input_player mode for hard input using patch"""
        with patch('builtins.input', return_value='hard'):
            result = self.view.input_player_mode()
            self.assertEqual(result, 'hard')

    def test_input_player_mode_choice(self):
        """ Tests input_player mode for choice input using patch"""
        with patch('builtins.input', return_value='choice'):
            result = self.view.input_player_mode()
            self.assertEqual(result, 'choice')

    def test_input_player_mode_default(self):
        """ Tests input_player mode for default input using patch"""
        with patch('builtins.input', return_value='easy'):
            result = self.view.input_player_mode()
            self.assertEqual(result, 'easy')  # Default value

    def test_continue_or_not(self):
        """ Tests continue or not method """
        with patch('builtins.input', return_value='y'):
            result = self.view.continue_or_not()
            self.assertEqual(result, 'y')

    def test_no_health_potion(self):
        """ Tests no heath potion method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.view.no_health_potion()
            self.assertEqual(mock_stdout.getvalue().strip(), "You don't have any health potions left")

    def test_desired_health_points(self):
        """ Test desired health points method"""
        with patch('builtins.input', return_value='100'):
            result = self.view.desired_health_points()
            self.assertEqual(result, '100')

    def test_special_attack_results_warrior_success(self):
        """ Tests special attack success method"""
        hero = Warrior("Warrior", hit_points=100, attack_speed=1, chance_to_hit=0.5, minimum_damage=40
                       , maximum_damage=80, healing_potion_count=3, vision_potion_count=2, pillar_count=1
                       , chance_to_block=0.4)
        monster = Monster("Ogre", hit_points=50, name="Ogre", attack_speed=2, chance_to_hit=0.5, minimum_damage=40,
                          maximum_damage=80, chance_to_heal=0.5, minimum_heal_points=50, maximum_heal_points=100
                          , heal_points=20, has_fainted=False)
        result = {"success": True, "attacker": "Warrior", "damage": 25}
        expected_output = "Warrior performs a Crushing Blow for 25 damage points. Warrior has 100HP and Ogre has 50HP"

        with patch('builtins.print') as mock_print:
            self.view.special_attack_results(result, hero, "Warrior", monster)
            mock_print.assert_called_once_with(expected_output)

    def test_special_attack_results_warrior_failure(self):
        """ Tests special attack failure method"""
        hero = Warrior("Warrior", hit_points=100, attack_speed=1, chance_to_hit=0.5, minimum_damage=40
                       , maximum_damage=80, healing_potion_count=3, vision_potion_count=2, pillar_count=1
                       , chance_to_block=0.4)
        monster = Monster("Ogre", hit_points=50, name="Ogre", attack_speed=2, chance_to_hit=0.5, minimum_damage=40,
                          maximum_damage=80, chance_to_heal=0.5, minimum_heal_points=50, maximum_heal_points=100
                          , heal_points=20, has_fainted=False)
        result = {"success": False, "attacker": "Warrior"}
        expected_output = "Warrior couldn't perform Crushing Blow"

        with patch('builtins.print') as mock_print:
            self.view.special_attack_results(result, hero, "Warrior", monster)
            mock_print.assert_called_once_with(expected_output)

    def assert_stdout_dungeon(self, expected_output, function_to_test, dungeon):
        """ assert stdout for dungeon """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            function_to_test(dungeon)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_play_dungeon(self):
        """ Tests dungeon printing"""
        # Create a Dungeon instance with dimensions 3x3
        dungeon = Dungeon(3, 3)

        expected_output = '^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n\n^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n\n^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n^^^  ^^^  ^^^  \n\n'

        self.assert_stdout_dungeon(expected_output, View.print_play_dungeon, dungeon)

    def test_attack_mode(self):
        """ Test attack mode method from View and compare the output"""
        troll_monster = Monster(monster_type="Troll", name="Ragnok", hit_points=100, attack_speed=0.5,
                                chance_to_hit=0.3, minimum_damage=40, maximum_damage=80, chance_to_heal=0.6,
                                minimum_heal_points=50, maximum_heal_points=100, heal_points=30, has_fainted=False)

        # Expected output
        expected_output = """_______  
 ((      ))    _______
 ((      ))   /_     _\\
 ((      ))   \\|0   0|/
  __(())__    (_  ^  _)
   ( () )   /`\\ |\"\"\"|/`\\
     {}____/  / _____/  /
     () ____/\\    =(   /\\
     {}    /  \\_/\\=/\\_/  \\
     {}    /  \\_/\\=/\\_/  \\"""

        with patch('builtins.input', return_value=''):  # Mocking input function
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:

                View.attack_mode(troll_monster)

                # Capture the actual output
                actual_output = mock_stdout.getvalue().strip()

                # Assert that the actual output matches the expected output
                self.assertEqual(actual_output, expected_output)

    def test_end(self):
        """ Tests end printing"""
        expected_output = "\n\nThank you for playing Dungeon Adventure. \nThis game was created by\n\nAqueno Nirasmi Amalraj \nMinna Chae \nSarah St. Albin \n\nA special thanks to our instructors \n\nTom Capaul \nKevin Anderson \nVarik Hoang \nRobert Cordingly \nAshutosh Engavle\n\nWe could not have done it without you.\n"
        self.assert_stdout(expected_output, self.view.end)


if __name__ == '__main__':
    unittest.main()
