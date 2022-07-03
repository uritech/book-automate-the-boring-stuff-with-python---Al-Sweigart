import random, sys

print('ROCK, PAPER, SCISSORS')

#These variables keep track of the losses, wins and ties
wins = 0
losses = 0
ties = 0

while True:
    print ('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    #First check its a valid option
    while True:
        print ('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'p' or playerMove == 'r' or playerMove == 's':
            break
        print('Type one of r, p, s or q.')

    #Display what the player chose:
    if playerMove == 'p':
        print('Paper versus ... ')
    elif playerMove == 's':
        print('Scissors versus ... ')
    elif playerMove == 'r':
        print('Rock versus ... ')

    #Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 2:
        computerMove = 's'
        print('SCISSORS')
    elif randomNumber == 3:
        computerMove = 'r'
        print('ROCK')

    #Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You loose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You loose!')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You loose!')
        losses = losses + 1