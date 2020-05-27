import pygame
import setUp

#setup
gridColour = setUp.gridColour
colorX = setUp.colorX
colorO = setUp.colorO
#end setup


class Grid():
    def __init__(self,x,y,screen):
        self.x, self.y, self.screen = x, y, screen

    #Grid data
    def draw(self):
        x, y, screen = self.x, self.y, self.screen
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

        pygame.draw.line(screen,gridColour,(verticalStart_X_1,verticalStart_Y_1),(verticalEnd_X_1,verticalEnd_Y_1),5)
        pygame.draw.line(screen,gridColour,(verticalStart_X_2,verticalStart_Y_2),(verticalEnd_X_2,verticalEnd_Y_2),5)

        pygame.draw.line(screen,gridColour,(horizontalStart_X_1,horizontalStart_Y_1),(horizontalEnd_X_1,horizontalEnd_Y_1),5)
        pygame.draw.line(screen,gridColour,(horizontalStart_X_2,horizontalStart_Y_2),(horizontalEnd_X_2,horizontalEnd_Y_2),5)


#circle center X,Y
class Circle():
    circleCoordinates = {}

    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.coOrd()


    def coOrd(self):
        x, y = self.x , self.y
        circle1X,circle3X,circle5X = x/6, 3*(x/6), 5*(x/6)
        circle1Y,circle3Y,circle5Y = y/6, 3*(y/6), 5*(y/6)

        Circle.circleCoordinates={
            # 1
            1 : [(circle1X,circle1Y),False],
            2 : [(circle3X,circle1Y),False],
            3 : [(circle5X,circle1Y),False],
            # 2
            4 : [(circle1X,circle3Y),False],
            5 : [(circle3X,circle3Y),False],
            6 : [(circle5X,circle3Y),False],
            # 3
            7 : [(circle1X,circle5Y),False],
            8 : [(circle3X,circle5Y),False],
            9 : [(circle5X,circle5Y),False]
            }


    def update(self,cube):
        self.coOrd()
        if not Circle.circleCoordinates[cube][1]:
            Circle.circleCoordinates[cube][1] = True
            # print(Circle.circleCoordinates)

    def draw(self):
        radius = int(((2 * (self.x/12)) - (self.x/12)))        #just a clac i came up with
        # print(Circle.circleCoordinates)
        screen = self.screen
        #DRAW cicle
        for i in (Circle.circleCoordinates):           #itterates over all circle coordinates
            if Circle.circleCoordinates[i][1]:                     #checks if circle draw to be drawn or not
                (x , y)=Circle.circleCoordinates[i][0]         #gets the coord
                pygame.draw.circle(screen,colorO,(int(x),int(y)),radius,5)


class Cross():
    crossCoordinates = {}

    def __init__(self, x, y,screen):
        self.x ,self.y ,self.screen = x, y, screen
        self.coOrd()

    def coOrd(self):
        x, y = self.x ,self.y
        #data
        row1X1, row1X2, row2X1, row2X2, row3X1, row3X2 = (x/12), 3 * (x/12), 5 * (x/12), 7 * (x/12), 9 * (x/12), 11 * (x/12)
        column1Y1, column1Y2, column2Y1, column2Y2, column3Y1, column3Y2 = (y/12), 3 * (y/12), 5 * (y/12), 7 * (y/12), 9 * (y/12), 11 *  (y/12)
        #per cross
        Cross.crossCoordinates={
            1:[(row1X1, row1X2, column1Y1, column1Y2),False],
            2:[(row2X1, row2X2, column1Y1, column1Y2),False],
            3:[(row3X1, row3X2, column1Y1, column1Y2),False],
            4:[(row1X1, row1X2, column2Y1, column2Y2),False],
            5:[(row2X1, row2X2, column2Y1, column2Y2),False],
            6:[(row3X1, row3X2, column2Y1, column2Y2),False],
            7:[(row1X1, row1X2, column3Y1, column3Y2),False],
            8:[(row2X1, row2X2, column3Y1, column3Y2),False],
            9:[(row3X1, row3X2, column3Y1, column3Y2),False]
        }


    def update(self,cube):
        self.coOrd()
        if not Cross.crossCoordinates[cube][1]:
            Cross.crossCoordinates[cube][1] = True


    #draw on board
    def draw(self):
        screen =self.screen
        for j in (Cross.crossCoordinates):
            if Cross.crossCoordinates[j][1]:
                x1,x2,y1,y2=Cross.crossCoordinates[j][0]
                pygame.draw.line(screen,colorO,(x1,y1),(x2,y2),5)
                pygame.draw.line(screen,colorO,(x2,y1),(x1,y2),5)
