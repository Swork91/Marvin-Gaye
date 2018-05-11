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
    playerChoice = raw_input('\n\nCombat Start! Select action (1 attack, 2 magic, 3 item): ')
    while (playerChoice != '0'): 
        if (playerChoice=='1'): # attack
            print("attack chosen")
            return 1
        elif (playerChoice=='2'): # magic
            print("magic chosen")
            return 2
        elif (playerChoice=='3'): # item
            print("item chosen")
            return 3
        else:
            print('error')   
        playerChoice = raw_input('\nSelect action: ')
               
class CombatStart:
    @classmethod
    def oneOnOne(cls, marv, creature1):
        print("test 1v1")
        option = selectAction()
        # Action chosen. Now choose target. 
        if(option==1):
            print("attack {}".format(creature1.name))
        elif(option==2):
            print("magic {}".format(creature1.name))
        elif(option==3):
            print("item {}".format(creature1.name))
      
    @classmethod  
    def oneOnTwo(cls, marv, creature1, Creature2):
        print('test 1v2')
    

            
tim = Creature('Tim', 10, 3, 3)
jeff = Creature('Jeff', 10, 3, 3)
mark = Creature('Mark', 10, 3, 3)

marvin = Marvin('Marvin', 25, 5, 6)

introBattle = CombatStart.oneOnOne(marvin, mark)
rematch  = CombatStart.oneOnTwo(marvin, tim, jeff)
# marvin.attack(tim)
# tim.attack(marvin)