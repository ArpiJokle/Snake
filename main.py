from cell import *
import pygame
import snake
import apple
from values import *
import random

pygame.init()

pygame.display.set_caption("SNAKE")
programIcon = pygame.image.load("icon.png")
pygame.display.set_icon(programIcon)
window = pygame.display.set_mode((WIDTH, HEIGHT))

RENDER = pygame.USEREVENT + 1
pygame.time.set_timer(RENDER, 1000 // 80)

GROWING = pygame.USEREVENT + 2
pygame.time.set_timer(GROWING, 50)


Snake = snake.Snake(WIDTH/2, HEIGHT/2, SNAKE_COLOR, SNAKE_DIST, SECTIONS, SNAKE_R_MIN, SNAKE_R_MAX, SNAKE_GROW)
for i in range(SNAKE_LEN):
    Snake.AddCell()

Apple = apple.Apple(WIDTH, HEIGHT, BORDER, APPLE_COLOR, APPLE_WIDTH, APPLE_MIN_R, APPLE_MAX_R)

running = True
while running:
    keys = pygame.key.get_pressed()
    if Snake.status:
        Snake.Turn(keys)
        Snake.Move(VELOCITY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Snake = snake.Snake(WIDTH/2, HEIGHT/2, SNAKE_COLOR, SNAKE_DIST, SECTIONS, SNAKE_R_MIN, SNAKE_R_MAX, SNAKE_GROW)
                for i in range(SNAKE_LEN):
                    Snake.AddCell() 
                Apple.Generate()
            if event.key == pygame.K_1:
                Snake.COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if event.type == GROWING:
            Snake.Growing()
        if event.type == RENDER:
            #! BACKGROUND
            window.fill((80, 80, 80))
            pygame.draw.rect(window, RED, ((0, 0), (WIDTH, HEIGHT)), BORDER * 2)
            
            Apple.Render(window)
            Snake.Render(window)
    
    Snake.CheckState(BORDER, WIDTH, HEIGHT, Apple)
    
    pygame.display.flip()

pygame.quit()