'''
classes: Tree, Gnome, Woodchuck, Garden
water gauge
chance of rain
chance of tree disappearing
each turn: rain or woodchuck

'''

import random

# Classes
class Tree:
    def __init__(self):
        self.chance = 15
        self.rain = 25

# class FruitTree(Tree):
#     def __init__(self):
#         super().__init__()
#         self.water_level = 0
#         self.fruit = 0

#     def harvest(self):
#         if self.water_level >= 100:
#             self.fruit += 1
#             self.water_level = 0
#             print('One of your fruit trees has produced fruit!')

class Woodchuck:
    def __init__(self):
        self.disappearingTreeChance = 5
  
class Gnome: 
    def __init__(self):
        self.rainChance = 5

class Hunt():
    def __init__(self):
        self.uses = 3

class Garden:
    def __init__(self):
        self.trees = []
        # self.fruitTrees = []
        self.woodchucks = []
        self.gnomes = []
        self.waterLevel = 300
        self.waterLoss = 20
        self.rainChance = 25
        self.woodchuckChance = 10
        self.disappearingTreeChance = 0
        # self.fruit = 0
        hunt = Hunt()
        self.uses = hunt.uses

# Functions        
    def addTree(self):
        # if self.chance() > 15:
            tree = Tree()
            self.trees.append(tree)
            print('A new tree has blossomed!')
        # else: 
        #     fruitTree = FruitTree()
        #     self.fruitTrees.append(fruitTree)
        #     print('A new fruit tree has blossomed!')
        
    def addGnome(self):
        gnome = Gnome()
        self.gnomes.append(gnome)
        self.rainChance += gnome.rainChance
        print('The garden has been blessed with a new gnome!')
        
    def addWoodchuck(self):
        woody = Woodchuck()
        self.woodchucks.append(woody)
        self.disappearingTreeChance += woody.disappearingTreeChance
        print('A pesky woodchuck has entered the garden!')

    def rain(self):
        self.waterLevel += 50
        print('It rained! Water levels increased.')
        i = 0

    def hunt(self):
        self.uses -= 1
        if self.uses >= 0 and len(self.woodchucks) > 0:
            print('The hound successfully hunted %d woodchucks.' % len(self.woodchucks))
            killCount = len(self.woodchucks)
            while killCount > 0:
                del self.woodchucks[0]
                killCount -= 1
    
    def chance(self) -> float:
        return random.random() * 100

    def growTree(self, isRaining: bool, waterLevel: int):
        tree = Tree()
        chance = self.chance()
        if chance < tree.chance or (isRaining == True and chance < tree.rain) or (waterLevel >= 200 and chance < tree.rain):
            self.addTree()

    def getStats(self):
        print('---------------------------------------------')
        print('Water Level: %d' % self.waterLevel)
        print('Trees: %d' % len(self.trees))
        # print('Fruit Trees: %d' % len(self.fruitTrees))
        # print('Fruit: %d' % self.fruit)
        print('Gnomes: %d' % len(self.gnomes))
        print('Woodchucks: %d' % len(self.woodchucks))
        print('Hunts Available: %d' % self.uses)

# Simulation loop
garden = Garden()
i = 1
newTree = 0
rainChance = garden.rainChance
while len(garden.trees) < 10 and garden.waterLevel > 0:
    print('---------------------------------------------')
    print('Round %d' % i)
    garden.getStats()
    
    while True:
        userIn = input("Select 'h' to hunt or 'c' to continue : ")
        if userIn == 'h':
            garden.hunt()
        elif userIn == 'c':
            break
        else:
            print("Sorry, didn't catch that.")
    print('\n')
    
    isRaining = False
    chance = garden.chance()
    if chance < rainChance:
        garden.rain()
        isRaining = True

    garden.growTree(isRaining, garden.waterLevel)
    
    # garden.fruit = 0
    # for instance in garden.fruitTrees:
    #     instance.harvest()
    #     garden.fruit += instance.fruit

    chance = garden.chance()
    if chance < garden.woodchuckChance:
        garden.addWoodchuck()

    if i % 10 == 0:
        chance = garden.chance()
        if chance < 50:
            garden.addTree()
        else:
            garden.addGnome()

    chance = garden.chance()
    if chance < garden.disappearingTreeChance and len(garden.trees) > 0 and len(garden.woodchucks) > 0:
        print('The woodchucks destroyed a tree!')
        del garden.trees[0]

    # chance = garden.chance()    
    # if chance < (garden.disappearingTreeChance - 5) and len(garden.fruitTrees) > 0 and len(garden.woodchucks) > 0:
    #     print('The woodchucks destroyed a fruit tree!')
    #     del garden.fruitTrees[0] 
    
    decrease = garden.waterLoss - (len(garden.trees) * 2)
    if isRaining == False:
        garden.waterLevel -= decrease
    i += 1

# Win and lose conditions
if len(garden.trees) >= 10:
    print('You have won!')
    garden.getStats()
elif garden.waterLevel <= 0:
    print('You have lost!')
    garden.waterLevel = 0
    garden.getStats()