from charecter import Charecter
from asassin import Assasin
from ninja import Ninja
import time
a = input("your name> ")
b = input("player 2 name> ")
player1 = Assasin(name=a,defence=11,damage=3,health=100)
player2 = Ninja(name=b,defence=11,damage=2,health=100)
admin = Charecter(name="admin", damage=200, defence=100,health=200 )
while True:

    player1.attack(player2)
    player2.attack(player1)
    player1.is_alive()
    player2.is_alive()
    player2.roll(heal=player1.damage)


    print(player1)
    print(player2)
    time.sleep(2)
    admin.stroke()
    if player1.health <=0 or player2.health <=0:
        break
    else:
        continue

