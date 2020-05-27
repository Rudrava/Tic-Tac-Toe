import pygame
import pixelData
import Input
import setUp

pygame.init()

screenWidth = setUp.screenWidth
screenHeight = setUp.screenHeight
backGround =  setUp.backGround

board = [' ']*9
symbols = ['X','O']

#Setup

screen = pygame.display.set_mode((screenWidth,screenHeight),pygame.RESIZABLE)
screen.fill(backGround)

pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

#end of Setup


#Draw variables
grid = pixelData.Grid(screenWidth, screenHeight, screen)
circle =  pixelData.Circle(screenWidth, screenHeight, screen)
cross =  pixelData.Cross(screenWidth, screenHeight, screen)

#end of declaration

#win mwthod
def winner():
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


def checkWin():
    pass
keyBoard = False
mouse = True


def InputMethod(cube,turn):
    flag = False
    if not circle.circleCoordinates[cube][1] and turn % 2 == 0 :
        if board[cube - 1] == ' ':
            board[cube - 1] = symbols[1]
            circle.update(cube)
            return True

    elif not cross.crossCoordinates[cube][1] and turn % 2:
        if board[cube - 1] == ' ':
            board[cube - 1] = symbols[0]
            cross.update(cube)
            return True
    else :
        print('Invalid Inp')
        return False


#   Run
def draw ():
    circle.draw()
    cross.draw()
    pygame.display.update()


def run():
    running = True
    turn = 0
    while running:
        pygame.display.update()
        pygame.time.delay(100)
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if turn <=  8:
                if event.type == pygame.KEYDOWN and keyBoard:
                    cube = Input.keyInput(event.key)

                    if cube != None:
                        if InputMethod(cube,turn):
                            turn += 1

                elif event.type == pygame.MOUSEBUTTONDOWN and mouse:
                    posX ,posY = pygame.mouse.get_pos()
                    cube = Input.mouseInput(posX ,posY)

                    if cube != None:
                        if InputMethod(cube,turn):
                            turn += 1

            else:
                draw()
                print('Turns Ended')
                pygame.time.delay(100)
                exit()

            draw()
            didWin = winner()
            if didWin:
                print(didWin,' won the game')
                pygame.time.delay(1000)
                exit()



run()
