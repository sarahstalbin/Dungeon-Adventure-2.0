"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""


class Room:
    """ Room class sets all the items necessary for the dungeon adventure and prints the layout of the room """

    def __init__(self):
        """ Initializing the items and setting it initially to False  """

        self.__healing_potion = False
        self.__vision_potion = False
        self.__pit = False
        self.__entrance = False
        self.__exit = False
        self.__impasse = False
        self.__visited = False
        self.__multiple_items = False
        self.__north_door = False
        self.__south_door = False
        self.__east_door = False
        self.__west_door = False
        self.__abstraction_pillar = False
        self.__encapsulation_pillar = False
        self.__inheritance_pillar = False
        self.__polymorphism_pillar = False
        self.__empty_room = False
        self.__current_room = False
        self.__player_traveled = False

    @property
    def healing_potion(self):
        """ gets healing potion boolean value using property decorator """
        return self.__healing_potion

    @property
    def vision_potion(self):
        """ gets vision boolean value using property decorator """
        return self.__vision_potion

    @property
    def pit(self):
        """ gets pit boolean value using property decorator """
        return self.__pit

    @property
    def multiple_items(self):
        """ gets multiple_items boolean value using property decorator """
        return self.__multiple_items

    @property
    def abstraction_pillar(self):
        """ gets abstraction_pillar boolean value using property decorator """
        return self.__abstraction_pillar

    @property
    def inheritance_pillar(self):
        """ gets inheritance_pillar boolean value using property decorator"""
        return self.__inheritance_pillar

    @property
    def polymorphism_pillar(self):
        """ gets polymorphism_pillar boolean value using property decorator"""
        return self.__polymorphism_pillar

    @property
    def encapsulation_pillar(self):
        """ gets encapsulation_pillar boolean value using property decorator"""
        return self.__encapsulation_pillar

    @property
    def north_door(self):
        """ gets north_door boolean value using property decorator """
        return self.__north_door

    @property
    def south_door(self):
        """ gets south_door boolean value using property decorator """
        return self.__south_door

    @property
    def east_door(self):
        """ gets east_door boolean value using property decorator"""
        return self.__east_door

    @property
    def west_door(self):
        """ gets west_door boolean value using property decorator """
        return self.__west_door

    @property
    def impasse(self):
        """ gets impasse boolean value using property decorator"""
        return self.__impasse

    @property
    def visited(self):
        """ gets visited boolean value using property decorator"""
        return self.__visited

    @property
    def empty_room(self):
        """ gets empty_room boolean value using property decorator """
        return self.__empty_room

    @property
    def entrance(self):
        """ gets entrance boolean value using property decorator"""
        return self.__entrance

    @property
    def exit(self):
        """ gets exit boolean value using property decorator """
        return self.__exit

    @property
    def current_room(self):
        """ gets current_room boolean value using property decorator """
        return self.__current_room

    @property
    def player_traveled(self):
        """ gets player_traveled boolean value using property decorator """
        return self.__player_traveled

    @player_traveled.setter
    def player_traveled(self, player_traveled):
        """ setting player_traveled using setter property
         :param player_traveled
         :return boolean value"""
        self.__player_traveled = player_traveled

    @healing_potion.setter
    def healing_potion(self, add_potion):
        """ setting healing_potion using setter property
        :param add_potion
        :return boolean value"""
        self.__healing_potion = add_potion

    @vision_potion.setter
    def vision_potion(self, vision_potion):
        """ setting vision_potion using setter property
            :param vision_potion
            :return boolean value"""
        self.__vision_potion = vision_potion

    @pit.setter
    def pit(self, reduce_potion):
        """ setting pit using setter property
            :param reduce_potion
            :return boolean value"""
        self.__pit = reduce_potion

    @north_door.setter
    def north_door(self, north_door):
        """ setting north_door using setter property
            :param north_door
            :return boolean value"""
        self.__north_door = north_door

    @south_door.setter
    def south_door(self, south_door):
        """ setting south_door using setter property
            :param south_door
            :return boolean value"""
        self.__south_door = south_door

    @east_door.setter
    def east_door(self, east_door):
        """ setting east_door using setter property
            :param east_door
            :return boolean value """
        self.__east_door = east_door

    @west_door.setter
    def west_door(self, west_door):
        """setting west_door using setter property
            :param west_door
            :return boolean value """
        self.__west_door = west_door

    @abstraction_pillar.setter
    def abstraction_pillar(self, abstraction_pillar):
        """ setting abstraction_pillar using setter property
            :param abstraction_pillar
            :return boolean value """
        self.__abstraction_pillar = abstraction_pillar

    @encapsulation_pillar.setter
    def encapsulation_pillar(self, encapsulation_pillar):
        """ setting encapsulation_pillar using setter property
            :param encapsulation_pillar
            :return boolean value """
        self.__encapsulation_pillar = encapsulation_pillar

    @inheritance_pillar.setter
    def inheritance_pillar(self, inheritance_pillar):
        """ setting inheritance_pillar using setter property
            :param inheritance_pillar
            :return boolean value"""
        self.__inheritance_pillar = inheritance_pillar

    @polymorphism_pillar.setter
    def polymorphism_pillar(self, polymorphism_pillar):
        """ setting polymorphism_pillar using setter property
            :param polymorphism_pillar
            :return boolean value """
        self.__polymorphism_pillar = polymorphism_pillar

    @empty_room.setter
    def empty_room(self, is_empty):
        """ setting empty_room using setter property
            :param is_empty
            :return boolean value """
        self.__empty_room = is_empty

    @entrance.setter
    def entrance(self, entrance):
        """ setting entrance using setter property
            :param entrance
            :return boolean value """
        self.__entrance = entrance

    @exit.setter
    def exit(self, exit_room):
        """ setting exit using setter property
            :param exit_room
            :return boolean value """
        self.__exit = exit_room

    @impasse.setter
    def impasse(self, impasse):
        """ setting impasse using setter property
            :param impasse
            :return boolean value """
        self.__impasse = impasse

    @visited.setter
    def visited(self, visited):
        """ setting visited using setter property
            :param visited
            :return boolean value """
        self.__visited = visited

    @multiple_items.setter
    def multiple_items(self, multiple_items):
        """ setting multiple_items using setter property
            :param multiple_items
            :return boolean value """
        self.__multiple_items = multiple_items

    @current_room.setter
    def current_room(self, current_room):
        """ setting current_room using setter property
            :param current_room
            :return boolean value """
        self.__current_room = current_room

    def can_enter(self):
        """ This method can be called if there is no impasse and if it is not visited """
        return not self.__impasse and not self.__visited

    def __str__(self):
        """ str method prints the layout of the room class with its abbreviated names and symbols"""
        layout = ""
        if self.__north_door:
            layout += "*_*"
        else:
            layout += "***"
        layout += "\n"
        if self.__west_door:
            layout += "|"
        else:
            layout += "*"
        if self.__healing_potion:
            layout += "H"
        elif self.__vision_potion:
            layout += "V"
        elif self.__pit:
            layout += "X"
        elif self.__entrance:
            layout += "i"
        elif self.__exit:
            layout += "O"
        elif self.__multiple_items:
            layout += "M"
        elif self.__empty_room:
            layout += " "
        elif self.__current_room:
            layout += "@"
        elif self.__abstraction_pillar:
            layout += "A"
        elif self.__polymorphism_pillar:
            layout += "P"
        elif self.__inheritance_pillar:
            layout += "I"
        elif self.__encapsulation_pillar:
            layout += "E"
        if self.__east_door:
            layout += "|"
        else:
            layout += "*"
        layout += "\n"
        if self.__south_door:
            layout += "*_*"
        else:
            layout += "***"
        return layout
