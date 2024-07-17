import pygame
import math

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