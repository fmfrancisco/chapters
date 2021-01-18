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

SCREEN_WIDTH = 502
SCREEN_HEIGHT = 402


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chapter 07')
    pygame.mouse.set_visible(False)

    bg_screen = pygame.image.load('_img/bg_green.jpg').convert()

    player_img = pygame.image.load('_img/snake.png').convert()
    player_img.set_colorkey(BLACK)

    click_sound = pygame.mixer.Sound('_sound/laser5.ogg')

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                click_sound.play()

        screen.blit(bg_screen, (0, 0))

        player_pos = pygame.mouse.get_pos()
        x = player_pos[0]
        y = player_pos[1]

        screen.blit(player_img, (x, y))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()