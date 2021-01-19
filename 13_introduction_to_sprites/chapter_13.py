import pygame
import sys
import random
from pygame.locals import *


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

FPS = 20


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1
		if self.rect.y > SCREEN_HEIGHT + 15:
			self.reset_pos()			
	
	def reset_pos(self):
		self.rect.x = random.randrange(0, SCREEN_WIDTH)
		self.rect.y = random.randrange(-300, -10)


def terminate():
	pygame.quit()
	sys.exit()


def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Chapter 13')
	pygame.mouse.set_visible(False)
	bg_screen = pygame.Surface(screen.get_size()).convert()
	bg_screen.fill(WHITE)

	block_list = pygame.sprite.Group()
	all_sprites_list = pygame.sprite.Group()

	for i in range(50):
		block = Block(BLACK, 20, 15)

		block.rect.x = random.randrange(SCREEN_WIDTH)
		block.rect.y = random.randrange(SCREEN_HEIGHT)

		block_list.add(block)
		all_sprites_list.add(block)

	player = Block(RED, 20, 15)
	all_sprites_list.add(player)

	clock = pygame.time.Clock()

	score = 0

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()

		screen.blit(bg_screen, (0, 0))

		pos = pygame.mouse.get_pos()
		player.rect.x = pos[0]
		player.rect.y = pos[1]

		block_list.update()

		block_hit_list = pygame.sprite.spritecollide(player, block_list, False)

		for block in block_hit_list:
			score += 1
			print(score)
			block.reset_pos()
		
		all_sprites_list.draw(screen)

		pygame.display.update()
		clock.tick(FPS)


if __name__ == "__main__":
	main()
