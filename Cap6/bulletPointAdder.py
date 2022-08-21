#! python3
# bulletPointAdder.py - Adds Wikipedia bullet point to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range (len(lines)):
    lines[i] = f'* {lines[i]}'

text = '\n'.join(lines)

pyperclip.copy(text)
print(text)