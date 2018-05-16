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

# Read user input for the whole game.
# TODO: Possible efficiency issues. Try removing. 
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
            print('Controls>> Enter a valid number 1-5')   
        playerChoice = raw_input(': ')

# checks if user input is valid for the combat menu. 
def combatMenu():
    print("\nEnter 1 for attack, 2 for magic, 3 for items:")
    validChoice = False
    option = selectAction()
    while(validChoice == False):
        if(option==1):
            validChoice = True
            return 1
        elif(option==2):
            validChoice = True
            return 2
        elif(option==3):
            validChoice = True
            return 3
        else:
            print("Enter 1 for attack, 2 for magic, 3 for items:")
            option = selectAction()
def itemMenu():
    pass

# checks if user input is valid for targeting one creature. 
def oneTarget():
    validChoice = False
    target = selectAction()
    while(validChoice == False):
        if(target==1):
            validChoice = True
            return 1
        elif(target==5):
            validChoice = True
            return 5
        else:
            print("Enter 1 to select target, 5 to to return.")
            target = selectAction()

def twoTarget():
    validChoice = False
    target = selectAction()
    while(validChoice == False):
        if(target==1):
            validChoice = True
            return 1
        elif(target==2):
            validChoice = True
            return 2
        elif(target==5):
            validChoice = True
            return 5
        else:
            print("Enter 1-2 to select target, 5 to to return.")
            target = selectAction()

def threeTarget():
    validChoice = False
    target = selectAction()
    while(validChoice == False):
        if(target==1):
            validChoice = True
            return 1
        elif(target==2):
            validChoice = True
            return 2
        elif(target==3):
            validChoice = True
            return 3
        elif(target==5):
            validChoice = True
            return 5
        else:
            print("Enter 1-2 to select target, 5 to to return.")
            target = selectAction()
            
def fourTarget():
    validChoice = False
    target = selectAction()
    while(validChoice == False):
        if(target==1):
            validChoice = True
            return 1
        elif(target==2):
            validChoice = True
            return 2
        elif(target==3):
            validChoice = True
            return 3
        elif(target==4):
            validChoice = True
            return 4
        elif(target==5):
            validChoice = True
            return 5
        else:
            print("Enter 1-2 to select target, 5 to to return.")
            target = selectAction()

class CombatStart:
    #handles one on one combat encounters. 
    @classmethod
    def oneOnOne(cls, marv, creature1):
        CreatureOneDead = False
        print("\n !!!!!!! Combat Start !!!!!!!")
        while(CreatureOneDead==False):
            menuSelection = combatMenu()
            
            if(menuSelection==1): #attack
                print("Select target to attack:\n'1' for {}".format(creature1.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #attack creature1
                    marv.attack(creature1)
                    if(creature1.albums<=0):
                        CreatureOneDead=True
                        print("{} faints.".format(creature1.name))
                    else:
                        creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==2): #magic
                print("Select target to heal:\n'1' for {}".format(marv.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #heal marv
                    marv.heal()
                    if(creature1.albums<=0):
                        CreatureOneDead=True
                        print("{} faints.".format(creature1.name))
                    else:
                        creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==3): #item
                #TODO: Make an item class I guess. 
                itemSelection = itemMenu()
                print("Select target to use item on:\n'1' for {}, '2' for {}".format(marv.name, creature1.name))
                targetSelection = twoTarget()
                if(targetSelection==1): #item marv
                    print("used item on {}!".format(marv.name)) # TODO: replace me with itemMenu() stuff
                    if(creature1.albums<=0):
                        CreatureOneDead=True
                        print("{} faints.".format(creature1.name))
                    else:
                        creature1.attack(marv)
                elif(targetSelection==2): #item creature1
                    print("used item on {}!".format(creature1.name)) # TODO: replace me with itemMenu() stuff
                    if(creature1.albums<=0):
                        CreatureOneDead=True
                        print("{} faints.".format(creature1.name))
                    else:
                        creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
    #handles two on one combat encounters.          
    @classmethod  
    def oneOnTwo(cls, marv, creature1, creature2):
        CreatureOneDead = False
        CreatureTwoDead = False
        print("\n !!!!!!! Combat Start !!!!!!!")
        while((CreatureOneDead==False) | (CreatureTwoDead==False)):
            menuSelection = combatMenu()
            if(menuSelection==1): #attack
                print("Select target to attack:\n'1' for {}, 2 for {}".format(creature1.name, creature2.name))
                targetSelection = twoTarget()
                if(targetSelection==1): #attack creature1
                    marv.attack(creature1)
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                if(targetSelection==2): #attack creature2
                    marv.attack(creature2)
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==2): #magic
                print("Select target to heal:\n'1' for {}".format(marv.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #heal marv
                    marv.heal()                    
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==3): #item
                #TODO: Make an item class I guess. 
                itemSelection = itemMenu()
                print("Select target to use item on:\n'1' for {}, '2' for {}, 3 for {}".format(marv.name, creature1.name, creature2.name))
                targetSelection = threeTarget()
                if(targetSelection==1): #item marv
                    print("used item on {}!".format(marv.name)) # TODO: replace me with itemMenu() stuff
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                elif(targetSelection==2): #item creature1
                    print("used item on {}!".format(creature1.name)) # TODO: replace me with itemMenu() stuff
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                elif(targetSelection==3): #item creature2
                    print("used item on {}!".format(creature2.name)) # TODO: replace me with itemMenu() stuff
                    if(CreatureOneDead==False):
                        if(creature1.albums<=0):
                            CreatureOneDead=True
                            print("{} faints.".format(creature1.name))
                        else:
                            creature1.attack(marv)
                    if(CreatureTwoDead==False):
                        if(creature2.albums<=0):
                            CreatureTwoDead=True
                            print("{} faints.".format(creature2.name))
                        else:
                            creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
    #handles three on one combat encounters.          
    @classmethod  
    def oneOnThree(cls, marv, creature1, creature2, creature3):
        pass
        #TODO: The whole method.
    
tim = Creature('Tim', 10, 3, 3)
jeff = Creature('Jeff', 10, 3, 3)
mark = Creature('Mark', 10, 3, 3)

marvin = Marvin('Marvin', 25, 5, 6)

introBattle = CombatStart.oneOnOne(marvin, mark)
# TODO: Add a victory thing here when combat exits. 

rematch  = CombatStart.oneOnTwo(marvin, tim, jeff)
# TODO: Add a victory thing here when combat exits. 

# marvin.attack(tim)
# tim.attack(marvin)