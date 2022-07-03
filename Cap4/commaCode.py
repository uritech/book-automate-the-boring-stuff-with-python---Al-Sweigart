spam = ['cat', 'banana', 'apple', 'dog']

def editList (listEdit):
    cadena = ''
    tamañoLista = len(listEdit)
    if tamañoLista != 0 and tamañoLista > 1:
        for index, item in enumerate(listEdit):
            if index != (tamañoLista - 1):
                cadena += item + ', '
            else:
                cadena += 'and ' + item + '.'
    elif tamañoLista == 1:
        cadena = listEdit[0] + '.'

    else:
        cadena = 'La lista está vacía'
    return cadena
    
print(editList(spam))