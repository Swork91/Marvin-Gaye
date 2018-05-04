'''
Created on May 1, 2018

@author: Sam
'''
from pip._vendor.distlib.compat import raw_input
import sys
print ('Welcome to Marvin Gaye\'s Quest To Go Bowling')

class Creature:
    'Common base class for all creatures'
    
    def __init__(self, name, albums, jazz, damage):
        self.name = name
        self.albums = albums # health
        self.maxHealth = albums
        self.damage = damage
        self.jazz = jazz # magic damage
        
    def __repr__(self):
        return "Creature('{}', {}, {}, {})".format(self.name, self.albums, self.jazz, self.damage)

    def __str__(self):
        return " Name: {}\n Albums: {}\n Damage: {}".format(self.name, self.albums, self.damage)

    def attack(self, Creature):
        print('{} attacks you for {}.'.format(self.name, self.damage))
        Creature.albums-=self.damage
               
class Marvin(Creature):
    'the man himself'
    
    def attack(self, Creature):
        print('You attack {} for {}.'.format(Creature.name, self.damage))
        Creature.albums-=self.damage
        
    def heal(self):
        self.albums+=self.jazz
        if (self.maxHealth<self.albums):
            print('You heal for {}.'.format(self.maxHealth-(self.albums-self.jazz)))
            self.albums = self.maxHealth
        else:
            print('You heal for {}.'.format(self.jazz))
        
marvin = Marvin('Marvin', 17, 6, 5) # Create marvin right away since hes kinda important to everything? 

'''
combat handlers
'''
def combatOneOnOne(Creature1):
    playerChoice = raw_input('\n\nEnter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target
            if (Creature1.albums <= 0):
                print("'{}' is already long gone".format(Creature1.name))
            else:
                marvin.attack(Creature1)
                if (Creature1.albums <= 0):
                    print ("'{}' bites it.".format(Creature1.name))
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='2'): # Heal self
            marvin.heal()
            if (Creature1.albums <= 0):
                pass
            else:
                Creature1.attack(marvin)
                if (marvin.albums<0): #dead check
                    return False
        if (playerChoice=='3'): # inspect self
            print(marvin)
        if (playerChoice=='4'): # inspect target
            print(Creature1)
        if (playerChoice=='9'): # Display options
            print(" 1 to attack '{}'\n 2 to Heal\n 3 to inspect '{}'\n 4 to inspect '{}'\n 9 to show this\n 0 to quit".format(Creature1.name, marvin.name, Creature1.name))
        if ((Creature1.albums <=0)): # all foes defeated
            #playerChoice = '0'
            return True
        else:
            playerChoice = raw_input('\nEnter things: ')
    return False # quit
        
def combatOneOnTwo(Creature1, Creature2):
    playerChoice = raw_input('\n\nEnter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target 1
            if (Creature1.albums <= 0):
                print("'{}' is already long gone".format(Creature1.name))
            else:
                marvin.attack(Creature1)
                if (Creature1.albums <= 0):
                    print ("'{}' bites it.".format(Creature1.name))
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature2.albums <= 0):
                    pass
                else:
                    Creature2.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='2'): # attack target 2
            if (Creature2.albums <= 0):
                print("'{}' is already long gone".format(Creature2.name))
            else:
                marvin.attack(Creature2)
                if (Creature2.albums <= 0):
                    print ("'{}' bites it.".format(Creature2.name))
                else:
                    Creature2.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature1.albums <= 0):
                    pass
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='3'): # Heal self
            marvin.heal()
            if (Creature1.albums <= 0):
                pass
            else:
                Creature1.attack(marvin)
                if (marvin.albums<0): #dead check
                    return False
            if (Creature2.albums <= 0):
                pass
            else:
                Creature2.attack(marvin)
                if (marvin.albums<0): #dead check
                    return False
        if (playerChoice=='4'): # inspect self
            print(marvin)
        if (playerChoice=='5'): # inspect target 1
            print(Creature1)
        if (playerChoice=='6'): # inspect target 2
            print(Creature2)
        if (playerChoice=='9'): # Display options
            print(" 1 to attack '{}'\n 2 to attack '{}'\n 3 to Heal\n 4 to inspect '{}'\n 5 to inspect '{}'\n 6 to inspect '{}'\n 9 to show this\n 0 to quit".format(Creature1.name, Creature2.name, marvin.name, Creature1.name, Creature2.name))
        if ((Creature1.albums <=0) & (Creature2.albums <=0)):# all foes defeated
            return True
        else:
            playerChoice = raw_input('\nEnter things: ')
    return False
        
def combatOneOnThree(Creature1, Creature2, Creature3):
    playerChoice = raw_input('\n\nEnter things: ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack target 1
            if (Creature1.albums <= 0):
                print("'{}' is already long gone".format(Creature1.name))
            else:
                marvin.attack(Creature1)
                if (Creature1.albums <= 0):
                    print ("'{}' bites it.".format(Creature1.name))
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature2.albums <= 0):
                    pass
                else:
                    Creature2.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature3.albums <= 0):
                    pass
                else:
                    Creature3.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='2'): # attack target 2
            if (Creature2.albums <= 0):
                print("'{}' is already long gone".format(Creature2.name))
            else:
                marvin.attack(Creature2)
                if (Creature2.albums <= 0):
                    print ("'{}' bites it.".format(Creature2.name))
                else:
                    Creature2.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature1.albums <= 0):
                    pass
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature3.albums <= 0):
                    pass
                else:
                    Creature3.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='3'): # attack target 3
            if (Creature3.albums <= 0):
                print("'{}' is already long gone".format(Creature3.name))
            else:
                marvin.attack(Creature3)
                if (Creature3.albums <= 0):
                    print ("'{}' bites it.".format(Creature3.name))
                else:
                    Creature3.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature1.albums <= 0):
                    pass
                else:
                    Creature1.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
                if (Creature2.albums <= 0):
                    pass
                else:
                    Creature2.attack(marvin)
                    if (marvin.albums<0): #dead check
                        return False
        if (playerChoice=='4'): # Heal self
            marvin.heal()
            if (Creature1.albums <= 0):
                pass
            else:
                Creature1.attack(marvin)
                if (marvin.albums<0): #dead check
                        return False
            if (Creature2.albums <= 0):
                pass
            else:
                Creature2.attack(marvin)
                if (marvin.albums<0): #dead check
                        return False
            if (Creature3.albums <= 0):
                pass
            else:
                Creature3.attack(marvin)
                if (marvin.albums<0): #dead check
                        return False
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
        if ((Creature1.albums <=0) & (Creature2.albums <=0) & (Creature3.albums <=0)):
            return True
        else:
            playerChoice = raw_input('\nEnter things: ')
    return False

def gameOver():
    print('Game over. Thanks for playing.')
    sys.exit()
    
def combatVictory():
    print('You have defeated all foes, you are the jazz master.')
'''
public static void main(String[] args){
'''
tim = Creature('Tim', 10, 3, 3)
if (combatOneOnOne(tim)):
    combatVictory() #since you win just keep on truckin
else:
    gameOver()# you lost, well. The game should end somehow.

jeff = Creature('Jeff', 10, 2, 2)
alan = Creature('Alan', 10, 3, 1)
if (combatOneOnTwo(jeff, alan)):
    combatVictory() #since you win just keep on truckin
else:
    gameOver()# you lost, well. The game should end somehow.
    
bob = Creature('Robert', 10, 2, 2)
clide = Creature('Clide', 10, 3, 2)
doug = Creature('Doug', 10, 3, 3)
if (combatOneOnThree(bob, clide, doug)):
    combatVictory() #since you win just keep on truckin
else:
    gameOver()# you lost, well. The game should end somehow.
