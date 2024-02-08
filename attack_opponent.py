def attack_opponent_based_on_attack_speed(opponent):
    if self._attack_speed >= opponent._attack_speed: # self is the hero and opponent is the monster
        a_attack_speed = self._attack_speed / self._attack_speed
        b_attack_speed = opponent._attack_speed / self._attack_speed
    else:
        a_attack_speed = self._attack_speed / opponent._attack_speed
        b_attack_speed = opponent._attack_speed / opponent._attack_speed
    while self._hit_points > 0 and opponent._hit_points > 0:
        a_dps = a_attack_speed * self.calculate_damage() # a_dps means a's damage per second
        b_dps = b_attack_speed * opponent.calculate_damage() # b_dps means b's damage per second
        self.get_damage(b_dps)
        opponent.get_damage(a_dps)
