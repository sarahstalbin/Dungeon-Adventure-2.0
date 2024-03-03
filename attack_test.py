from Monster import Monster, Skeleton, Ogre, Gremlin
# from Hero import Hero, Thief, Warrior, Priestess
from Hero import Warrior

class Attack:

    def create_characters(self):
        s = Skeleton('skele john')
        o = Ogre('oge jacob')
        g = Gremlin('grem jingle')
        # t = Thief()
        w = Warrior()
        # p = Priestess()

        # s.attack(t)  # monster attack
        # o.attack(t)  # monster attack
        # g.attack(t)  # monster attack

        # s.attack(w)  # monster attack
        print("Ogre attacking warrior")
        o.attack(w)  # monster attack
        # g.attack(w)  # monster attack

        # s.attack(p)  # monster attack
        # o.attack(p)  # monster attack
        # g.attack(p)  # monster attack
        #
        # p.attack(o) #hero attack
        # t.attack(o) #hero attack
        print("Warrior attacking ogre")
        w.attack(o) #hero attack
        #
        # p.attack(g) #hero attack
        # t.attack(g) #hero attack
        # w.attack(g) #hero attack
        #
        # p.attack(s) #hero attack
        # t.attack(s) #hero attack
        # w.attack(s) #hero attack

    def attack_characters(self, attacker, defender):
        attacker.attack(defender) # true if attack was successful, false if not

    def attack_special(self, attacker, defender):
        pass
        # g.special_skill(t) #hero special attack
        # attack_opponent_based_on_attack_speed(s, t)

    # def attack_opponent_based_on_attack_speed(self, opponent):

        #
        # if self.attack_speed >= opponent.attack_speed:  # self is the hero and opponent is the monster
        #     a_attack_speed = self.attack_speed / self.attack_speed
        #     b_attack_speed = opponent.attack_speed / self.attack_speed
        # else:
        #     a_attack_speed = self.attack_speed / opponent.attack_speed
        #     b_attack_speed = opponent.attack_speed / opponent.attack_speed
        # while self.hit_points > 0 and opponent.hit_points > 0:
        #     a_dps = a_attack_speed * self.calculate_damage()  # a_dps means a's damage per second
        #     b_dps = b_attack_speed * opponent.calculate_damage()  # b_dps means b's damage per second
        #     self.get_damage(b_dps)
        #     opponent.get_damage(a_dps)

if __name__ == "__main__":
    attack = Attack()
    attack.create_characters()
# attack.attack_characters()