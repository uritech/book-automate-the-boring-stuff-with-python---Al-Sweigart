def a():
    print('a() Starts')
    b()
    d()
    print('a() return')
def b():
    print('b() Starts')
    c()
    print('b() returns')
def c():
    print('c() Starts')
    print('c() returns')
def d():
    print('d() Starts')
    print('d() returns')
a()