import time
import random


class NotEnougResource(Exception):
    def __init__(self, messege="У человека закончелись ресрурсы!"):
        Exception.__init__(self, messege)

class Person:
    name =("")
    health = 0
    mood = 0
    money = 1.0


#    def work(self):
#        print("work "+self.name)
#        self.health = self.health - random.randint(10, 100)
#        self.mood = self.mood - random.randint(20, 100)
#        self.money = self.money + random.randint(100, 300)
#
#    def relax(self):
#        print("relax " + self.name)
#        self.health = self.health + random.randint(20, 50)
#        self.mood = self.mood + random.randint(50, 60)
#        self.money = self.money - random.randint(10, 100)


    def __init__(self, name, health, mood, money):
         self.name = name
         self.health = health
         self.mood = mood
         self.money = money



    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health} \n' \
            f' Настроение: {self.mood}\n' \
            f' Финансы: {self.money}\n'

    def change_state(self, health, mood, money):
       # self.health = self.health + health
       # self.mood = self.mood + mood
      # self.money = self.money + money
        i = 0
        o = 0
        p = 0
        if self.health <= 0:
            i = 1
            self.health = 0
        if self.money <= 0:
            p = 1
            self.money = 0
        if self.mood <= 0:
            o = 1
            self.mood = 0

        time.sleep(2)
        if i == 1 and p == 1 and o == 1:
            raise NotEnougResource
        return

    def type(self):
       return self.__class__

    def begin_do(self, WhatToDo1, WhatToDo2, WhatToDo3):
        j = random.randint(1, 3)
        if j == 1:
            self.do(WhatToDo1)

        if j == 2:
            self.do(WhatToDo2)

        if j == 3:
            self.do(WhatToDo3)

    def do(self, WhatToDo):

        self.addmoney(WhatToDo.money)
        self.addmood(WhatToDo.mood)
        self.addhealth(WhatToDo.health)
        self.isDie()
        time.sleep(2)


    def stroke(self):
        print("-------------------------")

    def addmoney(self, money):
        if self.money > 0:
            self.money += money
        if self.money < 0:
            self.money = 0

    def addmood(self, mood):
        if self.mood > 0:
            self.mood += mood
        if self.mood < 0:
            self.mood = 0

    def addhealth(self, health):
       # print(self.name, self.health, health)
        if self.health > 0:
            self.health += health
        if self.health < 0:
            self.health = 0

    def isDie(self):
        if self.health == 0 and self.mood == 0 and self.money == 0:
            raise NotEnougResource


class Action(Person):
    def __init__(self, name, health, mood, money):
         self.name = name
         self.health = health
         self.mood = mood
         self.money = money



class Work(Action):
    def __init__(self, name, health, mood, money):
         self.name = name
         self.health = health
         self.mood = mood
         self.money = money

    def addmoney(self, money):
        if self.money > 0:
            if self.mood >= 90:
                self.money += money * 1.1
            else:
                self.money += money

        if self.money < 0:
            self.money = 0

class Relax(Action):
    def __init__(self, name, health, mood, money):
         self.name = name
         self.health = health
         self.mood = mood
         self.money = money

    #def addrelax(self, health, mood):
    #    if self.mood or self.health > 0:
    #        if self.health <= 40:
    #            self.mood -= mood * 0.6
    #            self.health += health
    #        else:
    #            self.mood += mood
    #
    #    elif self.money < 0:
    #        self.money = 0


Go_to_hospital = Action(name = 'go to hospital',  money = -20, mood = -5, health = 2)
Go_to_factory = Work(name = 'go to factory', money = 5, mood = -10, health = -10)
Go_To_park = Relax(name="go to the park", health= 1,  mood= 2, money=0)
object2 = Person(health = 9, name = "Andrey", mood = 10, money = 80)
object1 = Person(health = 100, name = "Vasya", mood = 200, money = 200)
object3 = Person(health = 200, name = "Oleg", mood = 100, money = 390)

while True:

        print(object1)
        print(object2)
        print(object3)



        object1.stroke()


        object2.begin_do(Go_To_park, Go_to_factory, Go_to_hospital)
        object3.begin_do(Go_To_park, Go_to_factory, Go_to_hospital)
        object1.begin_do(Go_To_park, Go_to_factory, Go_to_hospital)

 #       object1.change_state()
#       object2.change_state()
#       object3.change_state()
        #print(object1)
    #      print(object3)
#       object1.stroke()
