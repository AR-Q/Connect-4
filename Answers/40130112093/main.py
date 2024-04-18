import pygame
import numpy as np
from functions import *

pygame.init()
screan = pygame.display.set_mode((850,600))
clock = pygame.time.Clock()
running = True
turn = 0
font = pygame.font.Font('freesansbold.ttf', 18)

text_player1 = font.render('Player 1 is Red', True,"red","cyan")
textRect_player1 = text_player1.get_rect()
textRect_player1.center = (700,100)
text_player2 = font.render('Player 2 is Blue', True,"blue","cyan")
textRect_player2 = text_player2.get_rect()
textRect_player2.center = (700,150)

game = -1

board = np.zeros((5,5))

X = 0

while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and game != -1:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and game == -1:
            if select_row[X] >= 0:
                board[select_row[X]][X] = turn + 1
                game = endgame(board,turn +1)
                turn = (turn + 1) % 2
                print(board)
            

        
            


    screan.fill("cyan")

    pygame.draw.rect(screan, (0,0,0), pygame.Rect(50,50,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(150,50,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(250,50,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(350,50,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(450,50,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(50,150,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(150,150,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(250,150,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(350,150,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(450,150,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(50,250,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(150,250,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(250,250,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(350,250,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(450,250,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(50,350,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(150,350,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(250,350,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(350,350,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(450,350,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(50,450,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(150,450,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(250,450,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(350,450,100,100),1)
    pygame.draw.rect(screan, (0,0,0), pygame.Rect(450,450,100,100),1)
    
    
    screan.blit(text_player1, textRect_player1)
    screan.blit(text_player2, textRect_player2)
    text_turn = font.render(f'Turn : player {turn + 1}', True,"black","cyan")
    textRect_turn = text_turn.get_rect()
    textRect_turn.center = (700,200)
    screan.blit(text_turn, textRect_turn)


    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                pygame.draw.circle(screan, "red", configure_pos(j,i), 30)
            elif board[i][j] == 2:
                pygame.draw.circle(screan, "blue", configure_pos(j,i), 30)




    if game == -1:
        (x,y) = pygame.mouse.get_pos()

    
        if turn == 0:
            color = (255,133,133)
        else:
            color = (163, 209, 255)

        select_row = get_bottom_row(board)
        configure_selected_row = configure_row(select_row)

        if 50 < x < 150:
            pygame.draw.circle(screan, color, (100,configure_selected_row[0]), 30)
            X = 0
        elif 150 < x < 250:
            pygame.draw.circle(screan, color, (200,configure_selected_row[1]), 30)
            X = 1
        elif 250 < x < 350:
            pygame.draw.circle(screan, color, (300,configure_selected_row[2]), 30)
            X = 2
        elif 350 < x < 450:
            pygame.draw.circle(screan, color, (400,configure_selected_row[3]), 30)
            X = 3
        elif 450 < x < 550:
            pygame.draw.circle(screan, color, (500,configure_selected_row[4]), 30)
            X = 4
    else:
        text_winner = font.render(f'The WINNER is Player{game}', True,"yellow","cyan")
        textRect_winner = text_winner.get_rect()
        textRect_winner.center = (700,250)
        screan.blit(text_turn, textRect_turn)
    
    pygame.display.flip()

    clock.tick(60)





pygame.quit()
exit()