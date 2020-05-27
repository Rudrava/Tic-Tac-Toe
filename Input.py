import pygame
import setUp

def keyInput(key):

    if key == pygame.K_KP1 or  key == pygame.K_1:
        return 1

    elif key == pygame.K_KP2 or  key == pygame.K_2:
        return 2

    elif key == pygame.K_KP3 or  key == pygame.K_3:
        return 3

    elif key == pygame.K_KP4 or  key == pygame.K_4:
        return 4

    elif key == pygame.K_KP5 or  key == pygame.K_5:
        return 5

    elif key == pygame.K_KP6 or  key == pygame.K_6:
        return 6

    elif key == pygame.K_KP7 or  key == pygame.K_7:
        return 7

    elif key == pygame.K_KP8 or  key == pygame.K_8:
        return 8

    elif key == pygame.K_KP9 or  key == pygame.K_9:
        return 9

    else :
        return None

x = setUp.screenWidth
y = setUp.screenHeight
relX = [x , (x/3) ,(2 * (x / 3))]
relY = [y , (y / 3) ,(2 * (y / 3))]

def mouseInput(posX , posY):
    if posX > 0 and posX < relX[1]:

        if posY > 0 and posY < relY[1]:
            print('1 ')
            return 1

        if posY > relY[1] and posY < relY[2]:
            print('4 ')
            return 4


        if posY > relY[2] and posY < relY[0]:
            print('7')
            return 7


    elif posX > relX[1] and posX < relX[2]:

        if posY > 0 and posY < relY[1]:
            print('2 ')
            return 2

        if posY > relY[1] and posY < relY[2]:
            print('5')
            return 5

        if posY > relY[2] and posY < relY[0]:
            print('8')
            return 8


    elif posX > relX[2] and posX < relX[0]:

        if posY > 0 and posY <relY[1]:
            print('3 ')
            return 3

        if posY > relY[1] and posY <relY[2]:
            print('6')
            return 6

        if posY > relY[2] and posY < relY[0]:
            print('9')
            return 9

    else:   return None

