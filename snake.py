import pygame
from cell import *
import math
import random
import apple

class Snake:
    def __init__(self, x, y, Color, d = 20, sections = 800, r_min = 20, r_max = -1):
        if r_max == -1:
            r_max = int(1.5 * r_min)
        self.r_min = r_min
        self.r_max = r_max
        self.a = - 4 * (r_max - r_min)
        self.b = - self.a 
        self.CellList = [Cell(x, y, r_min, d)]
        self.COLOR = Color
        self.status = True
        self.Sections = sections
        self.Grow = 0
    
    def Turn(self, keys):
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
            Dif = abs(Target - self.CellList[0].angle)
            if abs(Dif - 2*math.pi) <= 1E-7:
                Dif = 0
            if Dif > 1E-7:
                if self.CellList[0].angle < Target:
                    if Dif <= math.pi:
                        self.CellList[0].angle += math.pi/self.Sections
                    else:
                        self.CellList[0].angle -= math.pi/self.Sections
                else:
                    if Dif < math.pi:
                        self.CellList[0].angle -= math.pi/self.Sections
                    else:
                        self.CellList[0].angle += math.pi/self.Sections
            else:
                self.CellList[0].angle = Target
        while self.CellList[0].angle >= 2*math.pi:
            self.CellList[0].angle -= 2*math.pi
        while self.CellList[0].angle < 0:
            self.CellList[0].angle += 2*math.pi
    
    def Move(self, velocity):
        self.CellList[0].MoveHead(velocity)
        for i in range(1, len(self.CellList)):
            self.CellList[i].MoveCell((self.CellList[i-1].x, self.CellList[i-1].y))
    
    def Render(self, screen):
        if not self.status:
            self.RandomRadiuses()
        else:
            self.CellList[0].drawHead(screen);
        
        SnakePoints = []
        SnakePoints = self.CellList[0].HeadPoints(SnakePoints)
        for i in range(1, len(self.CellList)):
            SnakePoints = self.CellList[i].CellPoints(SnakePoints)
        SnakePoints = self.CellList[len(self.CellList) - 1].TailPoints(SnakePoints)
        
        for i in range(0, len(SnakePoints)-1):
            pygame.draw.line(screen, self.COLOR, SnakePoints[i], SnakePoints[i + 1], 5)
        pygame.draw.line(screen, self.COLOR, SnakePoints[0], SnakePoints[len(SnakePoints) - 1], 5)
    
    def RandomRadiuses(self):
        for _ in range(0, len(self.CellList)):
            self.CellList[_].radius = random.randint(self.r_min, self.r_max)
    
    def AddCell(self):
        self.CellList.append(Cell(self.CellList[len(self.CellList) - 1], self.CellList[0]))
        self.a = - 4 * (self.r_max - self.r_min) / (len(self.CellList) ** 2)
        self.b = - self.a * len(self.CellList)
        self.Smooth()
    
    def Smooth(self):
        for i in range(1, len(self.CellList) + 1):
            self.CellList[i - 1].radius = self.r_min + self.a * i * i + self.b * i
    
    def CheckState(self, Border, Width, Height, Apple, Add):
        Distance = min(abs(self.CellList[0].x - Width), abs(self.CellList[0].x),
                       abs(self.CellList[0].y), abs(self.CellList[0].y - Height))
        if Distance <= Border + self.CellList[0].radius:
            self.status = False
            self.Grow = 0
            self.COLOR = (0.2 * self.COLOR[0], 0.2 * self.COLOR[1], 0.2 * self.COLOR[2])
        
        for i in range(math.ceil(self.CellList[0].radius * 3 / self.CellList[1].distance), len(self.CellList)):
            DIST = math.sqrt((self.CellList[0].x - self.CellList[i].x) ** 2 + (self.CellList[0].y - self.CellList[i].y) ** 2)
            if DIST <= self.CellList[0].radius + self.CellList[i].radius:
                self.status = False
                self.COLOR = (0.2 * self.COLOR[0], 0.2 * self.COLOR[1], 0.2 * self.COLOR[2])
                return i
        
        Distance = math.sqrt((self.CellList[0].x - Apple.x) ** 2 + (self.CellList[0].y - Apple.y) ** 2)
        if Distance <= self.CellList[0].radius + Apple.CurrentR:
            Apple.Generate()
            if random.randint(1, 10) == 1 and self.r_min != 35:
                self.r_min += 4
                self.r_max += 4
                self.Smooth()
            else:
                self.Grow += Add
        
        return -1