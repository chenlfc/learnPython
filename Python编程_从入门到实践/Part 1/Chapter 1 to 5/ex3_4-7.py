# create by o.c. 2018/7/19
def pt_names(n):
    print('-' * 40)
    for name in n:
        print("Invite " + name.title() + " to the party.")


names = ['jack', 'stven', 'lisa', 'tom']
pt_names(names)

can_not_name = 'tom'
names.remove(can_not_name)

print('-' * 40)
print(can_not_name.title() + " can't attend the party.")

names.append('mary')
pt_names(names)

print('-' * 40)
print("I found a bigger table for the party.")
names.insert(0, 'cheney')
names.insert(3, 'colin')
names.append('lance')
pt_names(names)

print('-' * 40)
print("Sorry everybody... Only two guests can be invited to the party. ")
while len(names) > 2:
    pop_name = names.pop()
    print("I'm sorry " + pop_name + " for this party.")
pt_names(names)
print("总共邀请了" + str(len(names)) + "位嘉宾.")
del names[0]
del names[0]
print(names)
