from cell import *
import pygame
from functions import *
import keyboard

pygame.init()
WIDTH = 1200
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 138, 0)

Snake = [Cell(WIDTH/2, HEIGHT/2, 20, 60)]
for _ in range(16):
    Snake.append(Cell(Snake[_]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #AXES
    window.fill((80, 80, 80))
    pygame.draw.line(window, BLACK, (0, HEIGHT/2), 
                     (WIDTH, HEIGHT / 2))
    pygame.draw.line(window, BLACK, (WIDTH/2, 0), 
                     (WIDTH/2, HEIGHT))
    
    keys = pygame.key.get_pressed()
    Snake[0].angle = Turning(keys, Snake[0].angle)
    
    #Moving
    Snake[0].MoveHead(8)
    for i in range(1, len(Snake)):
        Snake[i].MoveCell((Snake[i-1].x, Snake[i-1].y))
    
    Snake[0].drawHead(window, (70, 70, 70))
    for i in range(1, len(Snake)):
        Snake[i].drawCell(window, (10, 70, 80), (Snake[i-1].x, Snake[i-1].y))
    
    pygame.display.flip()

pygame.quit()