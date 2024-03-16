"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

import copy
import pickle
import random

from Dungeon import Dungeon
from DungeonCharacterFactory import DungeonCharacterFactory
from DungeonItemsFactory import DungeonItemsFactory
from View import View

""" 
Dungeon Adventure contains the main logic of playing the game. 
Game play must be initiated by creating an instance of the class and calling the module 
play_whole_game. This file
will have the set up created after the class.

This game provides 4 levels, Easy, Medium, Hard, and Player's Choice.
Player's choice allows the player to choose any HP, healing potion, vision potion, and dungeon size as long as the
dungeon size is equal to or larger than 3x3. HP can be negative but player will instantly die.
Healing and vision potions can be negative but that will count against player.

Players can use the Action menu option to view keyboard inserts "Action Menu": "m", "Go Up": 
"w", "Go Down": "s", "Go Left": "a", "Go Right": "d", "Use Health Potion": "h", "Use Vision": 
"v", "View current status": "stats", "Map Display": "map", "Quit Game": "q". There are also hidden inputs and monster
fighting inputs that can be displayed within the game.

Each time a player moves, the output will be a display of the map that does not reveal any information about the room. 
Traveled Rooms will be  indicated by the notation --- and not yet traveled rooms will be indicated by the notation ^^^.
Player's current location will display the current layout of the room. T

If a player picks up items or falls into a pit, a print statement will indicate these added or
negative points. If a player encounters monsters, the menu option will appear and the player can fight.

"""


class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go Up": "w", "Go Down": "s", "Go Left": "a", "Go Right": "d",
                     "Use Health Potion": "h", "Use Vision": "v", "Normal Attack": "1", "Special Attack": "2",
                     "View current status": "stats", "Map Display": "map", "Save Game": "save", "Quit Game": "q"}
        self.cheat = {"Map display": "cheat map", "win": "win the game!", "lose 1": "lose with pillar", "lose 2": "lose with maze", "lose 3": "lose completely",
                      "+100 vision potions": "visions", "+1000 HP": "healings", "kill monsters": "kill"}
        self.hidden_menu_option = "map"  # prints dungeon
        self.dungeon = Dungeon(5, 5)
        self.view = View()
        self.hero = DungeonCharacterFactory.create_character("priestess", "Priestess")
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.original_dungeon = copy.deepcopy(self.dungeon)
        self.item = DungeonItemsFactory()
        self.player_name = "Player One"

    def play_whole_game(self):
        """
        Plays full game from top to bottom
        :return: None
        """
        self.view.introduction()
        play = "y"
        while play.lower() == "y" or play.lower() == "yes":
            game_type = self.view.get_play_saved_game()  # need to add error handling
            if game_type == 'y' or game_type == 'yes':
                no_saved_game = self.play_saved_game()
                if no_saved_game:
                    self.view.print_no_saved_game()
                    self.set_play_mode()
                    self.set_up_player()
                    self.view.menu_str(self.menu_str())
            else:
                self.set_play_mode()
                self.set_up_player()
                self.view.menu_str(self.menu_str())
            self.player_command()
            self.view.print_original_and_player_maze(self.original_dungeon, self.dungeon)
            self.player_results()
            play = self.view.play_again()
        self.view.end()

    def set_play_mode(self):
        """
        Setting up play mode level based on user input. Adventure attributes health, health potion count,
        vision potion count, dungeon dimension are set up in this module
        :return: None
        # """
        input_player = self.view.input_player()
        if input_player.lower() == "warrior" or input_player.lower() == "w":
            self.hero = DungeonCharacterFactory.create_character("warrior", "Warrior")
        elif input_player.lower() == "priestess" or input_player.lower() == "p":
            self.hero = DungeonCharacterFactory.create_character("priestess", "Priestess")
        else:
            self.hero = DungeonCharacterFactory.create_character("thief", "Thief")

        input_play_mode = self.view.input_player_mode()
        if input_play_mode == "medium" or input_play_mode == "m":
            healing_potion_count = random.randint(3, 10)
            vision_potion_count = random.randint(3, 10)
            self.dungeon = Dungeon(10, 10)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            self.view.medium_level()
        elif input_play_mode == "hard" or input_play_mode == "h":
            healing_potion_count = 5
            vision_potion_count = 5
            self.dungeon = Dungeon(15, 15)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            self.view.hard_level()
        elif input_play_mode == "choice" or input_play_mode == "c":
            while True:
                choice = self.view.desired_health_points()
                try:
                    HP = int(choice)
                    if HP < 0:
                        HP = 0
                    self.hero.hit_points = HP
                    break
                except ValueError:
                    self.view.number()
            while True:
                choice = self.view.health_potion_count()
                try:
                    healing_potion_count = int(choice)
                    if healing_potion_count < 0:
                        healing_potion_count = 0
                    break
                except ValueError:
                    self.view.number()
            while True:
                choice = self.view.vision_potion_count()
                try:
                    vision_potion_count = int(choice)
                    if vision_potion_count < 0:
                        vision_potion_count = 0
                    break
                except ValueError:
                    self.view.number()
            while True:
                row = self.view.row_input()
                try:
                    row = int(row)
                    if row >= 3:
                        break
                    else:
                        self.view.row_col()
                except ValueError:
                    self.view.number()

            while True:
                col = self.view.col_input()
                try:
                    col = int(col)
                    if col >= 3:
                        break
                    else:
                        self.view.row_input()
                except ValueError:
                    self.view.number()

            self.dungeon = Dungeon(int(row), int(col))
            self.original_dungeon = copy.deepcopy(self.dungeon)
            self.view.player_choice(row, col)

        else:
            healing_potion_count = random.randint(20, 30)
            vision_potion_count = random.randint(15, 20)
            self.dungeon = Dungeon(5, 5)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            self.view.easy_level()

        self.player_name = self.view.player_name() + " the "
        # self.hero.player_name(name)
        self.hero.healing_potion_count = healing_potion_count
        self.hero.vision_potion_count = vision_potion_count
        self.view.player_stats(self.player_name, self.hero)

    def menu_str(self):
        """
        Creates and returns the menu string. Hidden menu option "map" prints dungeon map
        :return: str
        """
        formatted_list = ["    " + item + " : " + values for item, values in self.menu.items()]
        return "\n".join(formatted_list) + "\n"

    def cheat_list(self):
        """
        Creates and returns the menu string. Hidden menu option "map" prints dungeon map
        :return: str
        """
        formatted_list = ["    " + item + " : " + values for item, values in self.cheat.items()]
        return "\n".join(formatted_list) + "\n"

    def player_name_str(self):
        """
        Creates Hero's name
        """
        return self.player_name + str(self.hero.name)

    def set_up_player(self):
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        :return: None
        """
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).player_traveled = True

    def player_command(self):
        """
        Execute player's menu inputs
        :return: None
        """

        response = ""
        if self.hero.hit_points > 0:
            self.print_play()

        while self.hero.hit_points > 0:
            room = self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col))
            menu_command = self.view.next_move()
            # while still in maze and not quit
            # quits game
            if menu_command == "q":
                break
            # prints menu
            # elif menu_command == 'clear':
            #     self.view.clear_screen()
            elif menu_command == "m":
                self.view.menu_str(self.menu_str())
            # use health potion
            elif menu_command == 'cheat sheet':
                self.view.cheat_list(self.cheat_list())
            elif menu_command == "h":
                    self.use_healing_potion()
            # use vision potion
            elif menu_command == "v":
                if self.hero.vision_potion_count > 0:
                    self.hero.vision_potion_count -= 1
                    vision_str = self.item.create_item("V").use_vision(self.player_loc_row, self.player_loc_col,
                                                          self.dungeon)  # self.dungeon.get_col_length, self.dungeon.get_row_length,
                    self.view.print_vision(vision_str)
                else:
                    self.view.no_vision_potion()
            # print hero statistics
            elif menu_command == "stats":
                self.view.player_stats(self.player_name, self.hero)
            # move hero in dungeon
            elif menu_command == "win the game!":
                self.hero.pillar_count = 4
                self.dungeon.get_room_str(
                    (self.dungeon.get_row_length() - 1, self.dungeon.get_col_length() - 1)).current_room = True
                break

            elif menu_command == "lose with pillar":
                self.hero.pillar_count = 4
                self.dungeon.get_room_str(
                    (self.dungeon.get_row_length() - 1, self.dungeon.get_col_length() - 1)).current_room = False
                break
            elif menu_command == "lose with maze":
                self.dungeon.get_room_str(
                    (self.dungeon.get_row_length() - 1, self.dungeon.get_col_length() - 1)).current_room = True
                self.hero.pillar_count = 2
                break

            elif menu_command == "lose completely":
                self.hero.pillar_count = 2
                self.dungeon.get_room_str(
                    (self.dungeon.get_row_length() - 1, self.dungeon.get_col_length() - 1)).current_room = False
                break

            elif (menu_command == "w" or menu_command == "a" or menu_command == "s" or
                  menu_command == "d"):
                #
                # moving character
                room = self.move_hero(menu_command)

                # if the player dies the game end
                if self.hero.hit_points <= 0:
                    break
                # reached exit, ask to leave game
                elif room.exit:
                    self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = True
                    while True:
                        response = self.view.continue_or_not()
                        if response == "y" or response == "yes":
                            break
                        elif response == "pillar":
                            self.view.pillar_count(self.hero.pillar_count)
                        elif response.lower() == "n" or response.lower() == "no":
                            self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = False
                            break
                if response.lower() == "y" or response.lower() == "yes":
                    break
            # cheat test
            elif menu_command == "visions":
                self.hero.vision_potion_count += 100
            elif menu_command == "healings":
                self.hero.healing_potion_count += 1000
            elif menu_command == 'save':
                self.view.save_game_message()
                self.send_save_data()
            elif str(menu_command).lower() == 'map':
                self.print_play()
            elif str(menu_command).lower() == "cheat map":
                # Secret menu prints map and uses @ for player location
                self.print_dungeon()
            else:
                self.view.not_valid_command()

    def use_healing_potion(self):
        """
        Creates a healing potion and uses the healing potion on hero when called
        return: none
        """
        if self.hero.healing_potion_count > 0:
            health_points = self.item.create_item("H", 20, 100).use_item()
            self.hero.hit_points += health_points
            self.hero.healing_potion_count -= 1
            self.view.gained_health_points(health_points, self.hero.hit_points, self.hero.healing_potion_count)
        else:
            self.view.no_health_potion()


    def move_hero(self, menu_command="g"):
        """
        Player's input is a direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible, collect items and make traveled rooms empty unless pit
        :return: Room
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
        room = self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col))
        print(room)
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
                self.print_play()
                self.view.print_room(self.dungeon.get_room_str((new_row, new_col)))
                room = self.dungeon.get_room_str(
                    (self.player_loc_row, self.player_loc_col))  # item = get room content, array
                room = self.collect_item(room)  # item = get room content, array
                return room
            else:
                self.view.no_door()
                return room

        else:
            self.view.not_valid_direction()
            return room

    def collect_item(self, room):
        """
        Items in room affects the player and returns item str if needed
        :return: Room
        """

        # boss_type = ["Troll", "Chimera", "Dragon"]
        troll_names = ["Ragnok", "Grimbash", "Boulderfist", "Groggnar", "Gnarlgrip"]
        chimera_names = ["Hydra", "Nemean", "Typhon", "Thrawn", "Gryphon"]
        dragon_names = ["Drakar", "Fafnir", "Volcanor", "Pyrax", "Vritra"]
        ogre_names = ["Grommash", "Throg", "Grokk", "Ugg", "Gronk"]
        gremlin_names = ["Gizmo", "Spike", "Scratch", "Snaggletooth", "Gnash"]
        skeleton_names = ["Skeletor", "Deathclaw", "Rattlebones",
                          "Skullcrack", "Dreadbone"]

        if room.healing_potion:
            self.hero.healing_potion_count += 1
            room.healing_potion = False
            self.view.total_healing_potion(self.hero.healing_potion_count)
            # self.dungeon.set_empty_room((self.player_loc_row, self.player_loc_col)) #removing item from dungeon
            # Collect Vision potion

        # # Collect Vision potion
        if room.vision_potion:
            self.hero.vision_potion_count += 1
            room.vision_potion = False
            self.view.total_vision_potion(self.hero.vision_potion_count)
        # Encounter Pit
        if room.pit:
            pit_points = self.item.create_item("X", 1, 15)
            self.hero.hit_points -= pit_points.use_item()  # check if it returns negative
            self.view.fell_in_pit(pit_points.use_item(), self.hero.hit_points)
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room
        if room.ogre:
            ogre_name = random.choice(ogre_names)
            o_monster = DungeonCharacterFactory.create_character("ogre", ogre_name)
            self.fight(o_monster)
            if o_monster.has_fainted:
                room.ogre = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room
        if room.gremlin:
            gremlin_name = random.choice(gremlin_names)
            g_monster = DungeonCharacterFactory.create_character("gremlin", gremlin_name)
            self.fight(g_monster)
            if g_monster.has_fainted:
                room.gremlin = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room
        if room.skeleton:
            skeleton_name = random.choice(skeleton_names)
            s_monster = DungeonCharacterFactory.create_character("skeleton", skeleton_name)
            self.fight(s_monster)
            if s_monster.has_fainted:
                room.skeleton = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room

        if room.dragon:
            dragon_name = random.choice(dragon_names)
            d_monster = DungeonCharacterFactory.create_character("dragon", dragon_name)
            self.fight(d_monster)
            if d_monster.has_fainted:
                room.dragon = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room

        if room.chimera:
            chimera_name = random.choice(chimera_names)
            c_monster = DungeonCharacterFactory.create_character("chimera", chimera_name)
            self.fight(c_monster)
            if c_monster.has_fainted:
                room.chimera = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room

        if room.troll:
            troll_name = random.choice(troll_names)
            t_monster = DungeonCharacterFactory.create_character("troll", troll_name)
            self.fight(t_monster)
            if t_monster.has_fainted:
                room.troll = False
            if self.hero.hit_points <= 0:
                room.player_traveled = True
                return room
        if room.abstraction_pillar:  # abstraction
            self.hero.pillar_count += 1
            room.abstraction_pillar = False
            self.view.found_pillar(self.hero.pillar_count, "a")
        # collect polymorphism pillar
        if room.inheritance_pillar:
            self.hero.pillar_count += 1
            room.inheritance_pillar = False
            self.view.found_pillar(self.hero.pillar_count, "i")
        # collect inheritance pillar
        if room.polymorphism_pillar:  # inheritance
            self.hero.pillar_count += 1
            room.polymorphism_pillar = False
            self.view.found_pillar(self.hero.pillar_count, "p")
        # collect encapsulation pillar
        if room.encapsulation_pillar:  # encapsulation
            self.hero.pillar_count += 1
            room.encapsulation_pillar = False
            self.view.found_pillar(self.hero.pillar_count, "e")
        # find exit
        if room.exit:
            self.view.found_exit()
            room.player_traveled = True
            return room
        if self.hero.hit_points <= 0:
            room.player_traveled = True
            return room
        room.player_traveled = True
        return room

    def fight(self, monster):
        """
        Hero and monster fight method. Takes the input to determine which move to make
        return: None
        """
        move = self.view.attack_mode(monster)
        while self.hero.hit_points > 0 or not monster.has_fainted:
            if move == "healings":
                self.hero.hit_points += 1000
            elif move == 'n' or move == "normal" or move == '1':
                result = self.hero.attack(monster)
                self.view.display_attack_result(result, self.hero, self.player_name_str(), monster)
                result = monster.heal()
                self.view.monster_heal(result)
                result = monster.attack(self.hero)
                self.view.display_attack_result(result, self.hero,self.player_name_str(), monster)

                if self.hero.hit_points <= 0:
                    self.view.lost()
                    break
                if monster.has_fainted():
                    self.view.monster_dead(monster)
                    break
            elif move == 's' or move == 'special' or move == '2':
                result = self.hero.special_skill(monster)
                self.view.special_attack_results(result, self.hero,self.player_name_str(), monster)
                result = monster.heal()
                self.view.monster_heal(result)
                result = monster.attack(self.hero)
                self.view.display_attack_result(result, self.hero,self.player_name_str(), monster)

                if self.hero.hit_points <= 0:
                    break
                if monster.has_fainted():
                    self.view.monster_dead(monster)
                    break
            elif move == '3' or move == 'h':
                self.use_healing_potion()
            elif move == "stats" or move == '4':
                self.view.player_stats(self.player_name, self.hero)
            elif move == 'q' or move == 'quit':
                break
            elif move == 'help':
                self.view.attack_help()
            elif move == 'kill':
                monster.hit_points = 0
                monster.has_fainted()
                self.view.monster_dead(monster)
                break
            else:
                self.view.not_valid_command()
            move = self.view.next_attack()

    def player_results(self):

        """
        Game has ended and prints hero results
        :return: None
        """
        end_maze = self.dungeon.get_room_str((self.dungeon.get_row_length()-1,self.dungeon.get_col_length()-1)).current_room
        self.view.game_results(self.hero.pillar_count, end_maze)
        see_stats = self.view.see_stats()
        if see_stats == "y" or see_stats == "yes":
            self.view.player_stats(self.player_name, self.hero)
        else:
            self.view.not_see_stats()

        ####New  print out -------------------------------------------
        save_game = self.view.save_game()
        if save_game.lower() == "y" or save_game.lower() == "yes":
            self.dungeon.get_room_str((self.dungeon.get_row_length()-1,self.dungeon.get_col_length()-1)).current_room = False
            self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = False
            self.send_save_data()
        else:
            self.view.dont_save_game()

    def send_save_data(self):
        """
        Saves the game with pickle
        Return: None
        """
        with open('saved.pickle', 'wb') as saved_file:
            pickle.dump(self, saved_file)

    def print_play(self):
        """
        Calls View to print the playing dungeon map that does not show items
        return: None
        """
        self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = True
        self.view.print_play_dungeon(self.dungeon)
        self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = False

    def print_dungeon(self):
        """
        Calls view to print the dungeon with items in view
        return: None
        """
        self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = True
        self.view.print_view(self.dungeon)
        self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)).current_room = False

    def play_saved_game(self):
        """
        Reloads and sets up the previously saved dungeon game
        Returns: Boolean
        """
        try:
            with open('saved.pickle', 'rb') as saved_file:
                read_saved_game = pickle.load(saved_file)
                # self = read_saved_game
            self.dungeon = read_saved_game.dungeon
            self.hero = read_saved_game.hero
            self.player_loc_col = read_saved_game.player_loc_col
            self.player_loc_row = read_saved_game.player_loc_row
            self.original_dungeon = read_saved_game.original_dungeon
            self.player_name = read_saved_game.player_name
        except pickle.UnpicklingError as e:
            # normal, somewhat expected
            self.view.no_save_game_found()
            return True
        except (AttributeError, EOFError, ImportError, IndentationError, IndexError, TypeError, ValueError) as e:
            # secondary errors
            self.view.not_valid_file()
            return False
            # print(traceback.format_exc(e))
        except Exception as e:
            # everything else, possibly fatal
            # print(traceback.format_exc(e))
            self.view.error_pickling()
            return False


if __name__ == "__main__":
    game_play = DungeonAdventure()
    game_play.play_whole_game()

