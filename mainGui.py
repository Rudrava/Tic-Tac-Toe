import pygame
import pixelData

pygame.init()

screenWidth = 400
screenHeight = 400
backGround = (255,50,100)


#setup

screen = pygame.display.set_mode((screenWidth,screenHeight))
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


#   Run

def run():
    running = True

    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        circle.draw()
        cross.draw()
        grid.draw()


        pygame.display.update()


run()
