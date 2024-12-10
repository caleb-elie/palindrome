import pygame
import time
pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
snake_size = 20
snake_speed = 15
snake_x = 50
snake_y = 50
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    snake_x -= snake_size
elif keys[pygame.K_RIGHT]:
    snake_x += snake_size
elif keys[pygame.K_UP]:
    snake_y -= snake_size
elif keys[pygame.K_DOWN]:
    snake_y += snake_size
window.fill((0, 0, 0))
pygame.draw.rect(window, (255, 255, 255), (snake_x, snake_y, snake_size, snake_size))
pygame.display.update()
if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
    game_over = True
clock = pygame.time.Clock()
clock.tick(snake_speed)
pygame.quit()
