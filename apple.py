import pygame
import random

class Apple:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER, Color, Width = 6, r_min = 10, r_max = -1):
        self.Screen_WIDTH =SCREEN_WIDTH
        self.Screen_HEIGHT = SCREEN_HEIGHT
        self.Border = BORDER
        self.COLOR = Color
        self.Width = Width
        self.MinRadius = r_min
        if r_max == -1:
            r_max = int(1.5 * r_min)
        self.MaxRadius = r_max
        self.CurrentR = r_min
        self.x = 0
        self.y = 0
        self.Generate()
    
    def Generate(self):
        self.CurrentR = random.randint(self.MinRadius, self.MaxRadius)
        self.x = random.randint(self.Border + self.CurrentR + self.Width,
                                self.Screen_WIDTH - (self.Border + self.CurrentR + self.Width))
        self.y = random.randint(self.Border + self.CurrentR + self.Width,
                                self.Screen_HEIGHT - (self.Border + self.CurrentR + self.Width))
    
    def Render(self, Screen):
        pygame.draw.circle(Screen, self.COLOR, (self.x, self.y), self.CurrentR, self.Width)