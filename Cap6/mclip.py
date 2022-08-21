
#! python3
# mclip.py - A multi-clipboard program.

import sys, pyperclip

TEXT = {'agree' : """Yes, I agree. That sounds fine to me.""",
        'busy' : """Sorry, can we do this later this week or next week?""",
        'upsell' : """Would you consider making this a monthly donation?"""}

#The command line arguments will be stored in the variable sys.argv
#The first item in the sys.argv list should always be a string containing the program's file name.
#The second item should be the first command line argument.

if len(sys.argv) < 2:
    print('Usage: python3 mcli.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]         #first command line arg is the keyphrase

#This looks in the TEXT dictionary for the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}')