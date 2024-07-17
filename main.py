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

def Turning(keys, angle):
    Dif = 0.0
    Target = 0.0
    turn = False
    
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
        Dif = abs(Target - angle)
        if abs(Dif - 2*math.pi) <= 1E-7:
            Dif = 0
        if Dif > 1E-7:
            if angle < Target:
                if Dif <= math.pi:
                    angle += math.pi/800
                else:
                    angle -= math.pi/800
            else:
                if Dif < math.pi:
                    angle -= math.pi/800
                else:
                    angle += math.pi/800
        else:
            angle = Target
    
    while angle >= 2*math.pi:
        angle -= 2*math.pi
    while angle < 0:
        angle += 2*math.pi
    
    return angle

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