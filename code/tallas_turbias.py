import pygame
from pytmx.util_pygame import load_pygame
from tile import Tile
from support import import_folder, import_csv_layout
import sys
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame("../map_alvaro/mapa_bueno.tmx")
sprite_group = pygame.sprite.Group()
cosillas = import_folder("../map_alvaro/imgs")
arbustos = import_csv_layout("../map_alvaro/map_arbustos.csv")
terreno = import_csv_layout("../map_alvaro/map_terreno.csv")
display_surface = pygame.display.get_surface()
floor = import_csv_layout("../map/map_Floor.csv")


# for row_index,row in enumerate(terreno):
# 	for col_index, col in enumerate(row):
# 		if col != '-1':
# 			x = col_index * 64
# 			y = row_index * 64

# 			surf = graphics['objects'][int(col)]
# 			Tile(
# 				(x,y),
# 				sprite_group,
# 				"terreno",
# 				surf
# 			)

# for layer, layer_name in zip(tmx_data.layers, tmx_data.layernames.keys()):
# 	if hasattr(layer, "data"):
# 		tiles = layer.tiles()
# 		for x, y, surf in tiles:
# 			pos = (x*64, y*64)
# 			if surf:
# 				Tile(pos, sprite_group, layer_name, surf)

# for obj, layer_name in zip(tmx_data.objects, tmx_data.layernames.keys()):
# 	pos = obj.x, obj.y
# 	if obj.image:
# 		Tile(pos, sprite_group, layer_name, obj.image)


def create_attack():
	pass

def destroy_attack():
	pass
	

floor_surf = pygame.image.load("../map_alvaro/mapa bueno.png")
floor_rect = floor_surf.get_rect(topleft=(0,0))
	
def create_map():
	# for row_index,row in enumerate(floor):
	# 	for col_index, col in enumerate(row):
	# 		x = col_index
	# 		y = row_index
	# 		Tile((x, y), sprite_group, "terreno")


	Player(
		(400,300),
		sprite_group,
		pygame.sprite.Group(),
		create_attack,
		destroy_attack,
	)

create_map()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("white")
	display_surface.blit(floor_surf, (0,0))

	for sprite in sprite_group.sprites():
		offset_pos = sprite.rect.topleft
		display_surface.blit(sprite.image, offset_pos)

	pygame.display.update()

