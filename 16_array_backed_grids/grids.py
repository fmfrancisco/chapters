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

WIDTH = 20
HEIGHT = 20
MARGIN = 5
SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 16')

    clock = pygame.time.Clock()

    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)
    
    
    color = WHITE

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                grid[row][column] = 1

        screen.fill(BLACK)

        for row in range(10):
            for column in range(10):
                if grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                posx = (MARGIN + WIDTH) * column + MARGIN
                posy = (MARGIN + HEIGHT) * row + MARGIN
                pygame.draw.rect(screen, color, (posx, posy, WIDTH, HEIGHT))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
