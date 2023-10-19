import pygame
import constants
from enemy import Enemy

#initializing pygame
pygame.init()

#create clock
clock = pygame.time.Clock()

# Set up display
screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Tower Defense Game")

#loading images
enemy_image = pygame.image.load('imgs/Enemies/E1.png').convert_alpha()

#create groups
enemy_group = pygame.sprite.Group()

waypoints = [
(100, 100),
(400, 200),
(400, 100),
(200, 300)
]



enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

#game loop
run = True
while run: 

    clock.tick(constants.tick_per_second)

    screen.fill("black")

    #draw enemy path
    pygame.draw.lines(screen, "white", False, waypoints)


    #update groups
    enemy_group.update()

    #drawing groups
    enemy_group.draw(screen)

    #event handler
    for event in pygame.event.get():
        #ends game
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.flip()

pygame.quit()
