from cell import *
import pygame
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
    Dif = 0.0
    Target = 0.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    turn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Target = 3 * math.pi / 2
        turn = True
    if keys[pygame.K_DOWN]:
        Target = math.pi / 2
        turn = True
    if keys[pygame.K_RIGHT]:
        Target = 2*math.pi
        turn = True
    if keys[pygame.K_LEFT]:
        Target = math.pi
        turn = True
    
    if turn:
        Dif = abs(Target - A.angle)
        if abs(Dif - 2*math.pi) <= 1E-7:
            Dif = 0
        if Dif > 1E-7:
            if A.angle < Target:
                if Dif <= math.pi:
                    A.angle += math.pi/800
                else:
                    A.angle -= math.pi/800
            else:
                if Dif < math.pi:
                    A.angle -= math.pi/800
                else:
                    A.angle += math.pi/800
        else:
            A.angle = Target
    
    while A.angle >= 2*math.pi:
        A.angle -= 2*math.pi
    while A.angle < 0:
        A.angle += 2*math.pi
    
    window.fill((80, 80, 80))
    
    A.drawHead(window, (70, 70, 70))
    
    pygame.draw.line(window, BLACK, (0, HEIGHT/2), 
                     (WIDTH, HEIGHT / 2))
    
    pygame.draw.line(window, BLACK, (WIDTH/2, 0), 
                     (WIDTH/2, HEIGHT))
    
    pygame.display.flip()

pygame.quit()