from cell import *
import pygame
import snake
import apple
from values import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

RENDER = pygame.USEREVENT + 1
pygame.time.set_timer(RENDER, 1)


Snake = snake.Snake(WIDTH/2, HEIGHT/2, GREEN, SNAKE_DIST, SECTIONS, SNAKE_R_MIN, SNAKE_R_MAX)
for i in range(SNAKE_LEN):
    Snake.AddCell()

Apple = apple.Apple(WIDTH, HEIGHT, RED, APPLE_WIDTH, APPLE_MIN_R, APPLE_MAX_R)

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
                Snake.RandomRadiuses()
            if event.key == pygame.K_SPACE:
                Snake.AddCell()
        if event.type == RENDER:
            window.fill((80, 80, 80))
            
            pygame.draw.rect(window, RED, ((0, 0), (WIDTH, HEIGHT)), BORDER * 2)
            
            Apple.Render(window)
            Snake.Render(window)
            
    
    Snake.CheckState(BORDER, WIDTH, HEIGHT, Apple, SNAKE_GROW)
    
    pygame.display.flip()

pygame.quit()


#! MAKE BETTER GROW
#! MAKE RESTART BUTTON
#! REMOVE OTHER BUTTONS