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
        self.jazz = jazz # magic
        
    def __repr__(self):
        return " Name: {}\n Albums: {}\n Damage: {}".format(self.name, self.albums, self.damage)

    def __str__(self):
        return " Name: {}\n Albums: {}\n Damage: {}".format(self.name, self.albums, self.damage)

    def attack(self, creature):
        if(self.albums<=0):
            pass
        else:
            print('{} attacks {} for {}.'.format(self.name, creature.name, self.damage))
            creature.albums-=self.damage
        
class Marvin(Creature):
    'the man himself'
    
    def attack(self, creature):
        if(self.albums<=0):
            pass
        else:
            print('{} attacks {} for {}.'.format(self.name, creature.name, self.damage))
            creature.albums-=self.damage
        
    def heal(self):
        self.albums+=self.jazz
        if (self.maxHealth<self.albums):
            print('You heal for {}.'.format(self.maxHealth-(self.albums-self.jazz)))
            self.albums = self.maxHealth
        else:
            print('You heal for {}.'.format(self.jazz))
            
class Item:
    'Base class for all items'
    
    def __init__(self, name, value, health, flavor):
        self.name = name
        self.value = value
        self.health = health #Healing or damage amount
        self.description = flavor # flavor text
        
    def __repr__(self):    
        return '{}'.format(self.name)
        
    def __str__(self):
        if(self.description==0):
            return " '{}'\n Value: {}\n".format(self.name, self.value)
        else:
            return " '{}'\n Value: {}\n '{}'".format(self.name, self.value, self.description)
    
    def use(self):
        pass
            
class Potion(Item):
    'Healing and other restorative potions.'
    
    def use(self, targetCreature):
        print("{} heals {} for {}.".format(self.name, targetCreature.name, self.health))
        targetCreature.albums+=self.health
        
class Poison(Item):
    'Deals damage to target.'
    
    def use(self, targetCreature):
        print("{} poisons {} for {}.".format(self.name, targetCreature.name, self.health))
        targetCreature.albums-=self.health
        
# Read user input for the whole game.
# TODO: Possible efficiency issues. Try removing. 
def selectAction():
    playerChoice = raw_input(': ')
    while True: 
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
            
# Player's inventory
inventory = []

# Selects the item from inventory
def itemMenu():
    print(inventory)
    item = selectAction()
    return inventory[item-1]

# uses item on creature
def itemAction(itemSelection, targetCreature):
    itemSelection.use(targetCreature)
    inventory.remove(itemSelection)

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
        print("\n !!!!!!! Combat Start !!!!!!!")
        while(creature1.albums>0):
            menuSelection = combatMenu()
            
            if(menuSelection==1): #attack
                print("Select target to attack:\n'1' for {}".format(creature1.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #attack creature1
                    marv.attack(creature1)
                    creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==2): #magic
                print("Select target to heal:\n'1' for {}".format(marv.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #heal marv
                    marv.heal()
                    creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==3): #item
                itemSelection = itemMenu()
                print("Select target to use [{}] on:\n'1' for {}, '2' for {}".format(itemSelection.name, marv.name, creature1.name))
                targetSelection = twoTarget()
                if(targetSelection==1): #item marv
                    itemAction(itemSelection, marv)
                    creature1.attack(marv)
                elif(targetSelection==2): #item creature1
                    itemAction(itemSelection, creature1)
                    creature1.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
    #handles two on one combat encounters.          
    @classmethod  
    def oneOnTwo(cls, marv, creature1, creature2):
        print("\n !!!!!!! Combat Start !!!!!!!")
        while((creature1.albums>0) | (creature2.albums>0)):
            menuSelection = combatMenu()
            
            if(menuSelection==1): #attack
                print("Select target to attack:\n'1' for {}, 2 for {}".format(creature1.name, creature2.name))
                targetSelection = twoTarget()
                if((targetSelection==1) & (creature1.albums>=0)): #attack creature1
                    marv.attack(creature1)
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif((targetSelection==2) & (creature2.albums>=0)): #attack creature2
                    marv.attack(creature2)
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                else:
                    print("target already down")
                
            elif(menuSelection==2): #magic
                print("Select target to heal:\n'1' for {}".format(marv.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #heal marv
                    marv.heal()                    
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==3): #item
                itemSelection = itemMenu()
                print("Select target to use item on:\n'1' for {}, '2' for {}, 3 for {}".format(marv.name, creature1.name, creature2.name))
                targetSelection = threeTarget()
                if(targetSelection==1): #item marv
                    itemAction(itemSelection, marv)
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif((targetSelection==2) & (creature1.albums>=0)): #item creature1
                    itemAction(itemSelection, creature1)
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif((targetSelection==3) & (creature2.albums>=0)): #item creature2
                    itemAction(itemSelection, creature2)
                    creature1.attack(marv)
                    creature2.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                else:
                    print("target already down")
                
    #handles three on one combat encounters.          
    @classmethod  
    def oneOnThree(cls, marv, creature1, creature2, creature3):
        print("\n !!!!!!! Combat Start !!!!!!!")
        while((creature1.albums>0) | (creature2.albums>0) | (creature3.albums>0)):
            menuSelection = combatMenu()
            
            if(menuSelection==1): #attack
                print("Select target to attack:\n'1' for {}, 2 for {}, 3 for {}".format(creature1.name, creature2.name, creature3.name))
                targetSelection = twoTarget()
                if((targetSelection==1) & (creature1.albums>=0)): #attack creature1
                    marv.attack(creature1)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif((targetSelection==2) & (creature2.albums>=0)): #attack creature2
                    marv.attack(creature2)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif((targetSelection==3) & (creature3.albums>=0)): #attack creature2
                    marv.attack(creature3)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                else:
                    print("target already down")
                
            elif(menuSelection==2): #magic
                print("Select target to heal:\n'1' for {}".format(marv.name))
                targetSelection = oneTarget()
                if(targetSelection==1): #heal marv
                    marv.heal()                    
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                
            elif(menuSelection==3): #item
                itemSelection = itemMenu()
                print("Select target to use item on:\n'1' for {}, '2' for {}, 3 for {}".format(marv.name, creature1.name, creature2.name))
                targetSelection = threeTarget()
                if(targetSelection==1): #item marv
                    itemAction(itemSelection, marv)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif((targetSelection==2) & (creature1.albums>=0)): #item creature1
                    itemAction(itemSelection, creature1)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif((targetSelection==3) & (creature2.albums>=0)): #item creature2
                    itemAction(itemSelection, creature2)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif((targetSelection==4) & (creature3.albums>=0)): #item creature3
                    itemAction(itemSelection, creature3)
                    creature1.attack(marv)
                    creature2.attack(marv)
                    creature3.attack(marv)
                elif(targetSelection==5): #return to combat menu
                    pass
                else:
                    print("target already down")

'''
dumb testing stuff goes here
'''
minorHealthPotion = Potion("Minor Health Potion", 1, 10, 0)
medHealthPotion = Potion("Medium Health Potion", 1, 20, 'heals more')
majorHealthPotion = Potion("Major Health Potion", 1, 999, 'heals full')
minorPoison = Poison("Minor Poison", 1, 10, 0)

inventory.append(minorHealthPotion)
inventory.append(medHealthPotion)
inventory.append(majorHealthPotion)
inventory.append(minorPoison)

marvin = Marvin('Marvin', 25, 5, 6)

tim = Creature('Tim', 10, 3, 3)

jeff = Creature('Jeff', 10, 2, 3)
mark = Creature('Mark', 10, 2, 3)

mooka = Creature('Guard A', 5, 1, 3)
mookb = Creature('Guard B', 5, 1, 3)
boss = Creature('Big Boss', 20, 10, 6)

introBattle = CombatStart.oneOnOne(marvin, mark)
# TODO: Add a victory thing here when combat exits. 

rematch  = CombatStart.oneOnTwo(marvin, tim, jeff)
# TODO: Add a victory thing here when combat exits. 

finalBoss  = CombatStart.oneOnTwo(mooka, mookb, boss)
# TODO: Add a victory thing here when combat exits. 