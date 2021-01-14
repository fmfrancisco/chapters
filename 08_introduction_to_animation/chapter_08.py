import pygame
import sys
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

FPS = 30

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 07')

    bg_screen = pygame.Surface(screen.get_size()).convert()
    bg_screen.fill(BLACK)

    rect_x = 50
    rect_y = 50

    # Speed and direction of rectangle
    rect_x_change_x = 5
    rect_y_change_y = 5

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()


        screen.blit(bg_screen, (0, 0))

        pygame.draw.rect(screen, WHITE, (rect_x, rect_y, 50, 50))
        pygame.draw.rect(screen, RED, (rect_x + 10, rect_x + 10, 30, 30))

        if rect_y > SCREEN_HEIGHT - 50 or rect_y < 0:
            rect_y_change_y = rect_y_change_y * -1

        if rect_x > SCREEN_WIDTH - 50 or rect_x < 0:
            rect_x_change_x = rect_x_change_x * -1
        rect_x += rect_x_change_x
        rect_y += rect_y_change_y

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()