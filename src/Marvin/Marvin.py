'''
Created on May 1, 2018

@author: Sam
'''
from pip._vendor.distlib.compat import raw_input
print ('Welcome to Marvin Gaye\'s Quest To Go Bowling \n')

class Monster:
    'Common base class for all enemys'
    
    def __init__(self, name, albums, jazz):
        self.name = name
        self.albums = albums # health
        self.jazz = jazz # attack damage
        
    def attack(self):
        print(self.name + ' attacks')

class Marvin(Monster):
    'the man himself'

            
jeff = Monster('Jeff', 10, 2)
alan = Monster('Alan', 10, 3)
marvin = Marvin('Marvin', 17, 6)

"""
combat handler
"""
playerChoice = raw_input('Enter things: ')
while (playerChoice != 0):
    if (playerChoice==1):
        marvin.attack()
    if (playerChoice==2):
        print(marvin.name + ' sleeps')
    if (playerChoice==3):
        print(marvin.name + ' eats')
    playerChoice = raw_input('Enter things: ')