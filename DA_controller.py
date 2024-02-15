from DungeonAdventure import DungeonAdventure


class DungeonAdventureController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.dungeon_adventure = DungeonAdventure()

    def whole_game(self):
        """
                Plays full game from top to bottom
                :return: None
                """
        self.dungeon_adventure.print_introduction()
        play = "y"
        while play.lower() == "y" or play.lower() == "yes":
            self.dungeon_adventure.set_play_mode()
            print(self.dungeon_adventure.menu_str())
            self.dungeon_adventure.set_up_player()
            self.dungeon_adventure.player_command()
            print("\nOriginal maze:\n")
            self.dungeon_adventure.original_dungeon.print_dungeon()
            print("Your maze:\n")
            self.dungeon_adventure.dungeon.print_dungeon()
            self.dungeon_adventure.player_results()
            play = input("Would you like to play again? \"y\" to keep playing or enter any key to exit. ")
        self.dungeon_adventure.print_end()
