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
        
    def attack(self, Creature):
        print('{} attacks you for {}.'.format(Creature.name, self.damage))
        
class Marvin(Creature):
    'the man himself'
    def attack(self, Creature):
        print('You attack {} for {}.'.format(Creature.name, self.damage))
        
    def heal(self):
        print('You heal for {}.'.format(self.jazz))
        

jeff = Creature('Jeff', 10, 2, 1)
alan = Creature('Alan', 10, 3, 1)
marvin = Marvin('Marvin', 17, 6, 5)

"""
combat handler
"""
playerChoice = raw_input('Enter things: ')

while (playerChoice != '0'):
    if (playerChoice=='1'):
        marvin.attack(jeff)
        jeff.attack(marvin)
        alan.attack(marvin)
    if (playerChoice=='2'):
        marvin.attack(alan)
        jeff.attack(marvin)
        alan.attack(marvin)
    if (playerChoice=='3'):
        marvin.heal()
        jeff.attack(marvin)
        alan.attack(marvin)
    playerChoice = raw_input('Enter things: ')