"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""
import traceback

from Hero import Warrior, Priestess, Thief
from Dungeon_Model import DungeonModel
from Dungeon_Items_Factory import DungeonItemsFactory
# import random
import sys, time, copy, random, pickle
# import copy
# import pickle
from SaveGame import pickle, SaveGame
from View import View

""" 
Dungeon Adventure contains the main logic of playing the game. 
Game play must be initiated by creating an instance of the class and calling the module 
play_whole_game. This file
will have the set up created after the class.

This game provides 4 levels, Easy, Medium, Hard, and Player's Choice.
Easy provides a 5x5 dungeon maze with the player at 100 HP, 3 healing potions, random vision
potions between 1 and 3. Medium provides a 10x10 dungeon maze with the player at random 
generated HP of 75 to 100, random healing potions of 0 to 2, and random vision potions 
of 0 to 1. Hard provides a 15x15 dungeon maze with the player at random 
generated HP of 75 to 90, 0 healing potions, and 0 vision potions. Player's choice allows
the player to choose any HP, healing potion, vision potion, and dungeon size as long as the
dungeon size is equal to or larger than 3x3. HP can be negative but player will instantly die.
Healing and vision potions can be negative but that will count against player.

Players can use the Action menu option to view keyboard inserts "Action Menu": "m", "Go Up": 
"w", "Go Down": "s", "Go Left": "a", "Go Right": "d", "Use Health Potion": "h", "Use Vision": 
"v", "View current status": "stats", "Quit Game": "q". The hidden/secret menu option is "map"
which will print the whole map and item layout.

Each time a player moves, the output will be a display of the map. Traveled Rooms will be 
indicated by the notation --- and not yet traveled rooms will be indicated by the notation ^^^.
Player's current location will display the current layout of the room. There is also a print
of only the current room after the map layout.

If a player picks up items or falls into a pit, a print statement will indicate these added or
negative points.

"""


class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go Up": "w", "Go Down": "s", "Go Left": "a", "Go Right": "d",
                     "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit Game": "q"}
        self.hidden_menu_option = "map"  # prints dungeon
        self.dungeon = DungeonModel(5, 5)
        self.hero = Warrior()
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.original_dungeon = copy.deepcopy(self.dungeon)
        self.item = DungeonItemsFactory()
        self.play_whole_game()

    def play_whole_game(self):
        """
        Plays full game from top to bottom
        :return: None
        """
        self.print_introduction()
        play = "y"
        while play.lower() == "y" or play.lower() == "yes":
            game_type = View.get_play_saved_game()

            if game_type == 'y' or game_type == 'yes':
                no_saved_game = self.play_saved_game()
                """---- added 2/27/24---"""
                if no_saved_game:
                    View.print_no_saved_game()

                    self.set_play_mode()
                    self.set_up_player()
                    View.menu_str(self.menu_str())

            else:
                self.set_play_mode()
                self.set_up_player()
                View.menu_str(self.menu_str())

            View.print_play_dungeon(self.player_loc_row, self.player_loc_col)
            self.player_command()
            View.print_original_and_player_maze(self.original_dungeon, self.dungeon)  # needs work

            self.player_results()
            play = View.play_again()

    def print_introduction(self):
        """
        Prints Introduction and game play
        """
        View.introduction()

    def set_play_mode(self):
        """
        Setting up play mode level based on user input. Adventure attributes health, health potion count,
        vision potion count, dungeon dimension are set up in this module
        :return: None
        """
        input_player = View.input_player()

        if input_player.lower() == "Warrior" or input_player.lower() == "w":
            self.hero = Warrior()
        if input_player.lower() == "Priestess" or input_player.lower() == "p":
            self.hero = Priestess()
        if input_player.lower() == "Thief" or input_player.lower() == "t":
            self.hero = Thief()
        input_play_mode = View.input_player_mode()

        if input_play_mode.lower() == "medium" or input_play_mode.lower() == "m":
            healing_potion_count = random.randint(0, 2)
            vision_potion_count = random.randint(0, 1)
            self.dungeon = DungeonModel(10, 10)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            View.medium_level()

        elif input_play_mode.lower() == "hard" or input_play_mode.lower() == "h":
            healing_potion_count = 0
            vision_potion_count = 0
            self.dungeon = DungeonModel(15, 15)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            View.hard_level()

        elif input_play_mode.lower() == "choice" or input_play_mode.lower() == "c":
            while True:
                choice = View.desired_health_points()
                try:
                    HP = int(choice)
                    self.hero.hit_points = HP
                    break
                except ValueError:
                    View.number()

            while True:
                choice = View.health_potion_count()
                try:
                    healing_potion_count = int(choice)
                    break
                except ValueError:
                    View.number()

            while True:
                choice = View.vision_potion_count()
                try:
                    vision_potion_count = int(choice)
                    break
                except ValueError:
                    View.number()

            while True:
                row = View.row_input()
                try:
                    row = int(row)
                    if row >= 3:
                        break
                    else:
                        View.row_col()

                except ValueError:
                    View.number()

            while True:
                col = View.col_input()
                try:
                    col = int(col)
                    if col >= 3:
                        break
                    else:
                        View.row_col()

                except ValueError:
                    View.number()

            self.dungeon = DungeonModel(int(row), int(col))
            self.original_dungeon = copy.deepcopy(self.dungeon)
            View.player_choice(row, col)

        else:
            healing_potion_count = 3
            vision_potion_count = random.randint(1, 3)
            self.dungeon = DungeonModel(5, 5)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            View.easy_level()

        name = View.your_name()
        self.hero.hero_name = name
        self.hero.healing_potion_count = healing_potion_count
        self.hero.vision_potion_count = vision_potion_count
        View.your_stats(self.hero)

    def menu_str(self):
        """
        Creates and returns the menu string. Hidden menu option "map" prints dungeon map
        :return: str
        """
        formatted_list = ["    " + item + " : " + values for item, values in self.menu.items()]
        return "\n".join(formatted_list) + "\n"

    def set_up_player(self):
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        :return: None
        """
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.dungeon.player_traveled = (self.player_loc_row, self.player_loc_col)
        # self.dungeon.set_player_traveled((self.player_loc_row,self.player_loc_col))

    def player_command(self):
        """
        Execute player's menu inputs
        :return: None
        """
        response = ""
        if self.hero.hit_points > 0:
            View.print_play_dungeon(self.dungeon, self.player_loc_row, self.player_loc_col)

        while self.hero.hit_points > 0:
            menu_command = View.next_move()

            if menu_command.lower() == "q":

                break
            # prints menu
            elif str(menu_command).lower() == "m":
                View.menu_str(self.menu_str())
                # print(self.menu_str())
            # use health potion
            elif str(menu_command).lower() == "h":
                if self.hero.healing_potion_count > 0:
                    health_points = self.item.create_item("H", 1, 10).use_item()
                    self.hero.hit_points += health_points
                    self.hero.healing_potion_count -= 1
                    View.gained_health_points(health_points, self.hero.hit_points, self.hero.healing_potion_count)

                else:
                    View.no_health_potion()

            # use vision potion
            elif str(menu_command).lower() == "v":
                if self.hero.vision_potion_count > 0:
                    self.hero.vision_potion_count -= 1
                    self.item.create_item("V").use_vision(self.player_loc_row, self.player_loc_col,
                                                          self.dungeon.col_length, self.dungeon.row_length,
                                                          self.dungeon)
                else:
                    View.no_vision_potion()

            # print hero statistics
            elif str(menu_command).lower() == "stats":
                print(self.hero)
            # move hero in dungeon
            elif (menu_command.lower() == "w" or menu_command.lower() == "a" or menu_command.lower() == "s" or
                  menu_command.lower() == "d"):
                # moving character
                item = self.move_hero(menu_command)

                # if the player dies the game end
                if self.hero.hit_points <= 0:
                    break
                # reached exit, ask to leave game
                elif item == "O":
                    while True:
                        response = View.continue_or_not()

                        if response.lower() == "y" or response.lower() == "yes":
                            break
                        elif response.lower() == "pillar":
                            if self.hero.pillar_count == 1:
                                View.pillar_count(self.hero.pillar_count)
                            else:
                                View.pillar_count(self.hero.pillar_count)
                                # print(f"You have found {self.hero.pillar_count} pillars so far.")
                        elif response.lower() == "n" or response.lower() == "no":
                            break
                if response.lower() == "y" or response.lower() == "yes":
                    break
            elif str(menu_command).lower() == "map":
                # Secret menu prints map and uses @ for player location
                View.print_dungeon(self.player_loc_row, self.player_loc_col)
            else:
                View.not_valid_command()

    def move_hero(self, menu_command="g"):
        """
        Player's input is a direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible, collect items and make traveled rooms empty unless pit
        :return: str
        """
        # Getting direction
        if menu_command == "w":
            real_direction = "N"
        elif menu_command == "s":
            real_direction = "S"
        elif menu_command == "d":
            real_direction = "E"
        elif menu_command == "a":
            real_direction = "W"
        else:
            return menu_command
        # get coordinates for next move
        new_row, new_col = self.dungeon._return_neighbor_coordinates(self.player_loc_row, self.player_loc_col,
                                                                     real_direction)
        # checking to see if next move is going to an actual room
        if self.dungeon.is_valid_room(new_row, new_col):
            new_key = self.dungeon._return_neighbor_coordinates(self.player_loc_row, self.player_loc_col,
                                                                real_direction)
            current_key = self.player_loc_row, self.player_loc_col

            # If there is a door to enter into the next room
            if self.dungeon.show_doors(current_key, new_key, real_direction):
                self.player_loc_row, self.player_loc_col = new_row, new_col
                print(View.print_play_dungeon(self.player_loc_row, self.player_loc_col))
                print(self.dungeon.show_room_str((new_row, new_col)))
                self.dungeon.player_traveled = (self.player_loc_row, self.player_loc_col)
                item = self.dungeon.show_room_contents(
                    (self.player_loc_row, self.player_loc_col))  # item = get room content, str
                item = self.collect_item(item)  # item = get room content, str
                if item == "O":
                    View.found_exit()

                    return item
                if self.hero.hit_points <= 0:
                    View.lost()

                    return item
            else:
                View.no_door()


        else:
            View.not_valid_direction()

            return

    def collect_item(self, item="a"):
        """
        Items in room affects the player and returns item str if needed
        :return: str
        """
        # Collect Health potion
        if item == "H":
            self.hero.healing_potion_count += 1
            View.total_healing_potion(self.hero.healing_potion_count)
            # print(f"Picked up Healing Potion. Total Healing Potions: {self.hero.healing_potion_count}")
            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)  # removing item from dungeon
        # Collect Vision potion
        elif item == "V":
            self.hero.vision_potion_count += 1
            View.total_vision_potion(self.hero.vision_potion_count)

            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)
        # Encounter Pit
        elif item == "X":
            pit_points = self.item.create_item("X", 1, 15)
            self.hero.hit_points -= pit_points.use_item()  # check if it returns negative
            View.fell_in_pit(pit_points.use_item(), self.hero.hit_points)

        # find exit
        elif item == "O":
            return item
        # Collect multiple items
        elif item == "M":
            multi_items = self.dungeon.multi_item_room()
            # Health, vision, pit
            pit = False
            for value in multi_items:
                if item == "V":
                    self.hero.vision_potion_count += 1
                    View.total_vision_potion(self.hero.vision_potion_count)

                if value == "H":
                    self.hero.healing_potion_count += 1
                    View.total_healing_potion(self.hero.healing_potion_count)

                if value == "X":
                    pit_points = self.item.create_item("X", 1, 15)
                    self.hero.hit_points -= -pit_points.use_item()
                    View.fell_in_pit(pit_points.use_item(), self.hero.hit_points)

            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), pit)

        # collect Abstraction pillar
        elif item == "A":  # abstraction
            self.hero.pillar_count += 1
            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)
            View.found_abstraction_pillar(self.hero.pillar_count)

        # collect polymorphism pillar
        elif item == "P":
            self.hero.pillar_count += 1
            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)
            View.found_polymorphism_pillar(self.hero.pillar_count)

        # collect inheritance pillar
        elif item == "I":  # inheritance
            self.hero.pillar_count += 1
            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)
            View.found_inheritance_pillar(self.hero.pillar_count)

        # collect encapsulation pillar
        elif item == "E":  # encapsulation
            self.hero.pillar_count += 1
            self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col), False)
            View.found_encapsulation_pillar(self.hero.pillar_count)

        else:
            return item

    def player_results(self):

        """
        Game has ended and prints hero results
        :return: None
        """
        if self.hero.pillar_count == 4:
            View.won_the_game(self.hero.pillar_count)
        elif self.hero.pillar_count == 1:
            View.lost_game(self.hero.pillar_count)

        else:
            View.lost_game(self.hero.pillar_count)

        see_stats = View.see_stats()
        if see_stats.lower() == "y" or see_stats.lower() == "yes":
            print(self.hero)
        else:
            View.not_see_stats()

        ####New  print out -------------------------------------------
        save_game = View.save_game()
        if save_game.lower() == "y" or save_game.lower() == "yes":
            self.send_save_data()
            # self.send_save_data(self)
        else:
            View.dont_save_game()

    def play_saved_game(self):
        """
        Saves the currently running dungeon adventure game.
        Returns: Boolean if game was saved
        """
        try:
            with open('dungeon_adventure.pickle', 'rb') as saved_file:
                read_saved_game = pickle.load(saved_file)
            self.dungeon = read_saved_game.dungeon
            self.hero = read_saved_game.hero
            self.player_loc_col = read_saved_game.player_loc_col
            self.player_loc_row = read_saved_game.player_loc_row
            self.original_dungeon = read_saved_game.original_dungeon
        except pickle.UnpicklingError as e:
            # normal, somewhat expected
            View.no_save_game_found()

            return True
        except (AttributeError, EOFError, ImportError, IndentationError, IndexError, TypeError, ValueError) as e:
            # secondary errors
            View.not_valid_file()

            return True

        except Exception as e:
            # everything else, possibly fatal

            View.error_pickling()

            return True

    def print_end(self):
        """
        Prints closing title slides
        """
        View.end()

    # save game method pickle
    def send_save_data(self):
        save_game = SaveGame()
        save_game.pickle(self)


if __name__ == "__main__":
    game_play = DungeonAdventure()
    game_play.set_play_mode()
