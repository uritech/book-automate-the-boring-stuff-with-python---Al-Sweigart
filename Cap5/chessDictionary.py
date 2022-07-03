#Write a function named isValidChessBoard() 
#that takes a dictionary argument and returns True of False 
#depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white king.
#Each player can only have at most 16 pieces, at most 8 pawns, 
#and all pieces must be on a valid space from '1a' to '8h'; that is, a piece cant be on space '9z'
#The piece names begin with either a 'w' or 'b' to represent white or black,
#followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chess board.

dictBoard = {'1h' : 'bking', '6c' : 'wqueen', '2g' : 'bbishop', '5h' : 'bqueen', '3e' : 'wking'}

#This will be the counter pieces for each color
piecesCounter = {'w' : {'king' : 0, 'queen' : 0, 'bishop' : 0, 'pawn' : 0, 'knight' : 0, 'rook' : 0},
        'b': {'king' : 0, 'queen' : 0, 'bishop' : 0, 'pawn' : 0, 'knight' : 0, 'rook' : 0}}

#A dictionary to compare with the number of pieces. it should be less or equal
validPieces = {'king' : 1, 'queen' : 1, 'bishop' : 2, 'pawn' : 8, 'knight' : 2, 'rook' : 2}

#Valid spaces at chess board
validSpaces = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
            '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
            '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
            '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
            '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
            '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
            '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
            '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']


def isValidChessBoard(board, counter):
    try:
        #Save the number of pieces and separate by color
        for k, v in board.items():
            if k not in validSpaces:
                print(k + ' Is not a valid space!!!')
                return False
            #v[1:] shows the piece and v[:1] shows the color.
            color = v[:1]
            piece = v[1:]
            counter[color][piece] += 1

        #Evaluates for valid number of pieces. No more than 1 king, 1 queen, 2 bishop, 2 knights, 2 rook, and 8 pawns per color.
        for key, val in counter.items():
            for k, v in val.items():
                if v > validPieces[k]:
                    print('More ' + k + ' than should be at the color ' + key + '!!!')
                    return False
    except:
        print('There was an error!!! Check your Chess Board!!!')
        return False

    return True

print(isValidChessBoard(dictBoard, piecesCounter))
