from charecter import Charecter
import random

class Assasin(Charecter):
    def __init__(self, health, damage, defence, name):
        Charecter.__init__(self, name, health, defence, damage)

    def setDamage(self):
        brut = random.randint(1, 1000)
        if brut <= 100:
            self.attaka = 65
        else:
            self.attaka = self.damage