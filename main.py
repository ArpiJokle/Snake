from cell import *
import pygame
import snake
from values import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

Snake = snake.Snake(WIDTH/2, HEIGHT/2, GREEN, SNAKE_DIST, SNAKE_R_MIN, SNAKE_R_MAX)
for i in range(SNAKE_LEN):
    Snake.AddCell()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Snake.RandomRadiuses()
            if event.key == pygame.K_SPACE:
                Snake.AddCell()
    
    #AXES
    window.fill((80, 80, 80))
    pygame.draw.line(window, BLACK, (0, HEIGHT/2), 
                     (WIDTH, HEIGHT / 2))
    pygame.draw.line(window, BLACK, (WIDTH/2, 0), 
                     (WIDTH/2, HEIGHT))
    
    keys = pygame.key.get_pressed()
    Snake.Turn(keys)
    Snake.Move(15)
    Snake.Render(window)
    
    pygame.display.flip()

pygame.quit()