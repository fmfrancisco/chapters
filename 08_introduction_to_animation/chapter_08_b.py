import pygame
import sys
import random
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

FPS = 20

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 07')

    snow_list = []
    for i in range(100):
        x = random.randrange(0, SCREEN_WIDTH - 3)
        y = random.randrange(0, SCREEN_HEIGHT - 3)
        snow_list.append([x, y])

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        screen.fill(BLACK)
        # Process each snow flake in the list
        for i in range(len(snow_list)):
            # Draw the snow flake
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            snow_list[i][1] += 1

            if snow_list[i][1] > SCREEN_HEIGHT:
                x = random.randrange(0, SCREEN_WIDTH - 3)
                y = random.randrange(-50, -10)
                snow_list[i][0] = x
                snow_list[i][1] = y

        # Process A COPY of each snow flake's location in the list
        # for xy in snow_list:
        #     pygame.draw.circle(screen, WHITE, xy, 2)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
