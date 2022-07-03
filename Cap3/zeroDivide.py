def spam (divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Estas dividiendo por 0 y eso nos se puede!!!!')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))