"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

from Room import Room
from DungeonItemsFactory import DungeonItemsFactory
import random


class Dungeon:
    """
    Creates a Dungeon for the DungeonAdventure Game.
    """

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__current_room = None  # Temporary?
        self.__empty_room = None  # Temporary?
        self.__player_traveled = None  # Temporary?
        self.__items = {}
        self.__maze = []

        for r in range(0, self.__rows):
            self.__maze.append([Room() for c in range(0, self.__cols)])

        self.build_dungeon()

    # External methods

    def build_dungeon(self):
        """
        Generates a maze for the Dungeon.
        :return: None
        """
        # Randomly select a starting Room
        start_row = random.randint(0, self.__rows - 1)
        start_col = random.randint(0, self.__cols - 1)
        start_room = self.__maze[start_row][start_col]

        # Generate the maze
        self._create_maze(start_room, start_row, start_col)

        # Set entrance and exit
        self._set_entrance_exit()

        # Make some Rooms impassable
        self._make_impassable()

        # Verify that the maze is still traversable from entrance to exit
        if self._is_traversable(0, 0):  # If it's traversable
            self.__items = {(row, col): self.__maze[row][col] for row in range(self.__rows) for col
                            in range(self.__cols)}
            self._place_pillars()  # Randomly add pillars
            self._place_items()  # Randomly add pillars, potions, and other objects to it
        else:
            self._create_maze(start_room, start_row, start_col)  # Otherwise generate a new maze if not passable

    @property
    def entrance(self):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__maze[0][0]

    @property
    def maze_array(self):
        return self.__maze

    @property
    def maze_dictionary(self):
        """
        Internal getter method that returns the dictionary.
        :return: the dictionary instantiated in the class constructor.
        """
        return self.__items

    def show_room_str(self, key):
        """
        Gets the entrance Room coordinates of the Dungeon's maze based on the provided key.
        :return: Room
        """
        return self.__items.get(key)

    @property
    def col_length(self):
        return self.__cols

    @property
    def row_length(self):
        return self.__rows

    def show_doors(self, current_key, new_key, direction="N"):
        """
        Get attributes of room
        :return: Boolean
        """
        attributes_current = self.__items.get(current_key)  # grabbing room attributes
        attributes_new = self.__items.get(new_key)  # grabbing room attributes

        if direction == "N":
            boo_results = attributes_current.north_door and attributes_new.south_door
            return boo_results

        if direction == "S":
            boo_results = attributes_current.south_door and attributes_new.north_door
            return boo_results

        if direction == "E":
            boo_results = attributes_current.east_door and attributes_new.west_door
            return boo_results

        if direction == "W":
            boo_results = attributes_current.west_door and attributes_new.east_door
            return boo_results

    @property
    def current_room(self):
        return self.__current_room

    @current_room.setter
    def current_room(self, room):
        """
        Sets player's current coordinates as current room. Used in vision potion
        """
        room.healing_potion = False
        room.vision_potion = False
        room.pit = False
        room.multiple_items = False
        room.entrance = False
        room.empty_room = False
        room.abstraction_pillar = False
        room.polymorphism_pillar = False
        room.inheritance_pillar = False
        room.encapsulation_pillar = False
        room.current_room = True


    def get_empty_room(self):
        return self.__empty_room


    def set_empty_room(self, key=(0, 0), pit=False):
        """
        If room traveled, removes items but leaves pit
        """
        item = self.__items.get(key)
        if item.healing_potion:
            item.healing_potion = False
            item.empty_room = True
        elif item.vision_potion:
            item.vision_potion = False
            item.empty_room = True
        elif item.multiple_items:
            item.multiple_items = False
            if pit:
                item.pit = True
            else:
                item.empty_room = True
        elif item.abstraction_pillar:
            item.abstraction_pillar = False
            item.empty_room = True
        elif item.polymorphism_pillar:
            item.polymorphism_pillar = False
            item.empty_room = True
        elif item.inheritance_pillar:
            item.inheritance_pillar = False
            item.empty_room = True
        elif item.encapsulation_pillar:
            item.encapsulation_pillar = False
            item.empty_room = True

    def show_room_contents(self, key):
        """
       Gets the contents of a Room in the dungeon.
       :param key: a tuple representation of the row, column Room coordinates (0, 0)
       :return: the contents of the specified Room, in the format specified in the __str__() method in Room class.
       """

        item = self.__items.get(key)
        symbols = ""
        if item.healing_potion:
            symbols += "H"
        elif item.vision_potion:
            symbols += "V"
        elif item.pit:
            symbols += "X"
        elif item.entrance:
            symbols += "i"
        elif item.exit:
            symbols += "O"
        elif item.multiple_items:
            symbols += "M"
        elif item.empty_room:
            symbols += " "
        elif item.abstraction_pillar:
            symbols += "A"
        elif item.polymorphism_pillar:
            symbols += "P"
        elif item.inheritance_pillar:
            symbols += "I"
        elif item.encapsulation_pillar:
            symbols += "E"
        return symbols

    def print_dictionary(self):
        """
        Prints the contents of each Room without the symbols from Room's __str__() method.
        Uses the format (row, col) : contents.
        :return: None
        """
        symbols_dict = self._get_object_symbols()
        for key, value in symbols_dict.items():
            print(f"Room at ({key[0]}, {key[1]}): {value}")

    def is_valid_room(self, row, col):
        """
        Checks whether a Room is valid or not.
        :param row: row coordinate
        :param col: column coordinate
        :return: boolean
        """
        return 0 <= row < self.__rows and 0 <= col < self.__cols

    def __str__(self):
        """
        External method that builds a string containing information about the entire Dungeon.
        :return: String
        """
        dungeon_info = ""
        for row in range(self.__rows):
            for col in range(self.__cols):
                room = self.__maze[row][col]
                dungeon_info += f"Room at ({row}, {col}):"
                dungeon_info += f"\n  - North Door: {room.north_door}"
                dungeon_info += f"\n  - South Door: {room.south_door}"
                dungeon_info += f"\n  - East Door: {room.east_door}"
                dungeon_info += f"\n  - West Door: {room.west_door}"
                dungeon_info += f"\n  - Visited: {room.visited}"
                dungeon_info += f"\n  - Entrance: {room.entrance}"
                dungeon_info += f"\n  - Exit: {room.exit}"
                dungeon_info += f"\n  - Impasse: {room.impasse}"
                dungeon_info += f"\n  - Empty Room: {room.empty_room}"
                room.abstraction_pillar = True
                dungeon_info += f"\n  - Abstraction Pillar: {room.abstraction_pillar}"
                room.encapsulation_pillar = True
                dungeon_info += f"\n  - Encapsulation Pillar: {room.encapsulation_pillar}"
                room.inheritance_pillar = True
                dungeon_info += f"\n  - Inheritance Pillar: {room.inheritance_pillar}"
                room.polymorphism_pillar = True
                dungeon_info += f"\n  - Polymorphism Pillar: {room.polymorphism_pillar}"
                room.healing_potion = True
                dungeon_info += f"\n  - Healing Potion: {room.healing_potion}"
                room.vision_potion = True
                dungeon_info += f"\n  - Vision Potion: {room.vision_potion}"
                room.pit = True
                dungeon_info += f"\n  - Pit: {room.pit}"
                dungeon_info += "\n\n"

        return dungeon_info

    def print_play_dungeon(self, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze as player is playing
        :return: None.
        """
        top = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    top.append(str(self.__maze[row][col])[0:3] + "  ")
                else:
                    if self.__items.get((row, col)).player_traveled:
                        top.append("---  ")
                    else:
                        top.append("^^^  ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    if len(str(self.__maze[row][col])) == 10:
                        mid.append(str(self.__maze[row][col])[4:6] + "   ")
                    else:
                        mid.append(str(self.__maze[row][col])[4:7] + "  ")
                else:
                    if self.__items.get((row, col)).player_traveled:
                        mid.append("---  ")
                    else:
                        mid.append("^^^  ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    if len(str(self.__maze[row][col])) == 10:
                        bottom.append(str(self.__maze[row][col])[7:10] + "  ")
                    else:
                        bottom.append(str(self.__maze[row][col])[8:11] + "  ")
                else:
                    if self.__items.get((row, col)).player_traveled:
                        bottom.append("---  ")
                    else:
                        bottom.append("^^^  ")

        # prints dungeon according to the dimensons
        for i in range(0, self.__rows):
            # print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(bottom[room], end="")
            print("\n")

    @property
    def player_traveled(self):
        return self.__player_traveled

    @player_traveled.setter
    def player_traveled(self, key):
        room = self.__items.get(key)
        room.player_traveled = True

    def print_dungeon(self, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze.
        :return: None.
        """
        # Saves top strings of all rooms in dungeon
        top = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                top.append(str(self.__maze[row][col])[0:3] + "     ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    current = str(self.__maze[row][col])[4]
                    current += "@"
                    current += str(self.__maze[row][col])[6]  + "     "
                    mid.append(current)
                else:
                    if len(str(self.__maze[row][col])) == 10:
                        mid.append(str(self.__maze[row][col])[4:6] + "      ")
                    else:
                        mid.append(str(self.__maze[row][col])[4:7] + "     ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if len(str(self.__maze[row][col])) == 10:
                    bottom.append(str(self.__maze[row][col])[7:10] + "     ")
                else:
                    bottom.append(str(self.__maze[row][col])[8:11] + "     ")

        # prints dungeon according to the dimensions
        for i in range(0, self.__rows):
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(bottom[room], end="")
            print("\n")

    # Internal methods

    def _create_maze(self, room, current_row, current_col):
        """
        Internal method that randomly generates a maze for the Dungeon.
        :param room: starting room
        :param current_row: current row coordinate
        :param current_col: current column coordinate
        :return: None
        """
        # Set the starting room to "visited"
        room.visited = True

        # Shuffle a list of possible directions
        directions = ["N", "S", "E", "W"]
        random.shuffle(directions)

        # Loop through the shuffled directions
        for direction in directions:
            neighbor_row, neighbor_col = self._return_neighbor_coordinates(current_row, current_col, direction)
            if self.is_valid_room(neighbor_row, neighbor_col):
                neighbor_room = self.__maze[neighbor_row][neighbor_col]
                if not neighbor_room.visited:  # If the neighboring room hasn't been visited...
                    # Create doors between them
                    self._create_doors(room, direction)
                    self._create_doors(neighbor_room, self._opposite_direction(direction))

                    # Recursively explore the neighbor Room
                    self._create_maze(neighbor_room, neighbor_row, neighbor_col)

    def _return_neighbor_coordinates(self, row, col, direction):
        """
        Internal method that returns the coordinates of the neighboring room in order to generate the maze.
        :param row: row coordinate, intended to be the current row
        :param col: column coordinate, intended to be the current column
        :param direction: the current direction that the maze is following during generation
        :return: the new row and column coordinates
        """
        d_row = {"N": -1, "S": 1, "E": 0, "W": 0}
        d_col = {"N": 0, "S": 0, "E": 1, "W": -1}

        new_row = row + d_row[direction]
        new_col = col + d_col[direction]
        return new_row, new_col

    def _opposite_direction(self, direction):
        """
        Internal method that returns the opposite direction of the provided direction.
        Raises ValueError if an invalid direction is given.
        :param direction: the given direction ("N," "S," "E," "W")
        :return: (Str) the opposite direction of the provided direction
        """
        if direction not in ("N," "S," "E," "W"):
            raise ValueError("INVALID DIRECTION PROVIDED")
        return {"N": "S", "S": "N", "E": "W", "W": "E"}[direction]

    def _create_doors(self, room, direction):
        """
        Internal method that creates a door in a particular direction ("N," "S," "E," "W") in relation
        to the provided Room.
        :param room: Room object whose doors need to be knocked down in _create_maze()
        :param direction: the direction of the door that will be knocked down ("N," "S," "E," "W")
        :return: None
        """
        if direction not in ("N," "S," "E," "W"):
            raise ValueError("INVALID DIRECTION PROVIDED")

        # Update the relevant door based on given direction
        if direction == "N":
            room.north_door = True
        elif direction == "S":
            room.south_door = True
        elif direction == "E":
            room.east_door = True
        elif direction == "W":
            room.west_door = True

    def _set_entrance_exit(self):
        """
        Internal method that sets the entrance and exit in the maze, sets them as passable, and sets them as empty.
        :return: None.
        """
        # Set the entrance and exit
        self.__maze[0][0].entrance = True
        self.__maze[self.__rows - 1][self.__cols - 1].exit = True

        # Set them as passable
        self.__maze[0][0].impasse = False
        self.__maze[self.__rows - 1][self.__cols - 1].impasse = False

        # Set them as empty
        self.__maze[0][0].empty_room = True
        self.__maze[self.__rows - 1][self.__cols - 1].empty_room = True

        # Set exterior doors
        self.__maze[0][0].west_door = True
        self.__maze[self.__rows - 1][self.__cols - 1].east_door = True

    def _make_impassable(self):
        """
        Internal method that randomly sets some Rooms as impassable.
        :return: None.
        """
        for row in range(self.__rows):
            for col in range(self.__cols):
                if random.randrange(1, 101) > 80:
                    self.__maze[row][col].impasse = True

    def _is_traversable(self, start_row, start_col):
        """
        Internal method that returns a boolean reflecting whether the maze is passable or not.
        :param start_row: starting row coordinate (usually 0)
        :param start_col: starting column coordinate (usually 0)
        :return: boolean
        """
        return self._traverse_the_maze(start_row, start_col)

    def _traverse_the_maze(self, row, col):
        """
        :param row: starting row coordinate of the Room
        :param col: starting column coordinate of the Room
        :return: True if the maze is traversable, false if not.
        """
        target = self.__maze[self.__rows - 1][self.__cols - 1]  # Identify the coordinates of the exit

        if not self.is_valid_room(row, col):  # Check if the Room is valid
            return False

        if self.__maze[row][col] == target:  # Check if the Room is the exit
            return True

        self.__maze[row][col].visited = True  # Set the starting Room as visited

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Check Rooms to the South, East, North, and West
        for d_row, d_col in directions:
            if self._traverse_the_maze(row + d_row, col + d_col):
                return True

        self.__maze[row][col].visited = True  # If no exit is found in any direction, mark Room as unvisited
        return False

    def _place_items(self):
        for (row, col), room in self.__items.items():
            if room.entrance or room.exit or room.abstraction_pillar \
                    or room.polymorphism_pillar or room.inheritance_pillar or room.encapsulation_pillar:
                continue
            else:
                item_list = ["V", "H", "M", "X"]
                choice = random.choice(item_list)
                possibility = random.randint(0, 100)
                # Place the healing potion
                if possibility <= 30:
                    # Place the vision potion
                    if choice == "V":
                        vision_potion = DungeonItemsFactory.create_item("V")
                        room.vision_potion = True if vision_potion else False
                    # Place health potion
                    if choice == "H":
                        healing_potion = DungeonItemsFactory.create_item("H", 1, 10)
                        room.healing_potion = True if healing_potion else False
                    # Place multi item
                    if choice == "M":
                        multiple_items = DungeonItemsFactory.create_multiple_items(1, 10)
                        room.multiple_items = True if multiple_items else False
                    # Place the pit
                    if choice == "X":
                        pit = DungeonItemsFactory.create_item("X", 1, 10)
                        room.pit = True if pit else False
                else:
                    room.empty_room = True

    def _place_pillars(self):
        """
        Internal method that randomly places Pillars in eligible Rooms throughout the maze.
        :return: None
        """
        abstraction = False
        encapsulation = False
        inheritance = False
        polymorphism = False

        qualified_rooms = [room for (row, col), room in self.__items.items()
                           if not room.entrance and not room.exit and not room.impasse
                           and not room.vision_potion and not room.pit and not room.healing_potion]

        selected_rooms = random.sample(qualified_rooms, 4)

        for room in selected_rooms:
            if not abstraction:
                room.abstraction_pillar = True
                abstraction = True
            elif not encapsulation:
                room.encapsulation_pillar = True
                encapsulation = True
            elif not inheritance:
                room.inheritance_pillar = True
                inheritance = True
            elif not polymorphism:
                room.polymorphism_pillar = True
                polymorphism = True
            else:
                break

    def _get_object_symbols(self):
        """
        Internal method that overrides the Room class __str__() method by converting its symbols to shorter, more
        readable symbols in the Dungeon class dictionary.
        :return: the dictionary of symbols
        """
        symbols_dict = {}
        for (row, col), room in self.__items.items():
            symbols = ""
            if room.healing_potion:
                symbols += "H"
            elif room.vision_potion:
                symbols += "V"
            elif room.pit:
                symbols += "X"
            elif room.entrance:
                symbols += "i"
            elif room.exit:
                symbols += "O"
            elif room.multiple_items:
                symbols += "M"
            elif room.empty_room:
                symbols += " "
            elif room.abstraction_pillar:
                symbols += "A"
            elif room.polymorphism_pillar:
                symbols += "P"
            elif room.inheritance_pillar:
                symbols += "I"
            elif room.encapsulation_pillar:
                symbols += "E"
            symbols_dict[(row, col)] = symbols
        return symbols_dict


dungeon = Dungeon(5, 5)
dungeon.print_dungeon()
