import random    

def CreateRandomBinaryBoard():
    l = []
    for i in range(8):
        l.append([])
        for j in range(8):
            num = random.randint(0,1)
            l[i].append(num)

    print('Random Binary Board:')
    for row in l:
        print(row)
    return l


def CurrentBoardState(board):
    l = [[] for _ in range(6)]
    for n in range(4):
        odd = 2*n + 1
        everyOtherTwo = n%2 + 2
        lastFour = n + 4
        for i in range(8):
            l[0].append(board[i][odd])
            l[1].append(board[i][everyOtherTwo])
            l[2].append(board[i][lastFour])
            l[3].append(board[odd][i])
            l[4].append(board[everyOtherTwo][i])
            l[5].append(board[lastFour][i])
    
    stateBin = ''
    for item in l:
        stateBin = str(sum(item) % 2) + stateBin

    print('Current State in Binary:',stateBin)
    return stateBin


def GetKeyBinaryLocation(keySquare=None):
    if keySquare is None:
        keySquare = random.randint(0,63)
    
    keyBin = f'{keySquare:06b}'

    print('Int key location:',keySquare)
    print('Binary key location:',keyBin)
    return keyBin


def GetFlipSquare(stateBin,keyBin):
    flipSquareBin = ''
    for i,j in zip(stateBin,keyBin):
        if i == j:
            flipSquareBin += '0'
        else:
            flipSquareBin += '1'

    return flipSquareBin


binaryBoard = CreateRandomBinaryBoard()

print('\n')

stateBin = CurrentBoardState(binaryBoard)

print('\n')

# You can pick the square for the key to be hidden in.
# Otherwise, the key location is random.
keyBin = GetKeyBinaryLocation(keySquare=None)

print('\n')

flipSquareBin = GetFlipSquare(stateBin,keyBin)
flipSquareInt = int(flipSquareBin,2)
print(f'Flip square {flipSquareBin} or {flipSquareInt}.')
