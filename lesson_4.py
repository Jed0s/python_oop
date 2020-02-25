from random import randrange
from time import sleep

class Unit:
    count = 0
    def __init__(self, t):
        self.id = Unit.count
        Unit.count += 1
        self.team = t

class Hero(Unit):
    def __init__(self, t):
        Unit.__init__(self, t)
        self.level = 1
    def level_up(self):
        self.level += 1


class Soldier(Unit):
    def __init__(self, t):
        Unit.__init__(self, t)
        self.my_hero = None
    def follow(self, hero):
        self.my_hero = hero.id
        if self.my_hero == 0:
            return "Follow the Batman."
        else:
            return "Follow the Joker."


def start():
    batman = Hero(1)
    batman_team = []
    joker = Hero(2)
    joker_team = []

    for i in range(20):
        n = randrange(2)
        if n == 0:
            batman_team.append(Soldier(n))
        else:
            joker_team.append(Soldier(n))
    print("Batman team: " + str(len(batman_team)) + " members")
    print("Joker team: " + str(len(joker_team)) + " members")

    if len(batman_team) > len(joker_team):
        batman.level_up()
    else:
        joker.level_up()
    print(batman_team[0].follow(batman))




start()

