import pygame
import numpy as np

pygame.init()
screan = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True
turn = 0
font = pygame.font.Font('freesansbold.ttf', 18)

game = True

board = np.zeros((3,3))




while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
            


    screan.fill("cyan")


    
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()