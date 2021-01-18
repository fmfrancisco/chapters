import pygame
import sys
import random
from pygame.locals import *


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.change_x = 0
        self.change_y = 0

        self.size = 10

        self.color = WHITE

    def off_screen(self):
        if self.x > 500 - 10 or self.x < 10:
            self.change_x *= - 1
        if self.y > 500 - 10 or self.y < 10:
            self.change_y *= -1

    def move(self):
        self.off_screen()
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)



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
    pygame.display.set_caption('Chapter 12')

    bg_screen = pygame.Surface(screen.get_size()).convert()
    bg_screen.fill(BLACK)

    balls = []
    for i in range(500):
        the_ball = Ball()
        the_ball.x = random.randint(10, 400)
        the_ball.y = random.randint(10, 400)
        the_ball.change_x = random.randint(1, 10)
        the_ball.change_y = random.randint(1, 5)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        size = random.randint(5, 15)

        the_ball.color = (r, g, b)
        the_ball.size = size
        balls.append(the_ball)


    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()


        screen.blit(bg_screen, (0, 0))

        for bls in balls:
            bls.move()

        for bls in balls:
            bls.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
