# import random
# def pVai(board):
#     choice = 5
#     if board[choice] == ' ' :
#         return choice
#     else:
#         while True:
#             choice = random.randint(0,8)
#             if board[choice] == ' ':
#                 return choice

# def minimax(board,depth,isMaximizing)
import  main


def pVai(board):
    bestScore = -20
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = 'X'
            ai = minimax(board,0,True)
            board[i] = ' '
            bestScore = max(ai,bestScore)
            bestMove = i
    return bestMove

score={
    'x':1,
    'O':-1,
}

def minimax(board,depth,isMaximizing):
    if isMaximizing:
        winner= main.win('X')
    else
        winner= main.win('O')
    # return 1
    if winner:
