'''
Created on May 11, 2018

@author: Sam

An FUll version of Marvin, but with legacy in mind, real planning, a agile approach... everything 2.0
'''
from pip._vendor.distlib.compat import raw_input

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
            
def selectAction():
    playerChoice = raw_input(': ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'):
            return 1
        elif (playerChoice=='2'):
            return 2
        elif (playerChoice=='3'):
            return 3
        elif (playerChoice=='4'):
            return 4
        elif (playerChoice=='5'):
            return 5
        else:
            print('Controls: enter a valid number 1-5')   
        playerChoice = raw_input(': ')
               

class CombatStart:
    @classmethod
    def oneOnOne(cls, marv, creature1):
        print("Combat Start! Select action:")
        validChoice = False
        option = selectAction()
        # Action chosen. Now choose target. 
        while(validChoice == False):
            if(option==1):
                validChoice = True
                print("attack {}".format(creature1.name))
            elif(option==2):
                validChoice = True
                print("magic {}".format(creature1.name))
            elif(option==3):
                validChoice = True
                print("item {}".format(creature1.name))
            else:
                print("1 for attack, 2 for magic, 3 for items:")
                option = selectAction()
      
    @classmethod  
    def oneOnTwo(cls, marv, creature1, Creature2):
        print("Combat Start! Select action:")
        validChoice = False
        option = selectAction()
        # Action chosen. Now choose target. 
        while(validChoice == False):
            if(option==1):
                validChoice = True
                print("attack {}".format(creature1.name))
            elif(option==2):
                validChoice = True
                print("magic {}".format(creature1.name))
            elif(option==3):
                validChoice = True
                print("item {}".format(creature1.name))
            else:
                print("1 for attack, 2 for magic, 3 for items:")
                option = selectAction()
    

            
tim = Creature('Tim', 10, 3, 3)
jeff = Creature('Jeff', 10, 3, 3)
mark = Creature('Mark', 10, 3, 3)

marvin = Marvin('Marvin', 25, 5, 6)

introBattle = CombatStart.oneOnOne(marvin, mark)
rematch  = CombatStart.oneOnTwo(marvin, tim, jeff)
# marvin.attack(tim)
# tim.attack(marvin)