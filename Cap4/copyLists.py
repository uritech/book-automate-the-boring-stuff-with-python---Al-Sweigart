import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese))

cheese[1] = 42

print('----------------')

print(spam)
print(cheese)
print('----------------')

spam = copy.deepcopy(cheese)

print(spam)
print(cheese)

print('----------------')
print(id(spam))
print(id(cheese))