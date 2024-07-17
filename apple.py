import pygame
import random

class Apple:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, Color, Width = 6, r_min = 10, r_max = -1):
        self.COLOR = Color
        self.MinRadius = r_min
        self.Width = Width
        self.MaxRadius = r_max
        if r_max == -1:
            self.MaxRadius = int(1.5 * r_min)
        self.CurrentR = r_min
        self.x = 0
        self.y = 0
        self.SCREEN_WIDTH =SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.Generate()
    
    def Generate(self):
        self.CurrentR = random.randint(self.MinRadius, self.MaxRadius)
        self.x = random.randint(self.CurrentR + self.Width, self.SCREEN_WIDTH - self.CurrentR - self.Width)
        self.y = random.randint(self.CurrentR + self.Width, self.SCREEN_HEIGHT - self.CurrentR - self.Width)
    
    def Render(self, Screen):
        pygame.draw.circle(Screen, self.COLOR, (self.x, self.y), self.CurrentR, self.Width)