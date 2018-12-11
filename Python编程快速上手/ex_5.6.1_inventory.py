stuff = {
    'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12
}


def displayInventory(items):
    print('Inventory:')
    total = 0
    for k, v in items.items():
        print(str(v) + ' ' + k)
        total = total + v
    print('Total number of items: ' + str(total))


displayInventory(stuff)
