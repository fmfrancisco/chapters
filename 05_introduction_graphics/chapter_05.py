import pygame
import sys
import math

pygame.init()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

FPS = 30
PI = math.pi

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chapter 5')

clock = pygame.time.Clock()
y_offset = 0

font = pygame.font.SysFont('calibri', 25, True, False)
score = 0
text = font.render(f'Score: {str(score)}', True, BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, GREEN, (0, 10 + y_offset), (100, 110 + y_offset), 5)

    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(200 * math.sin(radians_x)) + 200
        y = int(75 *  math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, (x, y), (x, y), 5)

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLUE, (x_offset, 100), (x_offset + 10, 90), 2)
        pygame.draw.line(screen, BLUE, (x_offset, 90), (x_offset + 10, 100), 2)

    pygame.draw.rect(screen, BLACK, (350, 20, 250, 100), 2)
    pygame.draw.ellipse(screen, BLACK, (350, 20, 250, 100), 2)

    pygame.draw.rect(screen, BLACK, (400, 180, 250, 200), 2)

    #              surface, color,        rect,       start_angle, stop_angle
    pygame.draw.arc(screen, GREEN, (400, 180, 250, 200), PI / 2, PI, 2)
    pygame.draw.arc(screen, BLACK, (400, 180, 250, 200), 0, PI / 2, 2)
    pygame.draw.arc(screen, RED, (400, 180, 250, 200), 3 * PI / 2, 2 * PI, 2)
    pygame.draw.arc(screen, BLUE, (400, 180, 250, 200), PI, 3 * PI/2, 2)

    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)