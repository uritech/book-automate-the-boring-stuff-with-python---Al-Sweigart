#! python3
#English to Pig Latin
#Pig latin is a silly made-up language that alters English words.
#If a word begins with a vowel, the word yay is added to the end
#If a word begins with a consonant or consonant cluster, that consonant is moved to the end of the word followed by ay.

print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of words in Pig Latin
for word in message.split():
    #Separate the non.letters at the start of this word:
    prefixNonLetters = ''
    #Tests if the first character is not a letter
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()     #make the word lowercase for translation

    #Separate the constants at the start of this word:

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word [1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word +='yay'
    
    #Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add the non letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))

