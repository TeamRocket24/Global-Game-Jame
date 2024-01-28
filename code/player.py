import pygame 
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(-6,HITBOX_OFFSET['player'])

		# graphics setup
		self.import_player_assets()
		self.status = 'down'

		# movement 
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites

		# weapon
		self.create_attack = create_attack
		self.destroy_attack = destroy_attack
		self.weapon_index = 0
		self.weapon = list(weapon_data.keys())[self.weapon_index]
		self.can_switch_weapon = True
		self.weapon_switch_time = None
		self.switch_duration_cooldown = 200


		# stats
		self.stats = {'health': 100,'energy':60,'attack': 4,'speed': 30}
		self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'speed': 30}
		self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'speed': 100}
		self.health = self.stats['health']
		self.energy = self.stats['energy'] * 0.8
		self.yuka = 5
		self.speed = self.stats['speed']

		# damage timer
		self.vulnerable = True
		self.hurt_time = None
		self.invulnerability_duration = 500

		# import a sound
		self.weapon_attack_sound = pygame.mixer.Sound('../audio/sword.wav')
		self.weapon_attack_sound.set_volume(0.4)

		# Dialogue
		self.is_dialoguing = {}
		self.npc_dialoguing = None
		self.can_move = True

	def hidden(self):
		self.kill()

	def set_can_move(self, value):
		self.can_move = value

	def set_is_dialoguing(self, key, value):
		self.is_dialoguing[key] = value


	def set_npc_dialoguing(self, npc):
		self.npc_dialoguing = npc


	def import_player_assets(self):
		character_path = '../graphics/player/'
		self.animations = {
			'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]
		}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			# movement input
			if keys[pygame.K_UP] and self.can_move:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN] and self.can_move:
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT] and self.can_move:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT] and self.can_move:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

			# attack input 
			if keys[pygame.K_SPACE]:
				if True in self.is_dialoguing.values() and self.npc_dialoguing:
					if self.npc_dialoguing.has_more_dialogue(): 
						self.npc_dialoguing.next_dialogue()

					else:
						self.npc_dialoguing.close_dialogue(self)

				else:
					self.attacking = True
					self.attack_time = pygame.time.get_ticks()
					self.create_attack()
					self.weapon_attack_sound.play()


	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle','_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack','')

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
				self.attacking = False
				self.destroy_attack()

		if not self.can_switch_weapon:
			if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
				self.can_switch_weapon = True

		if not self.vulnerable:
			if current_time - self.hurt_time >= self.invulnerability_duration:
				self.vulnerable = True

	def animate(self):
		animation = self.animations[self.status]

		# loop over the frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

		# flicker 
		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

	def get_full_weapon_damage(self):
		base_damage = self.stats['attack']
		weapon_damage = weapon_data[self.weapon]['damage']
		return base_damage + weapon_damage

	def get_value_by_index(self,index):
		return list(self.stats.values())[index]

	def get_cost_by_index(self,index):
		return list(self.upgrade_cost.values())[index]

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.stats['speed'])

