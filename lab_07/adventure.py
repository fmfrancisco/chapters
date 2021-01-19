import pygame
import sys
from pygame.locals import *

WIDTH = 500
HEIGHT = 500

WHITE = (255, 255, 255)

FPS = 30


def terminate():
    pygame.quit()
    sys.exite()


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
        screen.fill(WHITE)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
