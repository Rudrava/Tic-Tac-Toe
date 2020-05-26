import pygame
import main
import pixelData



#initialize pygame
pygame.init()

#create screen
x=400
y=400
screen = pygame.display.set_mode((x,y))

running = True

#title and logo
'''
as we arr changing the attr of the dispay so we need to access the display meethod
of pygame then it has functions for generally all the display attr
'''
pygame.display.set_caption('TIC TAC TOE')       #this sets the heading title of the screen

#icon
'''
to set an icon we again have to set the set_icon method to a png file
which has to be loaded by using pygame's image method

in which image is to be loaded as
pygame.image.load("path or file name if in same dir")
'''

icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)


'''
as if we run the above code it gets terminated after sometime and also no buttons work
like the X button minimize button and stuff

these all buttons are handled by pygame.event.get() it is a list
so we can itterate over it and just check for inputs and pygame has inbuilt EVENT TYPES for detection
of each events
like QUIT for the x or quit button

THE GENERAL SYNTAX

for event in pygame.event.get():
    if event.type == <event type>:
        <action>

also NOTE:-
    all the systems that are gonna have to updated or displayed continously
    are to be defined or called within this while loop
    like

    background colour

    which is needed to be set using pygames screen method

    syntax:-
    screen.fill((r,g,b))

    NOW HEADS UP

    THAT WHILE THESE PROCESSES ARE RUNNING THE METHODS
    WHICH AFFECT DISPLAY HAVE TO BE UPDATED EXPLICITLY
    ELSE WHICH IT WONT SHOW UP IIN THE DISPLAY WINDOW

    TO DO THAT WE NEED TO CALL THE UPDATE METHOD IN DISPLAY
    INSIDE THE GAME LOOP


'''
#grid
grid = pixelData.Grid(x, y, screen)

circle = pixelData.Circle(x, y, screen)

cross = pixelData.Cross(x, y, screen)


#draw on board
def drawCross(x1,x2,y1,y2):
    pygame.draw.line(screen,(100,25,255),(x1,y1),(x2,y2),5)
    pygame.draw.line(screen,(100,25,255),(x2,y1),(x1,y2),5)

keys=[]
def playerInputX(cube):
    crossCoorrdinates[cube][1]=True
    board[cube - 1]='X'
    print(board)
    main.display(board)


def playerInputO(cube):
    circleCoordinates[cube][1]=True
    board[cube-1]='O'
    print(board)
    main.display(board)



def markAt(symbol):
        if keys[pygame.K_KP1] or keys [pygame.K_1] :
            cube = 1
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 2
        if keys [pygame.K_KP2] or keys [pygame.K_2]:
            cube = 2
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 3
        if keys [pygame.K_KP3] or keys [pygame.K_3]:
            cube = 3
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        #4
        if keys [pygame.K_KP4] or keys [pygame.K_4]:
            cube = 4
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 5
        if keys [pygame.K_KP5] or keys [pygame.K_5]:
            cube = 5
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 6
        if keys [pygame.K_KP6] or keys [pygame.K_6]:
            cube = 6
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 7
        if keys [pygame.K_KP7] or keys [pygame.K_7]:
            cube = 7
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')

        # 8
        if keys [pygame.K_KP8] or keys [pygame.K_8]:
            cube = 8
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube)
                if symbol == 'O':
                    playerInputO(cube)
            else:
                print('invalid input')


        # 9
        if keys [pygame.K_KP9] or keys [pygame.K_9]:
            cube = 9
            if board[cube-1] == ' ':
                if symbol == 'X':
                    playerInputX(cube,turns)
                if symbol == 'O':
                    playerInputO(cube,turns)
            else:
                print('invalid input')


while running:             #this function to hold the screen or GENERAL GAME LOOP until quit pressed
    pygame.time.delay(100)
    screen.fill((255,50,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if turns <= 9:
        #     if event.type == pygame.KEYDOWN:
        #         keys = pygame.key.get_pressed()
        #         print(board)
        #         print('--',turns)
        #         if turns % 2:
        #             markAt(s[0])
        #             turns += 1
        #             continue
        #         else:
        #             markAt(s[1])
        #             turns += 1
        #             continue
        # else:
            # print('Turns Ended')
            # exit()
    circle.update(3)
    circle.draw()

    cross.update(4)
    cross.draw()



    grid.draw()

    pygame.display.update()








