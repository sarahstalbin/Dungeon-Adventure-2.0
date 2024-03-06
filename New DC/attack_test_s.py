from DungeonCharacterFactory import DungeonCharacterFactory

d = DungeonCharacterFactory.create_character("skeleton", "Dreadbone")
w = DungeonCharacterFactory.create_character("warrior", "Warrior")

w.attack(d)
