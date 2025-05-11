import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Car Racing")

# Load images
car_img = pygame.image.load("car.png")  # Replace with your car image path
enemy_img = pygame.image.load("enemy_car.png")  # Replace with enemy car image
road_img = pygame.image.load("road.png")  # Optional road background

# Resize if needed
car_img = pygame.transform.scale(car_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)

# Game variables
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120
car_speed = 5

enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

clock = pygame.time.Clock()

def draw_window():
    win.fill(WHITE)
    win.blit(road_img, (0, 0))
    win.blit(car_img, (car_x, car_y))
    win.blit(enemy_img, (enemy_x, enemy_y))
    pygame.display.update()

def check_collision(x1, y1, x2, y2):
    return pygame.Rect(x1, y1, 50, 100).colliderect(pygame.Rect(x2, y2, 50, 100))

# Game loop
run = True
while run:
    clock.tick(30)  # 30FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y < HEIGHT - 100:
        car_y += car_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)

    # Collision check
    if check_collision(car_x, car_y, enemy_x, enemy_y):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    draw_window()

pygame.quit()
