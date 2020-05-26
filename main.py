
board =[' ']*9

s=['X','O']

p1='X'
p2='O'

p1name='Rudra'     #player name
p2name='Ryan'

players={
    p1:p1name,
    p2:p2name
}


def get_name():
    p1name=input("PLAYER 1 INPUT NAME \n>>>")
    print("HI "+p1name)
    p2name=input("PLAYER 2 INPUT NAME \n>>>")
    print("HI "+p2name)
    pl1=input(p1name+" Choose your symbol [X/O]\n>>>")
    while pl1 not in s:             #checks valid symbol choice
        pl1=input("INVALID INPUT \n CHOOSE BETWEEN[X/O]")
        pl1=pl1.upper()
    if pl1=='X':        #obviosly the opp choice is for p2
        pl2='O'
    else:
        pl2='X'
    print(p1name+" You choose "+pl1+'\nAnd\n'+p2name+" You choose "+pl2+" \nNOW LETS PLAY") #agaaghz


def display(board):
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


def win(symbol):
    for i in range(0,9,3):
        count = 0
        for j in range (i,i+3):
            if board[j]==symbol:
                count+=1
        if count==3:
            # print('\nTrue through Row')
            return True

    for i in range(0,3):
        count = 0
        for j in range (i,9,3):
            if board[j]==symbol:
                count+=1
        if count==3:
            # print('\nTrue through COlumn')
            return True

    for i in [0,2]:
        count = 0
        for j in range(i,9-i,4-i):
            if board[j]==symbol:
                count+=1
        if count==3:
            # print('\nTrue through Diagonal')
            return True
    return False


def Input(symbol):
    while True:
        print(f'{players[symbol]}\'s turn: ')
        choice=int(input())
        if choice in range(0,9) and board[choice] == " ":
            board[choice]=symbol
            print(board)
            display()
            if win(symbol) == True:
                print(players[symbol],' Wins')
                exit()
            break
        else:
            print('INVALID INPUT')


def play():
    for i in range(0,9):
        if i % 2 == 0:
            playerInput(p1)
        else:
            playerInput(p2)
    print('TIE!!!')
    return


def main():

    play()

if __name__ == "__main__":
    main()
