from charecter import Charecter
import random

class Ninja(Charecter):
    def __init__(self, health, damage, defence, name):
        Charecter.__init__(self, name, health, defence, damage)

    def roll(self, heal):
        dash = random.randint(1, 1000)
        if dash <= 150:
            self.heal_count()
            self.health = self.health + heal



