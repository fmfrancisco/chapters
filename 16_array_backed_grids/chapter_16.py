import pygame
import sys
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255
WIDTH = 20
HEIGHT = 20
MARGIN = 5

WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
GREEN = pygame.Color('green')
color = WHITE
FPS = 30

def main():
    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Game')
    BG_SCREEN = pygame.Surface(SCREEN.get_size()).convert()
    BG_SCREEN.fill(BLACK)

    clock = pygame.time.Clock()

    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)

    # grid = [[0 for x in range(10)] for y in range(10)]

    # Set a row 1, column 5 to ono
    grid[1][5] = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                column = mouse_pos[0] // (WIDTH + MARGIN)
                row = mouse_pos[1] // (HEIGHT + MARGIN)
                grid[row][column] = 1

        SCREEN.blit(BG_SCREEN, (0, 0))

        for row in range(10):
            for column in range(10):
                posx = (MARGIN + WIDTH) * column + MARGIN
                posy = (MARGIN + HEIGHT) * row + MARGIN
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(SCREEN, color, (posx, posy, WIDTH, HEIGHT))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()