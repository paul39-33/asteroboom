import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clk = pygame.time.Clock()
    dt = 0
    test = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        test.update(dt)
        test.draw(screen)
        pygame.display.flip()
        dt = game_clk.tick(60) / 1000


if __name__ == "__main__":
    main()