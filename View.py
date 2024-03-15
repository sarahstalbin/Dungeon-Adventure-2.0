import sys, time, os


class View:

    @staticmethod
    def introduction():
        """ Prints the introduction in the controller class """

        print("\nWelcome to the Dungeon Adventure Game, where you may traverse a dangerous maze in hopes of finding"
              "\nthe 4 pillars of Object Oriented Programing (OOP) - Abstraction, Encapsulation, Inheritance, and"
              "\nPolymorphism. Within the dungeon's maze you will find surprises, such as healing potions, vision"
              "\npotions, monsters, or pits. Items will be stored and healing potions can be used to increase"
              "\nyour HP, or health points. The Vision potion allows you to see through the walls of surrounding"
              "\n rooms. Falling into a pit will lower your HP. You will also battle powerful monsters.Be careful"
              "\nnot to die and lose the game. Survive, find all pillars of OOP and make it to the exit to win. "
              "\n \nTo travel, press keys w for Up, s for Down, a for Left, and d for Right. "
              "\nPress \"m\" to view menu options for legend key.\n")

    @staticmethod
    def print_no_saved_game():
        """ Prints no saved game line in the controller class """
        print("There is no saved game. Please play a new game.")

    @staticmethod
    def number():
        """ Prints this method in the controller class to make sure it a number """
        print("Must be a number")

    @staticmethod
    def row_col():
        """ Prints this method in the controller class to get right dimension """
        print("Row/Column dimension must not be smaller than 2")

    @staticmethod
    def print_original_and_player_maze(original, player):
        """ Prints original and player maze in the controller class """
        print("\nOriginal maze:\n")
        print(original)
        print("Your maze:\n")
        print(player)

    @staticmethod
    def get_play_saved_game():
        """ Prints this method in the controller class to get input from the user """
        return input("Would you like to play the previously saved game? ").lower()

    @staticmethod
    def play_again():
        """ Prints this method in the controller class to get input from the user """
        return input("Would you like to play again? \"y\" to keep playing or enter any key to exit. ").lower()

    @staticmethod
    def input_player():
        """ Prints this method in the controller class to get input from the user """
        return input(
            f"Please choose a Hero. Type \"Warrior\" or w, \"Priestess\" or p, and \"Thief\" or t ").lower()

    @staticmethod
    def input_player_mode():
        """ Prints this method in the controller class to get input from the user """
        return input(
            f"Choose: Easy/e, Medium/m, Hard/h, or players choice (c/choice)? Default will be Easy. ").lower()

    @staticmethod
    def continue_or_not():
        """ Prints this method in the controller class to get input from the user """
        return input("You have reached the exit. Would you like to leave the maze? (y to leave, "
                     "pillar to view pillar count, or n to stay: ").lower()

    @staticmethod
    def no_health_potion():
        """ Prints this method in the controller class to indicate there is no health potion left """
        print("You don't have any health potions left")

    @staticmethod
    def desired_health_points():
        """ Prints this method in the controller class to get input from the user """
        return input("Desired health points? ")

    @staticmethod
    def health_potion_count():
        """ Prints this method in the controller class to get input from the user """
        return input("Healing Potion count? ")

    @staticmethod
    def vision_potion_count():
        """ Prints this method in the controller class to get input from the user """
        return input("Vision Potion count? ")

    @staticmethod
    def row_input():
        """ Prints this method in the controller class to get input from the user """
        return input("Row Dimension? Must be larger than 2. ")

    @staticmethod
    def col_input():
        """ Prints this method in the controller class to get input from the user """
        return input("Column Dimension? Must be larger than 2. ")

    @staticmethod
    def player_name():
        """ Prints this method in the controller class to get input from the user """
        return input("What is your name? ")

    @staticmethod
    def see_stats():
        """ Prints this method in the controller class to get input from the user """
        return input("\nDo you want to see your stats? y/n ").lower()

    @staticmethod
    def not_see_stats():
        """ Prints this method in the controller class  """
        print("I guess you'll never know")

    @staticmethod
    def save_game():
        """ Prints this method in the controller class to get input from the user """
        return input("\nDo you want to save the game? y/n ").lower()

    @staticmethod
    def save_game_message():
        """ Prints this method in the controller class to indicate the game is saved """
        print("Game Saved")

    @staticmethod
    def dont_save_game():
        """ Prints this method in the controller class to indicate the game is not saved """
        print("The game was never saved")

    @staticmethod
    def no_save_game_found():
        """ Prints this method in the controller class to indicate no saved game is found """
        print("No saved game found")

    @staticmethod
    def not_valid_file():
        """ Prints this method in the controller class to indicate it is not a valud file """
        print("Not a valid file please try again")

    @staticmethod
    def error_pickling():
        """ Prints this method in the controller class to indicate there is error in pickling """
        print("Error in pickling")

    @staticmethod
    def next_move():
        """ Prints this method in the controller class to get input from the user """
        return str(input("What is your next move? Enter \"m\" for menu: ").lower())

    @staticmethod
    def no_vision_potion():
        """ Prints this method in the controller class to indicate no vision potion is left"""
        print("You don't have any vision potions left")

    @staticmethod
    def no_healing_potion():
        """ Prints this method in the controller class to indicate no healing potion is left"""
        print("You don't have any healing potions left")

    @staticmethod
    def easy_level():
        """ Prints this method in the controller class for easy level """
        print(f"Play mode is Easy with dungeon dimension of 5x5")

    @staticmethod
    def medium_level():
        """ Prints this method in the controller class for medium level"""
        print(f"Play mode is Medium with dungeon dimension of 10x10")

    @staticmethod
    def hard_level():
        """ Prints this method in the controller class for hard level """
        print(f"Play mode is Hard with dungeon dimension of 15x15")

    @staticmethod
    def found_exit():
        """ Prints this method in the controller class """
        print("You found the exit to the dungeon")

    @staticmethod
    def lost():
        """ Prints this method in the controller class """
        print("You have died and lost the game!")

    @staticmethod
    def no_door():
        """ Prints this method in the controller class """
        print("Cannot move that direction because there is no door")

    @staticmethod
    def not_valid_direction():
        """ Prints this method in the controller class """
        print("Not valid direction")

    @staticmethod
    def not_valid_command():
        """ Prints this method in the controller class """
        print("Not a valid command")

    @staticmethod
    def gained_health_points(health_points, hit_points, healing_potion_count):
        """ Prints this method in the controller class """
        print(f"You gained {health_points} health points! Your health is now "
              f"{hit_points} and you have "
              f"{healing_potion_count} left.")

    @staticmethod
    def pillar_count(pillar_count):
        """ Prints this method in the controller class """
        if pillar_count == 1:
            print(f"You have found {pillar_count} pillar so far.")
        else:
            print(f"You have found {pillar_count} pillars so far.")

    @staticmethod
    def total_healing_potion(healing_potion_count):
        """ Prints this method in the controller class """
        print(f"Picked up Healing Potion. Total Healing Potions: {healing_potion_count}")

    @staticmethod
    def total_vision_potion(vision_potion_count):
        """ Prints this method in the controller class """
        print(f"Picked up Vision Potion. Total Vision Potions: {vision_potion_count}")

    @staticmethod
    def found_pillar(pillar_count, pillar_type):
        """ Prints how many pillars found in the controller class"""
        if pillar_type == "a":
            print(f"You found the Abstraction pillar! Total Pillars: {pillar_count}")
        elif pillar_type == "p":
            print(f"You found the Polymorphism pillar! Total Pillars: {pillar_count}")
        elif pillar_type == "i":
            print(f"You found the Inheritance pillar! Total Pillars: {pillar_count}")
        elif pillar_type == "e":
            print(f"You found the Encapsulation pillar! Total Pillars: {pillar_count}")
        else:
            print("That is not a pillar!")

    @staticmethod
    def game_results(pillar_count, end_maze):
        """ Prints game results in the controller class """
        if pillar_count == 1:
            print(f"Sorry, you only found {pillar_count} pillar. You have lost the game")
        elif pillar_count == 4 and end_maze:
            print(f"You won the game and found all {pillar_count} pillars!")
        elif pillar_count == 4:
            print \
                (f"Sorry, you only found {pillar_count} pillar but you couldn't finish the maze. You have lost the game")
        else:
            print(f"Sorry, you only found {pillar_count} pillars. You have lost the game")

    @staticmethod
    def player_choice(row, col):
        """ Prints this method in the controller class """
        print(f"Play mode is Player's Choice with dungeon dimension of {row}x{col}")

    @staticmethod
    def fell_in_pit(pit_points, hit_points):
        """ Prints this method in the controller class """
        print(f"You fell into a Pit! You lost {pit_points} points. Current HP: {hit_points}")

    @staticmethod
    def player_stats(player_name, hero):
        """ Prints Hero image in the controller class """
        if hero.name == 'Priestess':
            print("                        _____")
            print("                      /`.---.`\\")
            print("                     / /.---.\\ \\")
            print("                    ; |/ e e \\| ;")
            print("                    ; \\|  ^  |/ |")
            print("                    |   \\_=_/   |")
            print("                    |.-\\\"`   `\\\"-.")
            print("                   /  `'-...-' ___\\_")
            print("                  /          ,'  v  `,")
            print("                 /  /     , ( <==+==> )")
            print("                -. / | | : : \\   ^   /")
            print("              (\\\\)   ||  : :  \\  ^  /")
            print("                \\    ||  : :   \\ ^ /        ")
            print("                 )   ||  ; :    \\^/      ")
            print("                (    ||  : :  || V     ")
            print("               <(^)> ||  '.'  ||")
            print("                 v   ||   +   ||")
            print("                     |'-.___.-'|")
            print("                     |         |")
            print("                     '-.__ __.-'")
            print("                       (_/`\\_)")
        if hero.name == "Warrior":
            print("                      /'|")
            print("                     |  ||")
            print("                     |  ||")
            print("                     |  ||         __.--._")
            print("                     |  ||      /~~   __.-~\\ _")
            print("                     |  ||  _.-~ / _---._ ~-\\/~\\")
            print("                     |  || // /  /~/  .-  \\  /~-\\")
            print("                     |  ||((( /(/_(.-(-~~~~~-)_/ |")
            print("                     |  || ) (( |_.----~~~~~-._\\ /")
            print("                     |  ||    ) |              \\_|")
            print("                     |  ||     (| =-_   _.-=-  |~)        ,")
            print("                     |  ||      | `~~ |   ~~'  |/~-._-'/'/_,")
            print("                     |  ||       \\    |        /~-.__---~ , ,")
            print("                     |  ||       |   ~-''     || `\\_~~~----~")
            print("                     |  ||_.ssSS$$\\ -====-   / )\\_  ~~--~")
            print("             ___.----|~~~|%$$$$$$/ \\_    _.-~ /' )$s._")
            print("    __---~-~~        |   |%%$$$$/ /  ~~~~   /'  /$$$$$$$s__")
            print("  /~       ~\\    ============$$/ /        /'  /$$$$$$$$$$$SS-.")
            print("/'      ./\\\\\\_( ~---._(_))$/ /       /'  /$$$$%$$$$$~      \\ ")
            print("(      //////////(~-(..___)/$/ /      /'  /$$%$$%$$$$'         \\")
            print(" \\    |||||||||||(~-(..___)$/ /  /  /'  /$$$%$$$%$$$            |")
            print("  `-__ \\\\\\\\\\\\(-.(_____) /  / /'  /$$$$%$$$$$%$             |")
            print("      ~~\"\"\"\"\"\"\"\"-\\.(____) /   /'  /$$$$$%%$$$$$$\\_            /")
            print("                    $|===|||  /'  /$$$$$$$%%%$$$$$( ~         ,'|")
            print("                __  $|===|%\\/'  /$$$$$$$$$$$%%%%$$|        ,''  |")
            print("               ///\\ $|===|/'  /$$$$$$%$$$$$$$%%%%$(            /'")
            print("                \\///\\|===|  /$$$$$$$$$%%$$$$$$%%%%$\\_-._       |")
            print("                 `\\//|===| /$$$$$$$$$$$%%%$$$$$$-~~~    ~      /")
            print("                   `\\|-~~(~~-`$$$$$$$$$%%%///////._       ._  |")
            print("                   (__--~(     ~\\\\\\\\\\\\\\\\\\\\        \\ \\ ")
            print("                   (__--~~(       \\\\\\\\\\\\\\\\\\|        \\/")

        if hero.name == 'Thief':
            print("⠀⠀⠀⠀⢀⣤⣶⣶⣿⣿⣶⣶⣤⣀⠀⠀⠀⠀")
            print("⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀")
            print("⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀")
            print("⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀")
            print("⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷")
            print("⠈⠉⠉⠉⣉⣉⠉⠉⠉⠉⠉⣉⣉⡉⠉⠉⠉")
            print("⢀⣴⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣦⡀")
            print("⢸⣿⣿⣅⠀⢀⣨⣿⣿⣿⣿⣇⡀⠀⣈⣿⣿⡿")
            print("⠀⠙⠿⢿⣿⣿⡿⠿⠛⠛⠿⢿⣿⣿⡿⠿⠛⠁")

        stats = '\n' + player_name + str(hero)
        print(stats)

    @staticmethod
    def menu_str(menu_str):
        """ Prints this method in the controller class """
        print(menu_str)

    @staticmethod
    def cheat_list(cheat_str):
        """ Prints this method in the controller class """
        print(cheat_str)

    @staticmethod
    def display_hero_stats(hero):
        """ Prints this method in the controller class """
        formatted_list = ["   " + str(item) + " : " + str(values) for item, values in hero.stats.items()]
        print("\n" + "\n".join(formatted_list) + "\n")

    @staticmethod
    def attack_mode(monster):
        """ Prints Monster images in the controller class """
        troll_names = ["Ragnok", "Grimbash", "Boulderfist", "Groggnar", "Gnarlgrip"]
        chimera_names = ["Hydra", "Nemean", "Typhon", "Thrawn", "Gryphon"]
        dragon_names = ["Drakar", "Fafnir", "Volcanor", "Pyrax", "Vritra"]
        ogre_names = ["Grommash", "Throg", "Grokk", "Ugg", "Gronk"]
        gremlin_names = ["Gizmo", "Spike", "Scratch", "Snaggletooth", "Gnash"]
        skeleton_names = ["Skeletor", "Deathclaw", "Rattlebones",
                          "Skullcrack", "Dreadbone"]

        if monster.name in dragon_names:
            print("                 ___====-_  _-====___")
            print("           _--^^^#####//      \\\\#####^^^--_")
            print("        _-^##########// (    ) \\\\##########^-_")
            print("       -############//  |\\^^/|  \\\\############-")
            print("     _/############//   (@::@)   \\\\############\\_")
            print("    /#############((     \\\\//     ))#############\\")
            print("   -###############\\\\    (oo)    //###############-")
            print("  -#################\\\\  / VV \\  //#################-")
            print(" -###################\\\\/      \\//###################-")
            print("_#/|##########/\\######(   /\\   )######/\\##########|\\#_")
            print("|/ |#/\\#/\\#/\\/  \\#/\\##\\  |  |  /##/\\#/  \\/\\#/\\#/\\#| \\|")
            print("`  |/  V  V  `   V  \\#\\| |  | |/#/  V   '  V  V  \\|  '")
            print("   `   `  `      `   / | |  | | \\   '      '  '   '")
            print("                    (  | |  | |  )")
            print("                   __\\ | |  | | /__")
            print("                  (vvv(VVV)(VVV)vvv)")

        if monster.name in skeleton_names:
            print("      .-. ")
            print("     (o.o) ")
            print("      |=|  ")
            print("     __|__ ")
            print("   //.=|=.\\ ")
            print("  // .=|=. \\ ")
            print("  \\ .=|=. // ")
            print("   \\(_=_)// ")
            print("    (:| |:) ")
            print("     || || ")
            print("     () () ")
            print("     || || ")
            print("     || || ")
            print("    ==' '== ")
        if monster.name in ogre_names:
            print("          _......._")
            print("       .-'.'.'.'.'.'.`-.")
            print("    /.'.'               '.\\")
            print("    |.'    _.--...--._     |")
            print(" .-.'    `.   ((@))  .'   '.-.")
            print("( ^ \\      `--.   .-'     / ^ )")
            print(" \\  /         .   .       \\  /")
            print(" /          .'     '.  .-    \\")
            print("( _.\\    \\ (_`-._.-'_)    /._\\)")
            print(" `-' \\   ' .--.          / `-'")
            print("     |  / /|_| `-._.'\\   |")
            print("     |   |       |_| |   /-.._")
            print(" _..-\\   `.--.______.'  |")
            print("      \\       .....     |")
            print("       `.  .'      `.  /")
            print("          `-..___..-`")

        if monster.name in chimera_names:
            print("       ,'.` ,,,")
            print("     (( ))().)       _-- __)")
            print("      _~ /\\.( ) ) --__/   ^ \\ ___------_")
            print("   _//o_  ))(). ,)       (_ø \\          `-_")
            print("  /      ))()  . ))     /   \"             |\\__")
            print("  ø_---\\ )).. )   )                       |   `---.___")
            print("    (\"\" \\  )) . .)                        |           `--.__")
            print("     ___/ _/ ( ()   \\         \\          /__                `--._")
            print("      ---'(  (\\      |      ___\\_        \\  `-_._.-----___.-'    `-")
            print("         ((..( \\     |___--      \\_      |   /    /¢~~             )")
            print("           (( ( |   /\"             \\_    |  (.------_             /")
            print("              ((|   |                |   /_  `_-- ____  \\  ___,--'")
            print("                 |   |                |  /            --.____|/")
            print("                 |   |               /  /   ")
            print("                _|  /              _/ _/")
            print("              //__/             //__/")
            print("              ``                ``")

        if monster.name in gremlin_names:
            print("   .-',,^,,'.")
            print("  / \\(0)(0)/  \\")
            print("  )/( ,_\\\"_,)\\(")
            print("  `  >-`~(   ' ")
            print("_N\\ |(`\\ |___")
            print("\' |/ \\ \\/_-,)")
            print(" '.(  \\`\\_<")
            print("    \\ _\\|")
            print("     | |_\\__")
            print("     \\_,_>--'")

        if monster.name in troll_names:
            print("   _______  ")
            print(" ((      ))    _______")
            print(" ((      ))   /_     _\\")
            print(" ((      ))   \\|0   0|/")
            print("  __(())__    (_  ^  _)")
            print("   ( () )   /`\\ |\"\"\"|/`\\")
            print("     {}____/  / _____/  /")
            print("     () ____/\\    =(   /\\")
            print("     {}    /  \\_/\\=/\\_/  \\")
            print("     {}    /  \\_/\\=/\\_/  \\")

        return input(
            f"You've encountered a {monster.name}! You can use \n1. normal attack \"n\", 2. special "
            f"attack \"s\" 3. use healing potion \"h\" 4. see \"stats\" ").lower()

    @staticmethod
    def monster_dead(monster):
        """ Prints this method in the controller class """
        print(f"you killed the monster {monster.name}!")

    def next_attack(self):
        """ Prints this method in the controller class and gets input from the user """
        return input(
            f"Next Move 1. normal attack \"n\", 2. special "
            f"attack \"s\" or \"help\" ").lower()

    def attack_help(self):
        """ Prints this method in the controller class """
        print("1 normal attack \"n\", 2. special attack \"s\" 3. use healing potion \"h\" 4. see "
              "\"stats\" ")

    @staticmethod
    def clear_screen():
        """ Clear screen for the different operating systems """
        # Check if the operating system is Windows
        if os.name == 'nt':
            os.system('cls')
        # For Unix/Linux/Mac
        else:
            os.system('clear')

    @staticmethod
    def print_vision(vision_str):
        """ Prints vision in the controller class """
        print(vision_str)

    """----------------------------------dungeon characters----------------------------------------------------------"""

    @staticmethod
    def display_attack_result(result, hero, hero_name, monster):
        """ Prints attack result in the controller class """
        if result["success"]:
            print(f"{result['attacker']} attacks {result['opponent']} for {result['damage']} damage points. "
                  f"{hero_name} has {hero.hit_points}HP and {monster.name} has {monster.hit_points}HP")
        else:
            print(f"{result['attacker']} couldn't attack {result['opponent']}")

    @staticmethod
    def special_attack_results(result, hero, hero_name, monster):
        """ Prints special attack in the controller class """
        if hero.name == "Warrior":
            if result["success"]:
                print(f"{result['attacker']} performs a Crushing Blow for {result['damage']} damage points. "
                      f"{hero_name} has {hero.hit_points}HP and {monster.name} has {monster.hit_points}HP")
            else:
                print(f"{result['attacker']} couldn't perform Crushing Blow")

        elif hero.name == "Priestess":
            print(f"{result['attacker']} performs healing on itself {result['heal']} heal points. ")
        elif hero.name == "Thief":
            if result["success"]:
                if result["attacks"] == 2:
                    print(
                        f"{result['attacker']} attacked {result['opponent']} twice for {result['damage']} damage points. "
                        f"{hero_name} has {hero.hit_points} and {monster.name} has {monster.hit_points}")
                elif result["attacks"] == 1:
                    print(
                        f"{result['attacker']} attacked {result['opponent']} once for {result['damage']} damage points. Now "
                        f"{hero_name} has {hero.hit_points} and {monster.name} has {monster.hit_points}")
                else:
                    print(f"{result['attacker']} couldn't perform the special attack.")
            else:
                print(f"{result['attacker']} couldn't perform the special attack.")
        else:
            print(f"{result['attacker']} couldn't perform the special attack.")

    @staticmethod
    def priestess_adding_hit_points(result):
        """ Prints this method in the controller class """
        print(f" {result['attacker']} now has {result['hit_points']} ")

    @staticmethod
    def monster_heal(result):
        """ Prints monster heal method in the controller class """
        if result["success"]:
            if result["heal_amount"] > 0:
                print(f"The {result['name']} has healed itself!")
            else:
                print(f"The {result['name']} cannot heal itself, you're safe!")

    @staticmethod
    def print_room(room_str):
        """ Prints room in the controller class """
        print(room_str)

    @staticmethod
    def print_play_dungeon(dungeon):
        """ Prints dungeon in the controller class """
        """
        Prints a simple visual representation of the Dungeon's maze as player is playing
        :return: None.
        """
        space = " "
        top = []
        mid = []
        bottom = []

        for row in range(dungeon.get_row_length()):
            for col in range(dungeon.get_col_length()):
                # Top string

                if dungeon.get_room_str((row, col)).current_room:
                    top.append(str(dungeon.get_room_str((row, col)))[0:3] + "  ")
                    mid_len = len(str(dungeon.get_room_str((row, col)))[4:-4])
                    current = str(dungeon.get_room_str((row, col)))[4]
                    current += "@"
                    current += str(dungeon.get_room_str((row, col)))[-5:-4] + "  "  # space * (13 - mid_len)

                    mid.append(current)
                    bottom.append(str(dungeon.get_room_str((row, col)))[-3:] + "  ")  # (space * 2))

                elif dungeon.get_room_str((row, col)).player_traveled:
                    top.append("---  ")
                    mid.append("---  ")
                    bottom.append("---  ")
                else:
                    top.append("^^^  ")
                    mid.append("^^^  ")
                    bottom.append("^^^  ")

        # prints dungeon according to the dimensions
        for i in range(0, dungeon.get_row_length()):
            # print(end="\n")
            for room in range(i * dungeon.get_col_length(), (i + 1) * dungeon.get_col_length()):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * dungeon.get_col_length(), (i + 1) * dungeon.get_col_length()):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * dungeon.get_col_length(), (i + 1) * dungeon.get_col_length()):
                print(bottom[room], end="")
            print("\n")

    @staticmethod
    def print_view(dungeon):
        print("You are @")
        print(dungeon)

    @staticmethod
    def end():
        """
        Prints closing title slides
        """
        time.sleep(.1)
        group_names = ("Aqueno Nirasmi Amalraj \nMinna Chae \nSarah St. Albin \n")
        teacher_names = ("Tom Capaul \nKevin Anderson \nVarik Hoang \nRobert Cordingly \nAshutosh Engavle")
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
