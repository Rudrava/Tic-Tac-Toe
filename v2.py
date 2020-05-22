import ai
board =[' ']*9

symbols=['X','O']

p1Name = 'rudrava'
p2Name = 'ryan'

players=[{symbols[0]:p1Name},{symbols[1]:p2Name}]


def display():
    # print_header()
    print()          #displays
    print('     |     |')
    print('  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2])
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8])
    print('     |     |')
    return


def win():
    '''
    for rows i check chunk of 3 consecutive elements are equal or not

        try
        for i in range(0,9,3):
            for j in range(i,i+3):
                print(j,end=" ")
            print()

    for columns i check if the consecutive column elements are equal or not and the methd
    used is just a simple deivised algo try this :
    for i in range(0,3):
        for j in range (i,9,3):
                print(j,end=" ")
        print()

    for diagonals also similar logic like the one used for columns is used

    try this
        for i in [0,2]:
            for j in range(i,9-i,4-i):
                 print(j,end=" ")
         print()

        '''
    for symbol in symbols:
        for i in range(0,9,3):
            count = 0
            for j in range (i,i+3):
                if board[j]==symbol:
                    count+=1
            if count==3:
                # print('\nTrue through Row')
                return symbol

        for i in range(0,3):
            count = 0
            for j in range (i,9,3):
                if board[j]==symbol:
                    count+=1
            if count==3:
                # print('\nTrue through COlumn')
                return symbol

        for i in [0,2]:
            count = 0
            for j in range(i,9-i,4-i):
                if board[j]==symbol:
                    count+=1
            if count==3:
                # print('\nTrue through Diagonal')
                return symbol
    return False


def player(turn):
    if turn % 2 == 0:   return (symbols[0],players[0][symbols[0]])
    return (symbols[1],players[1][symbols[1]])


def isAvailable(position):
    if position in range(0,9):
        if board[position] == ' ':
            return True
    print('Invalid Input')
    return False


def play():
    for turn in range(0,9):
        if not win():
            symbol,playerName = player(turn)
            while True:
                position = int(input(f"{playerName}'s turn: "))-1
                if isAvailable(position):
                    board[position]=symbol
                    display()
                    break
        else:
            print(f'{playerName} wins')
            exit()

if __name__=='__main__':
    play()
