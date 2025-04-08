import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clk = pygame.time.Clock()
    dt = 0

    #Game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    test = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)
        for item in asteroids:
            if item.collision(test):
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen) 
        pygame.display.flip()
        dt = game_clk.tick(60) / 1000


if __name__ == "__main__":
    main()