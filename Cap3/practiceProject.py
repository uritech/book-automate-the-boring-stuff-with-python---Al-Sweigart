
while True:
    print('Ingrese un numero')
    try:
        numero = int(input())
        break
    except ValueError:
        print('Debes ingresar un numero')

def collatz(number):
    residuo = number % 2
    result = 0
    if residuo == 0:
        result = number // 2
    else:
        result = (3 * number) + 1
    print(result)
    return result

contador = collatz(numero)

while contador != 1:
    contador = collatz(contador)
