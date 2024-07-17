import pygame
from pygame import gfxdraw
import math

class Cell:
    # def __init__(self, x_, y_, r_ = 70, d_ = 90):
    #     self.x = x_
    #     self.y = y_
    #     self.radius = r_
    #     self.distance = d_
    #     self.angle = 0
    
    def __init__(self, *args):
        if len(args) == 1:
            Prev = args[0]
            self.x = Prev.x - Prev.distance
            self.y = Prev.y
            self.radius = Prev.radius
            self.distance = Prev.distance
            self.angle = 0
        else:
            self.x = args[0]
            self.y = args[1]
            self.radius = args[2]
            self.distance = args[3]
            self.angle = 0
    
    def drawHead(self, Screen, Color):
        
        #direction calculation
        Vector = (math.cos(self.angle), math.sin(self.angle))
        
        #DRAW RADIUS
        pygame.draw.circle(Screen, Color, (self.x, self.y), self.radius, 7)
        
        #DRAW DISTANCE RADIUS
        pygame.draw.circle(Screen, (240, 240, 240), (self.x, self.y), self.distance, 3)
        
        #DRAW CENTER
        pygame.draw.circle(Screen, (150, 140, 140), (self.x, self.y), 15)
        
        #direction
        pygame.draw.line(Screen, (0,140,140), (self.x, self.y),
                         ((self.x + self.distance * Vector[0],
                                                self.y + self.distance * Vector[1])), 3)
        
        self.x += Vector[0] / 5
        self.y += Vector[1] / 5
    
    def drawCell(self, Screen, Color, Coords):
        
        Vector = (Coords[0] - self.x, Coords[1] - self.y)
        Len = math.sqrt(Vector[0] ** 2 + Vector[1] ** 2)
        Vector = (Vector[0] / abs(Len), Vector[1] / abs(Len))
        
        #DRAW RADIUS
        pygame.draw.circle(Screen, Color, (self.x, self.y), self.radius, 7)
        
        #DRAW DISTANCE RADIUS
        pygame.draw.circle(Screen, (240, 240, 240), (self.x, self.y), self.distance, 3)
        
        #DRAW CENTER
        pygame.draw.circle(Screen, (150, 140, 140), (self.x, self.y), 15)
        
        #direction
        pygame.draw.line(Screen, (0,140,140), (self.x, self.y),
                         ((self.x + self.distance * Vector[0],
                                                self.y + self.distance * Vector[1])), 3)
    
    def MoveHead(self, velocity = 5):
        Vector = (math.cos(self.angle), math.sin(self.angle))
        self.x += Vector[0] * velocity / 25
        self.y += Vector[1] * velocity / 25
    
    def MoveCell(self, Coords):
        Vector = (Coords[0] - self.x, Coords[1] - self.y)
        Len = math.sqrt(Vector[0] ** 2 + Vector[1] ** 2)
        Vector = (- Vector[0] / Len, - Vector[1] / Len)
        self.x = Vector[0] * self.distance + Coords[0]
        self.y = Vector[1] * self.distance + Coords[1]