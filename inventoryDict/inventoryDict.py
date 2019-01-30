# print inventory from dictionary 
from copy import deepcopy


def displayInventory(dict):
    count=0
    #turn dict into list of tuples pairs
    for item,amnt in stuff.items():
        amount=stuff.get(item)
        count+=amount
        print(str(amount) + ' ' + item)
    print("Total number of items = " + str(count))

#displayInventory(stuff)

#PART2
#update inventory from List to Dictionary 
#use dragonloot to update stuff dictionary

def addtoInventory(stff, dragonlt):
    
    for items, amount in copyStuff.items():       #convert to list tuple pairs
        for loot in dragonlt:               
            if loot in items:
                stuff[loot] += 1                  #update original dict
            else:
                stuff.setdefault(loot,1)          #if item not in dict, add it

#given DICT
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

copyStuff=deepcopy(stuff)       #use deep copy to avoid loop errors for original dict

#acquired loot LIST
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv=addtoInventory(stuff,dragonLoot)
displayInventory(inv)
    