# You are creating a fantasy video game.
# The data structure to model the player´s inventory will be a dictionary 
# where the keys are string values describing the item in the inventory 
# and the value is an integer value detailing how many of that item the player has.
# For example, the dictionary value {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.sortedWirte function named displayInventory()
# that would take any possible "inventory" and display it.

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}

def displayInventory(inventory):
    print ("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' - ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addItems):
    for i in addItems:
        #If item is not at the inventory dictionary, new key will be added with the default value 0.
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)