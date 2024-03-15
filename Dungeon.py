"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 504
Dungeon Adventure 2.0
"""

from Room import Room
from DungeonItemsFactory import DungeonItemsFactory
import random


class Dungeon:
    """
    Creates a Dungeon for the DungeonAdventure Game.
    """

    def __init__(self, rows, cols):
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise ValueError("Rows and cols must be integers")
        if rows < 3 or cols < 3:
            raise ValueError("Rows and cols must be at least 3")

        self.__rows = rows
        self.__cols = cols
        self.__items = {}
        self.__maze = []
        self.__exit_row = None
        self.__exit_col = None
        self.__entrance_row = None
        self.__entrance_col = None

        for r in range(0, self.__rows):
            self.__maze.append([Room() for _ in range(0, self.__cols)])

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
        if self._is_traversable(0, 0):
            self.__items = {(row, col): self.__maze[row][col] for row in range(self.__rows) for col
                            in range(self.__cols)}
            self._place_pillars()
            self._place_boss_monster()
            self._place_monsters()
            self._place_items()
        else:
            self._create_maze(start_room, start_row, start_col)

    def get_entrance(self):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__maze[0][0]

    def get_maze_array(self):
        """ Returns the 2D array """
        return self.__maze

    def get_maze_dictionary(self):
        """ Returns the Dungeon dictionary to see items in Rooms """
        return self.__items

    def get_room_str(self, key):
        """
        Gets the entrance Room coordinates of the Dungeon's maze based on the provided key.
        :return: Room
        """
        return self.__items.get(key)

    def get_col_length(self):
        """
        Returns the number of columns in the Dungeon maze.
        :return: (Int) number of columns
        """
        return self.__cols

    def get_row_length(self):
        """
        Returns the number of rows in the Dungeon maze.
        :return: (Int) number of rows
        """
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
        Returns a simple visual representation of the Dungeon's maze.
        :return: string representation of the Dungeon
        """

        space = " "
        top = []
        mid = []
        bottom = []

        for row in range(self.get_row_length()):
            for col in range(self.get_col_length()):
                # Top string
                top.append(str(self.get_room_str((row, col)))[0:3] + space * 10)
                # Mid string
                mid_len = len(str(self.get_room_str((row, col)))[4:-4])
                if self.get_room_str((row, col)).current_room:

                    current = str(self.get_room_str((row, col)))[4]
                    current += "@"
                    current += str(self.get_room_str((row, col)))[-5:-4] + space * (13 - mid_len)
                    mid.append(current)
                else:
                    mid.append(str(self.get_room_str((row, col)))[4:-4] + space * (13 - mid_len))

                    # Bottom string
                bottom.append(str(self.get_room_str((row, col)))[-3:] + (space * 10))

        # Construct the visual representation of the dungeon
        dungeon_str = ""
        for i in range(0, self.get_row_length()):
            for room in range(i * self.get_col_length(), (i + 1) * self.get_col_length()):
                dungeon_str += top[room]
            dungeon_str += "\n"
            for room in range(i * self.get_col_length(), (i + 1) * self.get_col_length()):
                dungeon_str += mid[room]
            dungeon_str += "\n"
            for room in range(i * self.get_col_length(), (i + 1) * self.get_col_length()):
                dungeon_str += bottom[room]
            dungeon_str += "\n\n"

        return dungeon_str

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
        if not isinstance(room, Room) or not isinstance(direction, str):
            raise ValueError("Must pass a Room object and a string ('N', 'S', 'E', or 'W')")

        if direction not in ("N," "S," "E," "W"):
            raise ValueError("Direction must be 'N', 'S', 'E', or 'W'")

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
        self.__maze[0][0].empty_room = False
        self.__maze[self.__rows - 1][self.__cols - 1].exit = True

        # Update exit Room coordinates
        self.__exit_row = self.__rows - 1
        self.__exit_col = self.__cols - 1

        # Set them as passable
        self.__maze[0][0].impasse = False
        self.__maze[self.__rows - 1][self.__cols - 1].impasse = False

        # # Set entrance as empty
        self.__maze[0][0].empty_room = True

        # Set exterior doors
        self.__maze[0][0].west_door = True
        self.__maze[self.__rows - 1][self.__cols - 1].east_door = True

        # Update items dictionary
        self.__items[(self.__exit_row, self.__exit_col)] = self.__maze[self.__exit_row][self.__exit_col]

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

    def _place_monsters(self):
        """
        Randomly places Monsters throughout the Dungeon maze.
        :return: None
        """
        monster_types = ["Ogre", "Gremlin", "Skeleton"]

        total_rooms = len(self.__items)
        target_monster_rooms = total_rooms // 8

        monster_rooms = 0

        while monster_rooms < target_monster_rooms:
            random_room = random.choice(list(self.__items.values()))
            if random_room.entrance or random_room.exit:
                continue
            elif random_room.ogre or random_room.gremlin or random_room.skeleton:
                continue
            elif (random_room.abstraction_pillar or random_room.polymorphism_pillar or random_room.inheritance_pillar or
                  random_room.encapsulation_pillar):
                continue

            if random.random() < 0.5:
                choice = random.choice(monster_types)
                if choice == "Ogre":
                    random_room.ogre = True
                elif choice == "Gremlin":
                    random_room.gremlin = True
                elif choice == "Skeleton":
                    random_room.skeleton = True
                else:
                    random_room.ogre = False
                    random_room.gremlin = False
                    random_room.skeleton = False

                monster_rooms += 1

    def _place_boss_monster(self):
        """
        Internal method that places a boss Monster at the end of the maze.
        :return: None
        """

        boss_type = ["Troll", "Chimera", "Dragon"]

        qualified_rooms = [room for room in self.__items.values()
                           if room.exit or room.abstraction_pillar or room.encapsulation_pillar
                           or room.inheritance_pillar or room.polymorphism_pillar]

        for room in qualified_rooms:
            monster_choice = random.choice(boss_type)
            if monster_choice == "Troll":
                room.troll = True
            elif monster_choice == "Chimera":
                room.chimera = True
            elif monster_choice == "Dragon":
                room.dragon = True
            else:
                break

        # place pillars first
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

    #place items 2nd
    def _place_items(self):
        """ Places items throughout the maze """
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
                        # multiple_items = DungeonItemsFactory.create_item("M")
                        # room.multiple_items = True if multiple_items else False
                        items = ["V", "H", "X"]
                        results = random.sample(items, random.randint(2, 3))
                        for values in results:
                            if values == 'V':
                                vision_potion = DungeonItemsFactory.create_item("V")
                                room.vision_potion = True if vision_potion else False
                            if values == "H":
                                healing_potion = DungeonItemsFactory.create_item("H", 1, 10)
                                room.healing_potion = True if healing_potion else False
                            if values == "X":
                                pit = DungeonItemsFactory.create_item("X", 1, 10)
                                room.pit = True if pit else False
                    # Place the pit
                    if choice == "X":
                        pit = DungeonItemsFactory.create_item("X", 1, 10)
                        room.pit = True if pit else False
