import pygame
import math

class Cell:
    def __init__(self, *args):
        if len(args) == 1:
            Prev = args[0]
            Vector = Prev.Direction
            Len = math.sqrt(Vector[0] ** 2 + Vector[1] ** 2)
            Vector = (Vector[0] / Len, Vector[1] / Len)
            self.x = Prev.x - Vector[0] * Prev.distance
            self.y = Prev.y - Vector[1] * Prev.distance
            self.radius = Prev.radius
            self.distance = Prev.distance
            self.angle = 0
            self.Direction = (1, 0)
        else:
            self.x = args[0]
            self.y = args[1]
            self.radius = args[2]
            self.distance = args[3]
            self.angle = 0
            self.Direction = (1, 0)
    
    def drawHead(self, Screen):
        Points = self.HeadPoints()
        pygame.draw.line(Screen, (255,20,147), Points[0],
                         (Points[0][0] + self.Direction[0] * 18,
                          Points[0][1] + self.Direction[1] * 18),
                         5)

    
    def MoveHead(self, velocity = 5):
        self.Direction = (math.cos(self.angle), math.sin(self.angle))
        self.x += self.Direction[0] * velocity / 25
        self.y += self.Direction[1] * velocity / 25
    
    def MoveCell(self, Coords):
        self.Direction = (Coords[0] - self.x, Coords[1] - self.y)
        Len = math.sqrt(self.Direction[0] ** 2 + self.Direction[1] ** 2)
        self.Direction = (self.Direction[0] / Len, self.Direction[1] / Len)
        self.x = - self.Direction[0] * self.distance + Coords[0]
        self.y = - self.Direction[1] * self.distance + Coords[1]
    
    def HeadPoints(self, *args):
        P1 = (self.x + self.Direction[0] * self.radius, self.y + self.Direction[1] * self.radius)
        P2 = (self.x - self.Direction[1] * self.radius * 1.1, self.y + self.Direction[0] * self.radius * 1.1)
        P3 = (self.x + self.Direction[1] * self.radius * 1.1, self.y - self.Direction[0] * self.radius * 1.1)
        P4 = (P2[0] + self.Direction[0] * self.radius * 0.3, P2[1] + self.Direction[1] * self.radius * 0.3)
        P5 = (P3[0] + self.Direction[0] * self.radius * 0.3, P3[1] + self.Direction[1] * self.radius * 0.3)
        P2 = (P2[0] - self.Direction[0] * self.radius * 0.2, P2[1] - self.Direction[1] * self.radius * 0.2)
        P3 = (P3[0] - self.Direction[0] * self.radius * 0.2, P3[1] - self.Direction[1] * self.radius * 0.2)
        if len(args) == 0:
            return(P1, P4, P2, P3, P5)
        else:
            args[0].append(P1)
            args[0].append(P4)
            args[0].append(P2)
            args[0].append(P3)
            args[0].append(P5)
            return args[0]
    
    def CellPoints(self, *args):
        P1 = (self.x - self.Direction[1] * self.radius, self.y + self.Direction[0] * self.radius)
        P2 = (self.x + self.Direction[1] * self.radius, self.y - self.Direction[0] * self.radius)
        if len(args) == 0:
            return(P1, P2)
        else:
            A = args[0][:len(args[0])//2 + 1]
            B = args[0][len(args[0])//2 + 1:]
            Ret = A
            Ret.append(P1)
            Ret.append(P2)
            Ret.extend(B)
            return Ret
    
    def TailPoints(self, *args):
        P1 = (self.x - self.Direction[1] * self.radius, self.y + self.Direction[0] * self.radius)
        P2 = (self.x - self.Direction[0] * self.radius, self.y - self.Direction[1] * self.radius)
        P3 = (self.x + self.Direction[1] * self.radius, self.y - self.Direction[0] * self.radius)
        if len(args) == 0:
            return(P1, P2, P3)
        else:
            A = args[0][:len(args[0])//2 + 1]
            B = args[0][len(args[0])//2 + 1:]
            Ret = A
            Ret.append(P1)
            Ret.append(P2)
            Ret.append(P3)
            Ret.extend(B)
            return Ret