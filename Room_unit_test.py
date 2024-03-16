import unittest
from Room import Room


class TestRoomGettersAndSetters(unittest.TestCase):
    def setUp(self):
        self.room = Room()  # Creating an instance of the Room class for testing

    def test_healing_potion(self):
        """ Test healing potion method"""
        self.assertFalse(self.room.healing_potion)  # Initial value should be False
        self.room.healing_potion = True
        self.assertTrue(self.room.healing_potion)

    def test_vision_potion(self):
        """ Test vision potion method"""
        self.assertFalse(self.room.vision_potion)  # Initial value should be False
        self.room.vision_potion = True
        self.assertTrue(self.room.vision_potion)

    def test_pit(self):
        """ Test pit method"""
        self.assertFalse(self.room.pit)  # Initial value should be False
        self.room.pit = True
        self.assertTrue(self.room.pit)

    def test_entrance(self):
        """ Test entrance method"""
        self.assertFalse(self.room.entrance)  # Initial value should be False
        self.room.entrance = True
        self.assertTrue(self.room.entrance)

    def test_exit(self):
        """ Test exit method"""
        self.assertFalse(self.room.exit)  # Initial value should be False
        self.room.exit = True
        self.assertTrue(self.room.exit)

    def test_impasse(self):
        """ Test impasse method"""
        self.assertFalse(self.room.impasse)  # Initial value should be False
        self.room.impasse = True
        self.assertTrue(self.room.impasse)

    def test_visited(self):
        """ Test visited method"""
        self.assertFalse(self.room.visited)  # Initial value should be False
        self.room.visited = True
        self.assertTrue(self.room.visited)

    def test_north_door(self):
        """ Test north door method"""
        self.assertFalse(self.room.north_door)  # Initial value should be False
        self.room.north_door = True
        self.assertTrue(self.room.north_door)

    def test_south_door(self):
        """ Test south door method"""
        self.assertFalse(self.room.south_door)  # Initial value should be False
        self.room.south_door = True
        self.assertTrue(self.room.south_door)

    def test_east_door(self):
        """ Test east door method"""
        self.assertFalse(self.room.east_door)  # Initial value should be False
        self.room.east_door = True
        self.assertTrue(self.room.east_door)

    def test_west_door(self):
        """ Test west door method"""
        self.assertFalse(self.room.west_door)  # Initial value should be False
        self.room.west_door = True
        self.assertTrue(self.room.west_door)

    def test_encapsulation_pillar(self):
        """ Test encapsulation pillar method"""
        self.assertFalse(self.room.encapsulation_pillar)  # Initial value should be False
        self.room.encapsulation_pillar = True
        self.assertTrue(self.room.encapsulation_pillar)

    def test_polymorphism_pillar(self):
        """ Test polymorphism pillar method"""
        self.assertFalse(self.room.polymorphism_pillar)  # Initial value should be False
        self.room.polymorphism_pillar = True
        self.assertTrue(self.room.polymorphism_pillar)

    def test_inheritance_pillar(self):
        """ Test inheritance pillar method"""
        self.assertFalse(self.room.inheritance_pillar)  # Initial value should be False
        self.room.inheritance_pillar = True
        self.assertTrue(self.room.inheritance_pillar)

    def test_abstraction_pillar(self):
        """ Test abstraction pillar method"""
        self.assertFalse(self.room.abstraction_pillar)  # Initial value should be False
        self.room.abstraction_pillar = True
        self.assertTrue(self.room.abstraction_pillar)

    def test_empty_room(self):
        """ Test empty room method"""
        self.assertTrue(self.room.empty_room)

    def test_current_room(self):
        """ Test current room method"""
        self.assertFalse(self.room.current_room)  # Initial value should be False
        self.room.current_room = True
        self.assertTrue(self.room.current_room)

    def test_player_traveled(self):
        """ Test player_traveled method"""
        self.assertFalse(self.room.player_traveled)  # Initial value should be False
        self.room.player_traveled = True
        self.assertTrue(self.room.player_traveled)

    def test_ogre(self):
        """ Test ogre method"""
        self.assertFalse(self.room.ogre)  # Initial value should be False
        self.room.ogre = True
        self.assertTrue(self.room.ogre)

    def test_gremlin(self):
        """ Test gremlin method"""
        self.assertFalse(self.room.gremlin)  # Initial value should be False
        self.room.gremlin = True
        self.assertTrue(self.room.gremlin)

    def test_chimera(self):
        """ Test chimera method"""
        self.assertFalse(self.room.chimera)  # Initial value should be False
        self.room.chimera = True
        self.assertTrue(self.room.chimera)

    def test_troll(self):
        """ Test troll method"""
        self.assertFalse(self.room.troll)  # Initial value should be False
        self.room.troll = True
        self.assertTrue(self.room.troll)

    def test_dragon(self):
        """ Test dragon method"""
        self.assertFalse(self.room.dragon)  # Initial value should be False
        self.room.dragon = True
        self.assertTrue(self.room.dragon)

    def test_can_enter(self):
        # Test if can_enter method returns True when there is no impasse and the room is not visited
        self.assertTrue(self.room.can_enter())

        # Setting impasse to True and visited to True
        self.room.impasse = True
        self.room.visited = True

        # Test if can_enter method returns False when there is an impasse
        self.assertFalse(self.room.can_enter())

        # Setting impasse to False and visited to True
        self.room.impasse = False

        # Test if can_enter method returns False when the room is visited
        self.assertFalse(self.room.can_enter())

    def test_str_representation(self):
        # Test the __str__ method to ensure it returns the correct layout of the room
        expected_layout = "***\n* *\n***"
        self.assertEqual(str(self.room), expected_layout)

        # Test another layout
        self.room.healing_potion = True
        self.room.entrance = True
        expected_layout = "***\n*Hi*\n***"
        self.assertEqual(str(self.room), expected_layout)

        #  Test another layout
        self.room.west_door = True
        self.room.chimera = True
        self.room.encapsulation_pillar = True
        expected_layout = "***\n|Hi~E*\n***"
        self.assertEqual(str(self.room), expected_layout)

if __name__ == '__main__':
    unittest.main()
