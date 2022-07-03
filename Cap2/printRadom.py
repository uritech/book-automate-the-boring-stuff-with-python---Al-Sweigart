import random
from os import * 
#Importar un módulo con from, nos ayuda a no tener que poner el modulo como prefijo para llamar a uno de sus metodos
#Pero puede generar un código menos legible así que no es recomendable
system('clear')
for i in range(5):
    print(random.randint(1,100))