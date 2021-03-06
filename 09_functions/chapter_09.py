import pygame
import sys
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, (60+x, 400+y, 30, 45))
    pygame.draw.polygon(screen, GREEN, ((150+x, 400+y), (75+x, 250+y), (x, 400+y)))
    pygame.draw.polygon(screen, GREEN, ((140+x, 350+y), (75+x, 230+y), (10+x, 350+y)))

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
BROWN = pygame.Color('brown')

FPS = 30

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 07')

    bg_screen = pygame.Surface(screen.get_size()).convert()
    bg_screen.fill(WHITE)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        screen.blit(bg_screen, (0, 0))

        draw_tree(screen, 0, 0)
        draw_tree(screen, 150, 10)
        draw_tree(screen, 300, 40)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
