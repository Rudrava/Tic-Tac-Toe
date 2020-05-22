import pygame

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

def grid():
    #vertical line 1
    verticalStart_X_1,verticalStart_Y_1=(int(x/3),0)
    verticalEnd_X_1,verticalEnd_Y_1=(int(x/3),y)

    #vertical line 2
    verticalStart_X_2,verticalStart_Y_2=(int(2*(x/3)),0)
    verticalEnd_X_2,verticalEnd_Y_2= (int(2*(x/3)),y)

    #horizontal line 1
    horizontalStart_X_1,horizontalStart_Y_1=(0,int(y/3))
    horizontalEnd_X_1,horizontalEnd_Y_1=(x,int(y/3))

    #horizontal line 2
    horizontalStart_X_2,horizontalStart_Y_2=(0,int(2*(y/3)))
    horizontalEnd_X_2,horizontalEnd_Y_2=(x,int(2*(y/3)))

    pygame.draw.line(screen,(100,50,255),(verticalStart_X_1,verticalStart_Y_1),(verticalEnd_X_1,verticalEnd_Y_1),5)
    pygame.draw.line(screen,(100,50,255),(verticalStart_X_2,verticalStart_Y_2),(verticalEnd_X_2,verticalEnd_Y_2),5)

    pygame.draw.line(screen,(100,50,255),(horizontalStart_X_1,horizontalStart_Y_1),(horizontalEnd_X_1,horizontalEnd_Y_1),5)
    pygame.draw.line(screen,(100,50,255),(horizontalStart_X_2,horizontalStart_Y_2),(horizontalEnd_X_2,horizontalEnd_Y_2),5)


circle1X,circle3X,circle5X = x/6, 3*(x/6), 5*(x/6)
circle1Y,circle3Y,circle5Y = y/6, 3*(y/6), 5*(y/6)


circleCoordinates={
    #row 1
    1 : (circle1X,circle1Y),
    2 : (circle3X,circle1Y),
    3 : (circle5X,circle1Y),
    #row 2
    4 : (circle1X,circle3Y),
    5 : (circle3X,circle3Y),
    6 : (circle5X,circle3Y),
    #row 3
    7 : (circle1X,circle5Y),
    8 : (circle3X,circle5Y),
    9 : (circle5X,circle5Y)
}

def drawCircle(mouseX,mouseY):
    pygame.draw.circle(screen,(100,25,255),(int(mouseX),int(mouseY)),30,5)

row1X1, row1X2, row2X1, row2X2, row3X1, row3X2 = (x/12), 3 * (x/12), 5 * (x/12), 7 * (x/12), 9 * (x/12), 11 * (x/12)
column1Y1, column1Y2, column2Y1, column2Y2, column3Y1, column3Y2 = (y/12), 3 * (y/12), 5 * (y/12), 7 * (y/12), 9 * (y/12), 11 *  (y/12)


crossCoorrdinates={
    1:(row1X1, row1X2, column1Y1, column1Y2),
    2:(row2X1, row2X2, column1Y1, column1Y2),
    3:(row3X1, row3X2, column1Y1, column1Y2),
    #row 1
    4:(row1X1, row1X2, column2Y1, column2Y2),
    5:(row2X1, row2X2, column2Y1, column2Y2),
    6:(row3X1, row3X2, column2Y1, column2Y2),
    #row 2
    7:(row1X1, row1X2, column3Y1, column3Y2),
    8:(row2X1, row2X2, column3Y1, column3Y2),
    9:(row3X1, row3X2, column3Y1, column3Y2)

}
def drawCross(x1,x2,y1,y2):
    pygame.draw.line(screen,(100,25,255),(x1,y1),(x2,y2),5)
    pygame.draw.line(screen,(100,25,255),(x2,y1),(x1,y2),5)

while running:             #this function to hold the screen or GENERAL GAME LOOP until quit pressed
    screen.fill((255,50,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()==(1,0,0):
            print('Hey Mouse \n')
            mouseX,mouseY=pygame.mouse.get_pos()
            print(mouseX,mouseY)
            circleCoordinates.append((mouseX,mouseY))



    #DRAW cicle
    for i in (circleCoordinates):
        mouseX,mouseY=circleCoordinates[i]
        drawCircle(mouseX,mouseY)

    #DRAW cross
    for j in (crossCoorrdinates):
        x1,x2,y1,y2=crossCoorrdinates[j]
        drawCross((x1),int(x2),int(y1),int(y2))

    grid()
    pygame.display.update()
