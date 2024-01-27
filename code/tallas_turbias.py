import pygame
from pytmx.util_pygame import load_pygame
from tile import Tile
from support import import_folder, import_csv_layout
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame("../map_alvaro/mapa_bueno.tmx")
sprite_group = pygame.sprite.Group()
cosillas = import_folder("../map_alvaro/imgs")
arbustos = import_csv_layout("../map_alvaro/map_arbustos.csv")
terreno = import_csv_layout("../map_alvaro/map_terreno.csv")


for row_index,row in enumerate(terreno):
	for col_index, col in enumerate(row):
		if col != '-1':
			x = col_index * 64
			y = row_index * 64

			surf = graphics['objects'][int(col)]
			Tile(
				(x,y),
				sprite_group,
				"terreno",
				surf
			)

for layer, layer_name in zip(tmx_data.layers, tmx_data.layernames.keys()):
	if hasattr(layer, "data"):
		tiles = layer.tiles()
		for x, y, surf in tiles:
			pos = (x*64, y*64)
			if surf:
				Tile(pos, sprite_group, layer_name, surf)

for obj, layer_name in zip(tmx_data.objects, tmx_data.layernames.keys()):
	pos = obj.x, obj.y
	if obj.image:
		Tile(pos, sprite_group, layer_name, obj.image)
	
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("black")
	sprite_group.draw(screen)

	pygame.display.update()

