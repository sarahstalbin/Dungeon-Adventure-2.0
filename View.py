# from Dungeon_Model import DungeonModel
import random

import Dungeon_Model
from Dungeon_Items_Factory import DungeonItemsFactory
# from DungeonAdventure import DungeonAdventure
# from Hero_Model_new import Warrior, Priestess, Thief
import sys, time, copy, random, pickle
from SaveGame import SaveGame


class View:
    # def __init__(self):
    #     # self.dungeon = dungeon
    #     self.dungeon = Dungeon_Model.DungeonModel(5, 5)
    #     self.dungeon_adventure = DungeonAdventure()

    @staticmethod
    def introduction():

        print("\nWelcome to the Dungeon Adventure Game, where you may traverse a dangerous maze in hopes \nof finding "
              "the 4 pillars of Object Oriented Programing (OOP) - Abstraction, Encapsulation, \nInheritance, "
              "and Polymorphism. Within the dungeon's maze you will find surprises, such \nas healing potions, "
              "vision potions, or pits. Items will be stored and healing potions \ncan be used to increase your HP, "
              "or health points. The Vision potion allows you to see \nthrough the walls of surrounding rooms. Falling "
              "into a pit will lower your HP. Be careful \nnot to die and lose the game. Survive and find all pillars of OOP to win. "
              "\n \nTo travel, press keys w for Up, s for Down, a for Left, and d for Right. "
              "\nPress \"m\" to view menu options for legend key.\n")

    # @staticmethod
    # def print_healing_potion():
    #     print(f"Picked up Healing Potion. Total Healing Potions: {self.hero.healing_potion_count}")
    @staticmethod
    def print_no_saved_game():
        print("There is no saved game. Please play a new game.")

    @staticmethod
    def number():
        print("\nMust be a number")

    @staticmethod
    def row_col():
        print("\nRow/Column dimension must not be smaller than 2")

    @staticmethod
    def print_original_and_player_maze(original, player):
        print("\nOriginal maze:\n")
        original.print_dungeon()
        print("Your maze:\n")
        player.print_dungeon()

    @staticmethod
    def get_play_saved_game():
        return input("Would you like to play the previously saved game? ").lower()

    @staticmethod
    def play_again():
        return input("Would you like to play again? \"y\" to keep playing or enter any key to exit. ")

    @staticmethod
    def input_player():
        return input(
            f"Please choose a Hero. Type \"Warrior\" or w, \"Priestess\" or p, and \"Thief\" or t ").lower()

    @staticmethod
    def input_player_mode():
        return input(
            f"Choose: Easy/e, Medium/m, Hard/h, or players choice (c/choice)? Default will be Easy. ").lower()

    @staticmethod
    def continue_or_not():
        return input("You have reached the exit. Would you like to leave the maze? (y to leave, "
                     "pillar to view pillar count, or n to stay: ")

    @staticmethod
    def no_health_potion():
        print("You don't have any health potions left")

    @staticmethod
    def desired_health_points():
        return input("Desired health points? ")

    @staticmethod
    def health_potion_count():
        return input("Healing Potion count? ")

    @staticmethod
    def vision_potion_count():
        return input("Vision Potion count? ")

    @staticmethod
    def row_input():
        return input("Row Dimension? Must be larger than 2. ")

    @staticmethod
    def col_input():
        return input("Column Dimension? Must be larger than 2. ")

    @staticmethod
    def your_name():
        return input("What is your name? ")

    @staticmethod
    def see_stats():
        return input("\nDo you want to see your stats? y/n ")

    @staticmethod
    def not_see_stats():
        print("I guess you'll never know")

    @staticmethod
    def save_game():
        return input("\nDo you want to save the game? y/n ")

    @staticmethod
    def dont_save_game():
        print("The game was never saved")

    @staticmethod
    def no_save_game_found():
        print("No saved game found")

    @staticmethod
    def not_valid_file():
        print("Not a valid file please try again")

    @staticmethod
    def error_pickling():
        print("Error in pickling")

    @staticmethod
    def next_move():
        return input("What is your next move? Enter \"m\" for menu: ")

    @staticmethod
    def no_vision_potion():
        print("You don't have any vision potions left")

    @staticmethod
    def easy_level():
        print(f"Play mode is Easy with dungeon dimension of 5x5")

    @staticmethod
    def medium_level():
        print(f"Play mode is Medium with dungeon dimension of 10x10")

    @staticmethod
    def hard_level():
        print(f"Play mode is Hard with dungeon dimension of 15x15")

    @staticmethod
    def found_exit():
        print("You found the exit to the dungeon")

    @staticmethod
    def lost():
        print("You have died and lost the game!")

    @staticmethod
    def no_door():
        print("Cannot move that direction because there is no door")

    @staticmethod
    def not_valid_direction():
        print("Not valid direction")

    @staticmethod
    def not_valid_command():
        print("Not a valid command")

    @staticmethod
    def gained_health_points(health_points, hit_points, healing_potion_count):
        print(f"You gained {health_points} health points! Your health is now "
              f"{hit_points} and you have "
              f"{healing_potion_count} left.")

    @staticmethod
    def pillar_count(pillar_count):
        print(f"You have found {pillar_count} pillar so far.")

    @staticmethod
    def total_healing_potion(healing_potion_count):
        print(f"Picked up Healing Potion. Total Healing Potions: {healing_potion_count}")

    @staticmethod
    def found_abstraction_pillar(pillar_count):
        print(f"You found the Abstraction pillar! Total Pillars: {pillar_count}")

    @staticmethod
    def found_polymorphism_pillar(pillar_count):
        print(f"You found the Polymorphism pillar! Total Pillars: {pillar_count}")

    @staticmethod
    def found_inheritance_pillar(pillar_count):
        print(f"You found the Inheritance pillar! Total Pillars: {pillar_count}")

    @staticmethod
    def found_encapsulation_pillar(pillar_count):
        print(f"You found the Encapsulation pillar! Total Pillars: {pillar_count}")

    @staticmethod
    def won_the_game(pillar_count):
        print(f"You won the game and found all {pillar_count} pillars!")

    @staticmethod
    def lost_game(pillar_count):
        print(f"Sorry, you only found {pillar_count} pillar. You have lost the game")

    @staticmethod
    def total_vision_potion(vision_potion_count):
        print(f"Picked up Healing Potion. Total Healing Potions: {vision_potion_count}")

    @staticmethod
    def player_choice(row, col):
        print(f"Play mode is Player's Choice with dungeon dimension of {row}x{col}")

    @staticmethod
    def fell_in_pit(pit_points, hit_points):
        print(f"You fell into a Pit! You lost {pit_points} points. Current HP: {hit_points}")

    @staticmethod
    def your_stats(hero):
        print(f"Your stats: {hero}")

    @staticmethod
    def menu_str(menu_str):
        # menu_str = DungeonAdventure().menu_str()
        print(menu_str)

    @staticmethod
    def display_hero_stats(hero):
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in hero.stats.items()]
        print("\n" + "\n".join(formatted_list) + "\n")

    @staticmethod
    def display_attack_result(result):
        if result["success"]:
            print(f"{result['attacker']} attacks {result['opponent']} for {result['damage']} damage points")
        else:
            print(f"{result['attacker']} couldn't attack {result['opponent']}")

    @staticmethod
    def warrior_attack_result(result):
        if result["success"]:
            print(f"{result['attacker']} performs a Crushing Blow for {result['damage']} damage points.")
        else:
            print(f"{result['attacker']} couldn't perform Crushing Blow")

    @staticmethod
    def priestess_attack_result(result):
        print(f" {result['attacker']} performs healing on {result['opponent']} for {result['heal']} heal points ")

    @staticmethod
    def thief_special_attack_result(result):
        if result["success"]:
            if result["attacks"] == 2:
                print(
                    f"{result['attacker']} attacked {result['opponent']} twice for {result['damage']} damage points. ")
            elif result["attacks"] == 1:
                print(f"{result['attacker']} attacked {result['opponent']} once for {result['damage']} damage points.")
            else:
                print(f"{result['attacker']} couldn't perform the special attack.")
        else:
            print(f"{result['attacker']} couldn't perform the special attack.")

    @staticmethod
    def gremlin_skeleton_heal(result):
        if result["success"]:
            if result["heal_amount"] > 0:
                print(f"The Gremlin {result['name']} has healed itself!")
            else:
                print(f"The Gremlin {result['name']} cannot heal itself, you're safe!")

    @staticmethod
    def print_dictionary(self):
        """
        Prints the contents of each Room without the symbols from Room's __str__() method.
        Uses the format (row, col) : contents.
        :return: None
        """
        symbols_dict = self.dungeon._get_object_symbols()
        for key, value in symbols_dict.items():
            print(f"Room at ({key[0]}, {key[1]}): {value}")

    @staticmethod
    def print_play_dungeon(self, dungeon, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze as player is playing
        :return: None.
        """
        top = []
        for row in range(dungeon.row_length):
            for col in range(dungeon.col_length):
                if row == current_row and col == current_col:
                    top.append(str(self.dungeon.maze[row][col])[0:3] + "  ")
                else:
                    if self.dungeon.items.get((row, col)).player_traveled:
                        top.append("---  ")
                    else:
                        top.append("^^^  ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.dungeon.row_length):
            for col in range(self.dungeon.col_length):
                if row == current_row and col == current_col:
                    if len(str(self.dungeon.maze[row][col])) == 10:
                        mid.append(str(self.dungeon.maze[row][col])[4:6] + "   ")
                    else:
                        mid.append(str(self.dungeon.maze[row][col])[4:7] + "  ")
                else:
                    if self.dungeon.items.get((row, col)).player_traveled:
                        mid.append("---  ")
                    else:
                        mid.append("^^^  ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.dungeon.row_length):
            for col in range(self.dungeon.col_length):
                if row == current_row and col == current_col:
                    if len(str(self.dungeon.maze[row][col])) == 10:
                        bottom.append(str(self.dungeon.maze[row][col])[7:10] + "  ")
                    else:
                        bottom.append(str(self.dungeon.maze[row][col])[8:11] + "  ")
                else:
                    if self.dungeon.items.get((row, col)).player_traveled:
                        bottom.append("---  ")
                    else:
                        bottom.append("^^^  ")

        # prints dungeon according to the dimensons
        for i in range(0, self.dungeon.row_length):
            # print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(bottom[room], end="")
            print("\n")

    @staticmethod
    def print_dungeon(self, dungeon, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze.
        :return: None.
        """
        # Saves top strings of all rooms in dungeon
        top = []
        for row in range(dungeon.row_length):
            for col in range(self.dungeon.col_length):
                top.append(str(self.dungeon.maze[row][col])[0:3] + "     ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.dungeon.row_length):
            for col in range(self.dungeon.col_length):
                if row == current_row and col == current_col:
                    current = str(self.dungeon.maze[row][col])[4]
                    current += "@"
                    current += str(self.dungeon.maze[row][col])[6] + "     "
                    mid.append(current)
                else:
                    if len(str(self.dungeon.maze[row][col])) == 10:
                        mid.append(str(self.dungeon.maze[row][col])[4:6] + "      ")
                    else:
                        mid.append(str(self.dungeon.maze[row][col])[4:7] + "     ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.dungeon.row_length):
            for col in range(self.dungeon.col_length):
                if len(str(self.dungeon.maze[row][col])) == 10:
                    bottom.append(str(self.dungeon.maze[row][col])[7:10] + "     ")
                else:
                    bottom.append(str(self.dungeon.maze[row][col])[8:11] + "     ")

        # prints dungeon according to the dimensions
        for i in range(0, self.dungeon.row_length):
            print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.dungeon.col_length, (i + 1) * self.dungeon.col_length):
                print(bottom[room], end="")
            print("\n")

    @staticmethod
    def end():
        """
                Prints closing title slides
                """
        time.sleep(.1)
        group_names = ("Aqueno Nirasmi Amalraj \nMinna Chae \nSarah St. Albin \n")
        teacher_names = ("Varik Hoang \nRobert Cordingly \nAshutosh Engavle")
        print("\n")
        print("Thank you for playing Dungeon Adventure. \nThis game was created by\n")
        for character in group_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\nA special thanks to our instructors \n")
        for character in teacher_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\n\nWe could not have done it without you.")

        # save game method pickle

    # def send_save_data(self):
    #     save_game = SaveGame()
    #     save_game.pickle(self)

# d = View()
# d.print_dungeon(1,1)
