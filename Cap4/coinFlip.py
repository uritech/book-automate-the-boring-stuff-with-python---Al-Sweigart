import random

numberOfStreaks = 0
cadena = []
tails = 0
heads = 0

for experimentNumber in range(10000):
    for i in range(100):
        res = random.randint(0,1)
        if res == 1:
            cadena.append('H')
            heads += 1
            tails = 0
        else:
            cadena.append('T')
            tails += 1
            heads = 0

        if tails == 6 or heads == 6:
             numberOfStreaks += 1
             tails == 0
             heads == 0

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
print(numberOfStreaks)