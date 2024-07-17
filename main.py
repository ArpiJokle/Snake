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

A = Cell(WIDTH/2, HEIGHT/2)

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
    A.angle = Turning(keys, A.angle)
    A.drawHead(window, (70, 70, 70))
    
    pygame.display.flip()

pygame.quit()