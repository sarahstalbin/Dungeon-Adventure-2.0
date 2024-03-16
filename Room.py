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
        # self.__multiple_items = False
        self.__north_door = False
        self.__south_door = False
        self.__east_door = False
        self.__west_door = False
        self.__abstraction_pillar = False
        self.__encapsulation_pillar = False
        self.__inheritance_pillar = False
        self.__polymorphism_pillar = False
        self.__empty_room = True
        self.__current_room = False
        self.__player_traveled = False
        self.__ogre = False
        self.__gremlin = False
        self.__skeleton = False
        self.__dragon = False
        self.__chimera = False
        self.__troll = False


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

    # @property
    # def multiple_items(self):
    #     """ gets multiple_items boolean value using property decorator """
    #     return self.__multiple_items

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
    def ogre(self):
        return self.__ogre

    @property
    def gremlin(self):
        return self.__gremlin

    @property
    def skeleton(self):
        return self.__skeleton

    @property
    def troll(self):
        return self.__troll

    @property
    def dragon(self):
        return self.__dragon


    @property
    def chimera(self):
        return self.__chimera

    @property
    def impasse(self):
        """ gets impasse boolean value using property decorator"""
        return self.__impasse

    @property
    def visited(self):
        """ gets visited boolean value using property decorator"""
        return self.__visited

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
        if not isinstance(player_traveled, bool):
            raise ValueError("player_traveled must be a boolean")
        self.__player_traveled = player_traveled

    @healing_potion.setter
    def healing_potion(self, add_potion):
        """ setting healing_potion using setter property
        :param add_potion
        :return boolean value"""
        if not isinstance(add_potion, bool):
            raise ValueError("healing_potion must be a boolean")
        self.__healing_potion = add_potion
        self.empty_room()

    @vision_potion.setter
    def vision_potion(self, vision_potion):
        """ setting vision_potion using setter property
            :param vision_potion
            :return boolean value"""
        if not isinstance(vision_potion, bool):
            raise ValueError("vision_potion must be a boolean")
        self.__vision_potion = vision_potion
        self.empty_room()

    @pit.setter
    def pit(self, reduce_potion):
        """ setting pit using setter property
            :param reduce_potion
            :return boolean value"""
        if not isinstance(reduce_potion, bool):
            raise ValueError("pit must be a boolean")
        self.__pit = reduce_potion
        self.empty_room()

    @north_door.setter
    def north_door(self, north_door):
        """ setting north_door using setter property
            :param north_door
            :return boolean value"""
        if not isinstance(north_door, bool):
            raise ValueError("north_door must be a boolean")
        self.__north_door = north_door

    @south_door.setter
    def south_door(self, south_door):
        """ setting south_door using setter property
            :param south_door
            :return boolean value"""
        if not isinstance(south_door, bool):
            raise ValueError("south_door must be a boolean")
        self.__south_door = south_door

    @east_door.setter
    def east_door(self, east_door):
        """ setting east_door using setter property
            :param east_door
            :return boolean value """
        if not isinstance(east_door, bool):
            raise ValueError("east_door must be a boolean")
        self.__east_door = east_door

    @west_door.setter
    def west_door(self, west_door):
        """setting west_door using setter property
            :param west_door
            :return boolean value """
        if not isinstance(west_door, bool):
            raise ValueError("west_door must be a boolean")
        self.__west_door = west_door

    @abstraction_pillar.setter
    def abstraction_pillar(self, abstraction_pillar):
        """ setting abstraction_pillar using setter property
            :param abstraction_pillar
            :return boolean value """
        if not isinstance(abstraction_pillar, bool):
            raise ValueError("abstraction_pillar must be a boolean")
        self.__abstraction_pillar = abstraction_pillar
        self.empty_room()

    @encapsulation_pillar.setter
    def encapsulation_pillar(self, encapsulation_pillar):
        """ setting encapsulation_pillar using setter property
            :param encapsulation_pillar
            :return boolean value """
        if not isinstance(encapsulation_pillar, bool):
            raise ValueError("encapsulation_pillar must be a boolean")
        self.__encapsulation_pillar = encapsulation_pillar
        self.empty_room()

    @inheritance_pillar.setter
    def inheritance_pillar(self, inheritance_pillar):
        """ setting inheritance_pillar using setter property
            :param inheritance_pillar
            :return boolean value"""
        if not isinstance(inheritance_pillar, bool):
            raise ValueError("inheritance_pillar must be a boolean")
        self.__inheritance_pillar = inheritance_pillar
        self.empty_room()

    @polymorphism_pillar.setter
    def polymorphism_pillar(self, polymorphism_pillar):
        """ setting polymorphism_pillar using setter property
            :param polymorphism_pillar
            :return boolean value """
        if not isinstance(polymorphism_pillar, bool):
            raise ValueError("polymorphism_pillar must be a boolean")
        self.__polymorphism_pillar = polymorphism_pillar
        self.empty_room()

    def empty_room(self):
        """ setting empty_room using setter property
            :param is_empty
            :return boolean value """
        # if not isinstance(is_empty, bool):
        #     raise ValueError("empty_room must be a boolean")

        if self.__str__()[5] == " " or self.__str__()[5] == "|" or self.__str__()[5] == "*":
            self.__empty_room = True
        else:
            self.__empty_room = False
        return self.__empty_room

    @ogre.setter
    def ogre(self, ogre):
        if not isinstance(ogre, bool):
            raise ValueError("ogre must be a boolean")
        self.__ogre = ogre
        self.empty_room()

    @gremlin.setter
    def gremlin(self, gremlin):
        if not isinstance(gremlin, bool):
            raise ValueError("gremlin must be a boolean")
        self.__gremlin = gremlin
        self.empty_room()

    @skeleton.setter
    def skeleton(self, skeleton):
        if not isinstance(skeleton, bool):
            raise ValueError("skeleton must be a boolean")
        self.__skeleton = skeleton
        self.empty_room()

    @troll.setter
    def troll(self, troll):
        if not isinstance(troll, bool):
            raise ValueError("skeleton must be a boolean")
        self.__troll = troll
        self.empty_room()


    @dragon.setter
    def dragon(self, dragon):
        if not isinstance(dragon, bool):
            raise ValueError("dragon must be a boolean")
        self.__dragon = dragon
        self.empty_room()

    @chimera.setter
    def chimera(self, chimera):
        if not isinstance(chimera, bool):
            raise ValueError("chimera must be a boolean")
        self.__chimera = chimera
        self.empty_room()

    @entrance.setter
    def entrance(self, entrance):
        """ setting entrance using setter property
            :param entrance
            :return boolean value """
        if not isinstance(entrance, bool):
            raise ValueError("entrance must be a boolean")
        self.__entrance = entrance
        self.empty_room()

    @exit.setter
    def exit(self, exit_room):
        """ setting exit using setter property
            :param exit_room
            :return boolean value """
        if not isinstance(exit_room, bool):
            raise ValueError("exit must be a boolean")
        self.__exit = exit_room
        self.__empty_room = not exit_room

    @impasse.setter
    def impasse(self, impasse):
        """ setting impasse using setter property
            :param impasse
            :return boolean value """
        if not isinstance(impasse, bool):
            raise ValueError("impasse must be a boolean")
        self.__impasse = impasse

    @visited.setter
    def visited(self, visited):
        """ setting visited using setter property
            :param visited
            :return boolean value """
        if not isinstance(visited, bool):
            raise ValueError("visited must be a boolean")
        self.__visited = visited

    @current_room.setter
    def current_room(self, current_room):
        """ setting current_room using setter property
            :param current_room
            :return boolean value """
        if not isinstance(current_room, bool):
            raise ValueError("current_room must be a boolean")
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
        if self.__vision_potion:
            layout += "V"
        if self.__entrance:
            layout += "i"
        if self.__exit:
            layout += "O"
        # if self.__multiple_items:
        #     layout += "M"
        if self.__ogre:
            layout += "%"
        if self.__skeleton:
            layout += "$"
        if self.__gremlin:
            layout += "&"
        if self.__dragon:
            layout += "^"
        if self.__chimera:
            layout += "~"
        if self.__troll:
            layout += "#"
        if self.__abstraction_pillar:
            layout += "A"
        if self.__polymorphism_pillar:
            layout += "P"
        if self.__inheritance_pillar:
            layout += "I"
        if self.__encapsulation_pillar:
            layout += "E"
        if self.__pit:
            layout += "X"
        if self.__empty_room:
            layout += " "
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


if __name__ == "__main__":
    r = Room()
    # r.empty_room = False
    # r.healing_potion = True
    print(str(r)[5])