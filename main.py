# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from player import Player
from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # player.update(dt)
        # player.draw(screen)
        updatable.update(dt)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        time_since_last_call = clock.tick(60)
        dt = time_since_last_call / 1000



if __name__ == "__main__":
    main()
