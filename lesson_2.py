import random
import time

class Warrior:
    health = 100
    def makeHealth(self, value):
        self.health = value
    def makeKick(self):
        self.health -= 20


def fight_start():
    while(unitJoy.health > 0 and unitRoy.health > 0):
        choice = random.randrange(2)
        if choice == 0:
            unitJoy.makeKick() # Joy get damage
            print("Roy hit Joy")
            time.sleep(1)
            print("Joy have " + str(unitJoy.health) + " hp")
        else:
            unitRoy.makeKick() # Roy get damage
            print("Joy hit Roy")
            time.sleep(1)
            print("Roy have " + str(unitRoy.health) + " hp")
        time.sleep(2)
    if unitJoy.health > unitRoy.health:
        print("Joy won")
    else:
        print("Roy won")


unitJoy = Warrior()
unitJoy.makeHealth(100)
unitRoy = Warrior()
unitRoy.makeHealth(100)
fight_start()