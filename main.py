import os

import pygame

# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific # behavior.
try:
    import android
except ImportError:
    android = None

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

# get current path for assets
current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, 'data/background.png'))
spaceship = pygame.image.load(os.path.join(current_path, 'data/spaceship.png'))
bullet = pygame.image.load(os.path.join(current_path, 'data/bullet.png'))
bullet_y = 500
fired = False

planets = [os.path.join(current_path, 'data/p_one.png'), os.path.join(current_path, 'data/p_two.png'),
           os.path.join(current_path, 'data/p_three.png')]
p_index = 0
planet = pygame.image.load(planets[p_index])
planet_x = 140
move_direction = 'right'

keep_alive = True
clock = pygame.time.Clock()

while keep_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            keep_alive = False
        elif event.type == pygame.K_SPACE or event.type == pygame.FINGERUP:
            fired = True
        else:
            print(event.type)

    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500

    screen.blit(background, [0, 0])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160, 500])

    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'

    screen.blit(planet, [planet_x, 50])

    if bullet_y < 80 and 120 < planet_x < 180:
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        else:
            print('YOU WIN')
            keep_alive = False

    pygame.display.update()
    clock.tick(60)
