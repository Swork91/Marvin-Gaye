'''
Created on May 1, 2018

@author: Sam
'''
from pip._vendor.distlib.compat import raw_input
print ('Welcome to Marvin Gaye\'s Quest To Go Bowling \n')

class Creature:
    'Common base class for all creatures'
    
    def __init__(self, name, albums, jazz, damage):
        self.name = name
        self.albums = albums # health
        self.damage = damage
        self.jazz = jazz # magic damage
        
    def __repr__(self):
        return "Creature('{}', {}, {}, {})".format(self.name, self.albums, self.jazz, self.damage)

    def __str__(self):
        return " Name: {}\n Albums: {}\n Damage: {}".format(self.name, self.albums, self.damage)

    def attack(self, Creature):
        print('{} attacks you for {}.'.format(self.name, self.damage))
        Creature.albums-=self.damage
        
    def checkIfDead(self):
        if self.albums<=0:
            print("{} has died".format(self.name))
        
class Marvin(Creature):
    'the man himself'
    def attack(self, Creature):
        print('You attack {} for {}.'.format(Creature.name, self.damage))
        Creature.albums-=self.damage
        
    def heal(self):
        print('You heal for {}.'.format(self.jazz))
        self.albums+=self.jazz
        
marvin = Marvin('Marvin', 17, 6, 5) # Create marvin right away since hes kinda important to everything? 

'''
combat handlers
'''
def combatOneOnOne(Creature1):
    playerChoice = raw_input('Enter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target
            marvin.attack(Creature1)
            Creature1.attack(marvin)
            Creature1.checkIfDead()
        if (playerChoice=='2'): # Heal self
            marvin.heal()
            Creature1.attack(marvin)
        if (playerChoice=='3'): # inspect self
            print(marvin)
        if (playerChoice=='4'): # inspect target
            print(Creature1)
        if (playerChoice=='9'): # Display options
            print(" 1 to attack '{}'\n 2 to Heal\n 3 to inspect '{}'\n 4 to inspect '{}'\n 9 to show this\n 0 to quit".format(Creature1.name, marvin.name, Creature1.name))

        playerChoice = raw_input('Enter things: ')
        
def combatOneOnTwo(Creature1, Creature2):
    playerChoice = raw_input('Enter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target 1
            marvin.attack(Creature1)
            Creature1.attack(marvin)
            Creature2.attack(marvin)
        if (playerChoice=='2'): # attack target 2
            marvin.attack(Creature2)
            Creature1.attack(marvin)
            Creature2.attack(marvin)
        if (playerChoice=='3'): # Heal self
            marvin.heal()
            Creature1.attack(marvin)
            Creature2.attack(marvin)
        if (playerChoice=='4'): # inspect self
            print(marvin)
        if (playerChoice=='5'): # inspect target 1
            print(Creature1)
        if (playerChoice=='6'): # inspect target 2
            print(Creature2)
        if (playerChoice=='9'): # Display options
            print(" 1 to attack '{}'\n 2 to attack '{}'\n 3 to Heal\n 4 to inspect '{}'\n 5 to inspect '{}'\n 6 to inspect '{}'\n 9 to show this\n 0 to quit".format(Creature1.name, Creature2.name, marvin.name, Creature1.name, Creature2.name))
        playerChoice = raw_input('Enter things: ')
        
def combatOneOnThree(Creature1, Creature2, Creature3):
    playerChoice = raw_input('Enter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target 1
            marvin.attack(Creature1)
            Creature1.attack(marvin)
            Creature2.attack(marvin)
            Creature3.attack(marvin)
        if (playerChoice=='2'): # attack target 2
            marvin.attack(Creature2)
            Creature1.attack(marvin)
            Creature2.attack(marvin)
            Creature3.attack(marvin)
        if (playerChoice=='3'): # attack target 3
            marvin.attack(Creature3)
            Creature1.attack(marvin)
            Creature2.attack(marvin)
            Creature3.attack(marvin)
        if (playerChoice=='4'): # Heal self
            marvin.heal()
            Creature1.attack(marvin)
            Creature2.attack(marvin)
            Creature3.attack(marvin)
        if (playerChoice=='5'): # inspect self
            print(marvin)
        if (playerChoice=='6'): # inspect target 1
            print(Creature1)
        if (playerChoice=='7'): # inspect target 2
            print(Creature2)
        if (playerChoice=='8'): # inspect target 3
            print(Creature3)
        if (playerChoice=='9'): # Display options
            print(" 1 to attack '{}'\n 2 to attack '{}'\n 3 to attack '{}'\n 4 to Heal\n 5 to inspect '{}'\n 6 to inspect '{}'\n 7 to inspect '{}'\n 8 to inspect '{}'\n 0 to quit".format(Creature1.name, Creature2.name, Creature3.name, marvin.name, Creature1.name, Creature2.name, Creature3.name))
        playerChoice = raw_input('Enter things: ')

jeff = Creature('Jeff', 10, 2, 1)
alan = Creature('Alan', 10, 3, 1)
tim = Creature('Tim', 10, 1, 1)

combatOneOnOne(alan)
combatOneOnTwo(jeff, alan)
combatOneOnThree(jeff, alan, tim)

