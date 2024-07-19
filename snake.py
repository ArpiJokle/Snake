import pygame
from cell import *
import math
import random

class Snake:
    def __init__(self, x, y, Color, d = 20, sections = 800, r_min = 20, r_max = -1, grow_len = 6):
        if r_max == -1:
            r_max = int(1.5 * r_min)
        self.r_min = r_min
        self.r_max = r_max
        
        self.CellList = [Cell(x, y, r_min, d)]
        
        self.COLOR = Color
        
        self.status = True
        self.Sections = sections
        
        self.Grow_len = grow_len
        
        self.FoodList = []
        self.Grow = 0
        
        self.DLen = 0
        self.DWidth = 0
    
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
        if self.status:
            self.Smooth()
            self.AddWidth()
        
        SnakePoints = []
        SnakePoints = self.CellList[0].HeadPoints(SnakePoints)
        for i in range(1, len(self.CellList)):
            SnakePoints = self.CellList[i].CellPoints(SnakePoints)
        SnakePoints = self.CellList[len(self.CellList) - 1].TailPoints(SnakePoints)
        
        for i in range(0, len(SnakePoints)-1):
            pygame.draw.line(screen, self.COLOR, SnakePoints[i], SnakePoints[i + 1], 5)
        pygame.draw.line(screen, self.COLOR, SnakePoints[0], SnakePoints[len(SnakePoints) - 1], 5)
        
        if not self.status:
            self.RandomRadiuses()
            #self.AddWidth()
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("SCORE : " + str(self.DLen + self.DWidth), True, (210, 120, 210))
            textRect = text.get_rect()
            textRect.center = (screen.get_width() // 2, screen.get_height() // 3)
            screen.blit(text, textRect)
            text = font.render("Press \'r\' to RESTART", True, (210, 120, 210))
            textRect = text.get_rect()
            textRect.center = (screen.get_width() // 2, screen.get_height() // 3 + 40)
            screen.blit(text, textRect)
        else:
            self.CellList[0].drawHead(screen);
    
    def RandomRadiuses(self):
        for _ in range(0, len(self.CellList)):
            self.CellList[_].radius = random.randint(self.r_min, self.r_max)
    
    def AddCell(self):
        self.CellList.append(Cell(self.CellList[len(self.CellList) - 1], self.CellList[0]))
        self.Smooth()
    
    def Smooth(self):
        a = - 4 * (self.r_max - self.r_min) / (len(self.CellList) ** 2)
        b = - a * len(self.CellList)
        for i in range(1, len(self.CellList) + 1):
            self.CellList[i - 1].radius = self.r_min + a * i * i + b * i
    
    def CheckState(self, Border, Width, Height, Apple):
        #! BORDER DEATH
        Distance = min(abs(self.CellList[0].x - Width), abs(self.CellList[0].x),
                       abs(self.CellList[0].y), abs(self.CellList[0].y - Height))
        if Distance <= Border + self.CellList[0].radius:
            self.status = False
            self.Grow = 0
            self.COLOR = (0.2 * self.COLOR[0], 0.2 * self.COLOR[1], 0.2 * self.COLOR[2])
            return -1
        
        #!  SELF COLLISION DEATH
        for i in range(math.ceil(self.CellList[0].radius * 3 / self.CellList[1].distance), len(self.CellList)):
            Distance = math.sqrt((self.CellList[0].x - self.CellList[i].x) ** 2 + (self.CellList[0].y - self.CellList[i].y) ** 2)
            if Distance <= self.CellList[0].radius + self.CellList[i].radius:
                self.status = False
                self.Grow = 0
                self.COLOR = (0.2 * self.COLOR[0], 0.2 * self.COLOR[1], 0.2 * self.COLOR[2])
                return i
        
        #! APPLE EATING
        Distance = math.sqrt((self.CellList[0].x - Apple.x) ** 2 + (self.CellList[0].y - Apple.y) ** 2)
        if Distance <= self.CellList[0].radius + Apple.CurrentR:
            Apple.Generate()
            self.FoodList.append([3, Apple.CurrentR])
        
        return -1
    
    def AddWidth(self):
        for Food in self.FoodList:
            x = range(1, len(self.CellList) - 1)
            R = Food[1] // self.Grow_len
            y = range(Food[0] - R, Food[0] + R)
            xy = set(x) & set(y)
            if len(xy): 
                a = - 4 * int(math.ceil(Food[1] // self.Grow_len) * 1.8) / (len(xy) ** 2)
                b = - a * len(xy)
                MIN = min(xy)
                for i in xy:
                    X = i - MIN
                    self.CellList[i].radius += (a * X * X + b * X)
    
    def Growing(self):
        if self.status:
            for i in range(len(self.FoodList)):
                if self.FoodList[i][0] < len(self.CellList) - 3:
                    self.FoodList[i][0] += 1
                else:
                    if self.FoodList[i][1] > 0:
                        if self.r_min != 40 and random.randint(1, 20) == 1:
                            self.r_min += 2
                            self.r_max += 2
                            self.DWidth += 4
                        else:
                            self.Grow += 1
                        self.FoodList[i][1] -= self.Grow_len
            if self.Grow:
                self.AddCell()
                self.Grow -= 1
                self.DLen += 1