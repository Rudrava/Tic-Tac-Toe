import numpy as np
from os import system
import random
from time import sleep
import ai


board =[' ']*9


s=['X','O']

p1='X'
p2='O'


p1name='Rudra'     #player name
p2name=''
comp = True


def print_header():subl
    print(
    """
 _____  _  ____             _____  ____  ____              _____    ____      _____
/__ __\/ \/   _\           /__ __\/  _ \/   _\            /__ __\  /  _ \    /  __/
  / \  | ||  /     _____     / \  | / \||  /     _____      / \    | / \ |   |  \
  | |  | ||  \_    \____\    | |  | |-|||  \_    \____\     | |
  \_/  \_/\____/             \_/  \_/ \|\____/              \_/    \____/    \____\
""")



# def pVai():
#     choice = 5
#     if board[choice] == ' ' :
#         return choice
#     else:
#         while True:
#             choice = random.randint(0,8)
#             if board[choice] == ' ':
#                 return choice

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


def display(turn):
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
    for i in range(0,9,3):
        count = 0
        for j in range (i,i+3):
            if board[j]==symbol:
                count+=1
        if count==3:
            print('\nTrue through Row')
            return True

    for i in range(0,3):
        count = 0
        for j in range (i,9,3):
            if board[j]==symbol:
                count+=1
        if count==3:
            print('\nTrue through COlumn')
            return True

    for i in [0,2]:
        count = 0
        for j in range(i,9-i,4-i):
            if board[j]==symbol:
                count+=1
        if count==3:
            print('\nTrue through Diagonal')
            return True

    return False

def computer():
    return random.randint(0,9)


def play():
    display(-1)
    for i in range(0,9):
            if i % 2 == 0:
                while True:
                    print('player 1 turn: ')
                    choice=int(input())
                    if choice in range(0,9) and board[choice] == " ":
                        board[choice]=p1
                        display(i)
                        print(board)
                        if win(p1) == True:
                            print(p1name,' Wins')
                            exit()
                        break
                    else:
                        print('INVALID INPUT')
            else:
                if not comp:
                    while True:
                        print('player 2 turn: ')
                        choice=int(input())
                        if choice in range(0,9) and board[choice] == " " :
                            board[choice]=p2
                            display(i)
                            print(board)
                            if win(p2) == True:
                                print(p2name,' Wins')
                                exit()
                            break
                        else:
                            print('INVALID INPUT')
                else:
                    print('computer turn: ')
                    choice=ai.pVai(board)
                    board[choice]=p2
                    display(i)
                    print(board)
                    if win(p2) == True:
                        print(p2name,' Wins')
                        exit()
    print('TIE!!!')
    return

def main():

    play()

if __name__ == "__main__":
    main()
