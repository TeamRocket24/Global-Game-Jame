import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		w, h = pygame.display.get_desktop_sizes()[0]
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()
		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('../audio/dnacing_dragon.mp3')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					print(event.pos)

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE and self.level.is_game_over:
						self.level = Level()

					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()