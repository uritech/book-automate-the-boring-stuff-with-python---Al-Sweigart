from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'modificado por spam'
eggs = 'global'
print(eggs)
spam()
print(eggs)