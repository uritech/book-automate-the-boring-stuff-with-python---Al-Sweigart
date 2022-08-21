"""This is a multiline comment
and  will be ignore by python"""

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

#If we use the f letter before anystring, we will be able to put variable content inside the string
name = 'Macintosh'
age = 4000
print(f'I am {name} and my age is {age}')

#Also we can use %s and at the end add in order the variable names

print('I am %s and my age is %s' %(name, age))