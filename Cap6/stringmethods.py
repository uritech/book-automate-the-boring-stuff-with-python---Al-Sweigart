spam = 'Hello, world!'

#upper() method will change all the letters to uppercase, this method doesnot change the string itself
spam = spam.upper()
print (spam)

spam = spam.lower()
print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else : 
    print('I hope teh rest of your day is good!')

#isupper and islower methods will return True or False

print(spam.islower())
print(spam.isupper())

#startswith() and endswith() methods are useful alternatives to the == equals operator if you need
#to check only whether the first or last part of the string, rather than the whole thing is equal to another string.

print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))

#join() and split() methods
a = 'My name is Simon'
b = a.split()
print(b)
print(' '.join(b))

#strip(), lsrip() and rstrip() methods helps us to strip off whitespace characters(space, tab and newline)
#It will return a new string without any whitespace
spaceString = '        Hello world!         '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

#Passing strip() argument will tell it to strip occurrences from the end of the string stored. Argument order does not matter.

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam)
print(spam.strip('apmS'))