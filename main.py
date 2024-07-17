from cell import *
import pygame
from functions import *
import random

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

Snake = [Cell(WIDTH/2, HEIGHT/2, 20, 20)]
for _ in range(16):
    Snake.append(Cell(Snake[_]))
    Snake[_ + 1].radius = random.randint(15, 30)
Snake[len(Snake) - 1].radius = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Snake = RandomSnake(Snake)
    
    #AXES
    window.fill((80, 80, 80))
    pygame.draw.line(window, BLACK, (0, HEIGHT/2), 
                     (WIDTH, HEIGHT / 2))
    pygame.draw.line(window, BLACK, (WIDTH/2, 0), 
                     (WIDTH/2, HEIGHT))
    
    keys = pygame.key.get_pressed()
    Snake[0].angle = Turning(keys, Snake[0].angle)
    
    #Moving
    Snake[0].MoveHead(25)
    for i in range(1, len(Snake)):
        Snake[i].MoveCell((Snake[i-1].x, Snake[i-1].y))
    
    SnakePoints = []
    SnakePoints = Snake[0].HeadPoints(SnakePoints)
    for i in range(1, 16):
        SnakePoints = Snake[i].CellPoints(SnakePoints)
    SnakePoints = Snake[len(Snake) - 1].TailPoints(SnakePoints)
    
    for i in range(0, len(SnakePoints)-1):
        pygame.draw.line(window, GREEN, SnakePoints[i], SnakePoints[i + 1], 5)
    pygame.draw.line(window, GREEN, SnakePoints[0], SnakePoints[len(SnakePoints) - 1], 5)
    
    pygame.display.flip()

pygame.quit()