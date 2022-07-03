import time, sys

indent = 0 #How many spaces to indent
indentIncreasing = True #Whether the identation is increasing or not.

try:
    while True:
        print (' ' * indent, end = '') #Multiplica el espacio por la variable indent
        print('********')
        time.sleep(0.1)#Pause 1 milisecond para dar un efecto visual mas difuso

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                #Change direction
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent = indent -1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    print('Bye!!!')
    sys.exit()