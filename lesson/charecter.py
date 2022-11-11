class Charecter:
    name = ""
    damage = 1
    health = 100
    defence = 1

    def __init__(self, name, health, damage, defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.attaka = self.damage
    def __str__(self):
       return f'=={self.name}==\n' \
              f' Здоровье: {self.health}\n' \
              f' Урон: {self.attaka}\n' \
              f' Защита: {self.defence}\n'

    def setDamage(self):
        self.attaka = self.damage

    def stroke(self):
        print('-----------------')
    def take_damage(self,damage):
        self.health -= max(damage, 1)
    def attack(self, target):
        self.setDamage()

        target.take_damage(self.attaka)
    def is_alive(self):
        return self.health < 0
# if self.health < 0:
#    print(f'{self.name} умер')
#
    def heal_count (self):
        self.heal = self.damage








