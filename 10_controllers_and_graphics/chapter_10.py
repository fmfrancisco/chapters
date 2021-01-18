import pygame
import sys
from pygame.locals import *

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

FPS = 30

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def terminate():
    pygame.quit()
    sys.exit()


def draw_snowman(screen, x,  y):
    pygame.draw.ellipse(screen, WHITE, (35 + x, y, 25, 25))
    pygame.draw.ellipse(screen, WHITE, (23 + x, 20 + y, 50, 50))
    pygame.draw.ellipse(screen, WHITE, (x, 65 + y, 100, 100))


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 07')
    pygame.mouse.set_visible(False)

    bg_screen = pygame.Surface(screen.get_size()).convert()
    bg_screen.fill(GREEN)

    x_speed = 0
    y_speed = 0

    x_coord = 10
    y_coord = 10

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x_speed = -3
                elif event.key == K_RIGHT:
                    x_speed = 3
                elif event.key == K_UP:
                    y_speed = -3
                elif event.key == K_DOWN:
                    y_speed = 3
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    x_speed = 0
                elif event.key == K_UP or event.key == K_DOWN:
                    y_speed = 0

        screen.blit(bg_screen, (0, 0))

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        x_coord += x_speed
        y_coord += y_speed
        if x_coord < 0:
            x_coord = 0
        elif x_coord > SCREEN_WIDTH - 10:
            x_coord = SCREEN_WIDTH - 10
        if y_coord < 0:
            y_coord = 0
        elif y_coord > SCREEN_WIDTH - 30:
            y_coord = SCREEN_WIDTH - 30

        # draw_snowman(screen, 10, 10)
        # draw_snowman(screen, 300, 10)
        # draw_snowman(screen, 10, 300)
        draw_stick_figure(screen, x_coord, y_coord)
        draw_stick_figure(screen, x, y)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
