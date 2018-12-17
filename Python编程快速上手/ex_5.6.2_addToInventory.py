"""
Create By: O.C.
Date: 2018/12/11

This is a test program.
ex_5.6.2_addToInventory.py

"""


def addToInventory(inventory, addedItems):
    inv = inventory
    for i in addedItems:
        if i in inv.keys():
            inv[i] += 1
        else:
            inv.setdefault(i, 1)
    return inv


def displayInventory(items):
    print('Inventory:')
    total = 0
    for k, v in items.items():
        print((str(v).ljust(5)) + ' ' + k)
        total = total + v
    print('Total number of items: ' + str(total).rjust(5))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
