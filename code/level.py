# import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from upgrade import Upgrade
from npc import NPC
from settings import NPC_DATA

class Level:
	def __init__(self):

		# get the display surface 
		self.player_generated = False
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False
		self.is_game_over = False
		self.deaths = {'compinche_eugenio': 0, 'conejo':0,'lobo':0, "unicornio":0, "pollo":0, "ardilla":0, "ninja":0, "bandido":0, "ninja_boss": 0, "eugenio": 0, "soldado": 0}
		self.npcs_list = NPC_DATA.keys()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.npc_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()

		self.monster_name = None

	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('../map_news/map_floorBlocks.csv'),
			# 'grass': import_csv_layout('../map_news/map_arbustos.csv'),
			'object': import_csv_layout('../map_news/map_arboles_casas.csv'),
			'entities': import_csv_layout('../map_news/map_entities.csv')
		}
		graphics = {
			# 'grass': import_folder('../graphics/Grass'),
			# 'objects': import_folder('../graphics/new_objects')
		}


		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible') 
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile(
								(x,y),
								[
									self.visible_sprites,
								],
								'grass',
								random_grass_image)

						if style == 'object':
							# surf = graphics['objects'][int(col)]
							surf = pygame.image.load(f"../graphics/new_objects/{col}.png")
							Tile(
								(x,y),
								[
									self.visible_sprites,
									self.obstacle_sprites
								],
								'object',
								surf
							)

						if style == 'entities':
							if not self.player_generated:
								self.player = Player(
									(450, 400),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
								)
								self.player_generated = True

							elif col in self.npcs_list:
								npc_img_path = f"../graphics/npcs/{col}.png"

								NPC(
									col,
									NPC_DATA[col],
									npc_img_path,
									(x,y),
									[
										self.visible_sprites, 
										self.npc_sprites,
									],
									self.obstacle_sprites
								)


							else:
								if col == '9': self.monster_name = 'lobo'
								elif col == '11': self.monster_name = 'lobo'
								elif col == '20': self.monster_name = 'ninja'
								elif col == '19': self.monster_name = 'ninja'
								elif col == '8': self.monster_name ='pollo'
								elif col == '4': self.monster_name ='unicornio'
								elif col == '5': self.monster_name ='ardilla'
								elif col == '17': self.monster_name ='ninja_boss'
								elif col == '39': self.monster_name ='bandido'
								elif col == '40': self.monster_name ='bandido'
								elif col == '41': self.monster_name ='bandido'
								elif col == '7': self.monster_name = 'conejo'
								elif col == '33': self.monster_name ='compinche_eugenio'
								else: self.monster_name = None

								if self.monster_name:
									Enemy(
										self.monster_name,
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										# self.add_yuka
									)

	def create_attack(self):
		
		self.current_attack = Weapon(
			self.player,
			[
				self.visible_sprites,
				self.attack_sprites
			]
		)

	def destroy_attack(self):
		if self.current_attack: 
			self.current_attack.kill()
		self.current_attack = None

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(
					attack_sprite,
					self.attackable_sprites,
					False
				)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,75)
							for leaf in range(randint(3,6)):
								self.animation_player.create_grass_particles(
									pos - offset,
									[self.visible_sprites]
								)
							target_sprite.kill()
						else:
							target_sprite.get_damage(
								self.player,
								attack_sprite.sprite_type
							)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(
				attack_type,
				self.player.rect.center,
				[self.visible_sprites]
			)

	def trigger_death_particles(self,pos,particle_type):

		self.deaths [particle_type]+=1
		self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

	def add_yuka(self,amount):

		self.player.yuka += amount

	def toggle_menu(self):

		self.game_paused = not self.game_paused 

	def check_missions(self):
		obj = {"anim":self.deaths['lobo' ]+self.deaths["conejo"]+self.deaths['ardilla']+self.deaths['unicornio']+self.deaths['pollo' ], "bandido":self.deaths["bandido"],"eugenio":self.deaths["eugenio"],"soldado":self.deaths["soldado"],"ninja":self.deaths["ninja"],}
		missions = {"2" : {"anim":4}, "3":{"bandido":4}, "4":{"eugenio": 1, "soldado": 2}, "5":{"ninja":2}}
		reward = {"2":10, "3":20, "4":50, "5":100}
		for i, j in missions.items ():
			m = len (j.keys ())
			n = 0
			for k in j.keys ():
				#print (i, k)
				if obj [k] >=missions[i][k]:
					n+=1
					for mission in mision_data:
					    if mission["id"] == i:
					        mission["is_completed"] = True
					        # self.player.yuka += mission["yukas"]

			# if n == m:
			# 	self.add_yuka(reward[i])


	def run(self):
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player, self.npc_sprites, self.attackable_sprites)
		
		if self.game_paused and self.player.health > 0:
			self.upgrade.display()

		elif self.player.health <= 0:
			self.ui.show_game_over()
			self.player.hidden()
			self.is_game_over = True
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.visible_sprites.npc_update(self.player)
			self.player_attack_logic()
			self.check_missions()

		
class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../map_news/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [
			sprite 
			for sprite in self.sprites() 
			if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy'
		]
		for enemy in enemy_sprites:
			enemy.enemy_update(player)

	def npc_update(self, player):
		npc_sprites = [
			sprite 
			for sprite in self.sprites() 
			if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'npc'
		]
		for npc in npc_sprites:
			npc.npc_update(player)