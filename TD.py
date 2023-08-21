import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tower Defense Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Game variables
clock = pygame.time.Clock()
running = True
enemies = []
towers = []

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(100, screen_height - 100)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemies.remove(enemy)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new enemies
    if random.randint(0, 100) < 2:
        enemy = Enemy()
        enemies.append(enemy)

    # Update game objects
    for enemy in enemies:
        enemy.update()

    for tower in towers:
        tower.update()

    # Clear the screen
    screen.fill(white)

    # Draw game objects
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)

    for tower in towers:
        screen.blit(tower.image, tower.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()