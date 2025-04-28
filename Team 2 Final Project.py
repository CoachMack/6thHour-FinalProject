#Names:Logan,Elijah,Ryan
#Team:2
#Class: 6th Hour
#Assignment: Final Project

# https://docs.google.com/document/d/1Nf8NS5SYq5r-W5JxybsTVA2rOSIt7oYDnqMa_4sEEkE/edit?usp=sharing
import random, time


class Character:
    def __init__(self, maxhealth, damage, speed, iq, strength, armor, health, magic):
        self.maxhealth = maxhealth
        self.damage = damage
        self.speed = speed
        self.iq = iq
        self.strength = strength
        self.armor = armor
        self.health = health
        self.magic = magic

    def heal(self, target):
        heal_amount = 30
        target.health += heal_amount
        if target.health > 100:
            target.health = 100

    def take_damage(self):
        for i in range(10):
            damage_taken = random.randint(1, 6)
            self.health -= damage_taken
            print(f"character takes {damage_taken} damage. New health: {self.health}")
            time.sleep(1)

    def magic_used(self):
        mp_used = random.randint(1, 10)
        self.mp -= mp_used
        print(f"character has {self.magic} left")
        time.sleep(1)

    def dmgBuff(self):
        self.damage += 50


# Characters
warrior = Character(750, 100, 50, 90, 175, 20, 750, 0)
thief = Character(600, 80, 70, 110, 120, 10, 600, 0)
wizard = Character(500, 130, 40, 160, 100, 20, 500, 100)

# enemies
wolf = Character(350, 80, 90, 100, 45, 10, 350, 0)
bear = Character(800, 100, 70, 100, 100, 50, 800, 0)
troll = Character(850, 150, 50, 100, 150, 50, 850, 0)
dark_entity = Character(1500, 150, 60, 300, 5000, 20, 1500, 150)
guard = Character(750, 100, 50, 90, 175, 20, 750, 0)


def first_apperance():
    print('Hello welcome to your adventure')
    name = input('Who would you like to be known as: ')
    choice = int(input('ok now what would you like to be, warrior(1) thief(2) or wizard(3): '))
    if choice == 1:
        warriorJourney()
    if choice == 2:
        thiefJourney()
    if choice == 3:
        wizardJourney()


def warriorJourney():
    print('You start at the kingdom as a kings knight but once you return to your home you get a letter from a neighboring kingdom that needs your help and will reward you with glory and power')
    acception = int(input('do you want to accept(1) or decline(2): '))

    if acception == 1:
        global name
        print('you pack up your stuff and plan to leave by morning')
        time.sleep(2)
        print('you go to sleep but wake up to see an unknown dark figure above you, it bursts out the door but you grab you stuff and run out to chase it but once you get out its gone')
        time.sleep(7)
        print('an old friend sees your panic, "hey',name,' whats the rush, are you ok", you say your fine and head off to the kingdom with nothing but the clothes on your back and a simple sword')
        time.sleep(7)



    #ending number 1
    elif acception == 2:
        print('You stayed at your kingdom to serve your king and stay loyal till you die')
        exit()
    else:
        print('not an option, pick 1 or 2')
        warriorJourney()
def thiefJourney():
    print()

def wizardJourney():
    print()

first_apperance()
