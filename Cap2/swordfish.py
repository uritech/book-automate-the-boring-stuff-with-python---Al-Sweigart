#! /bin/python3
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe! What is our password?')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')