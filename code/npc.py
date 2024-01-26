from entity import Entity
import pygame

class NPC(Entity):
	def __init__(
		self,
		npc_name,
		pos,
		image,
		groups,
		dialogue ):

		# general setup
		super().__init__(groups)
		self.sprite_type = 'npc'

		# graphics
		self.status = 'idle'
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect(topleft = pos)

		# stats
		self.name = npc_name
		self.notice_radius = 100

		# Dialogue
		self.index_dialogue = 0
		self.dialogue_list = dialogue


	def get_player_distance_direction(self,player):
		npc_vec = pygame.math.Vector2(self.rect.center)
		player_vec = pygame.math.Vector2(player.rect.center)
		distance = (player_vec - npc_vec).magnitude()

		if distance > 0:
			direction = (player_vec - npc_vec).normalize()
		else:
			direction = pygame.math.Vector2()

		return (distance,direction)


	def get_status(self, player):
		distance = self.get_player_distance_direction(player)[0]

		if distance <= self.notice_radius:
			self.status = 'speak'
			player.set_is_dialoguing(self.name, True)
			player.set_npc_dialoguing(self)
		
		else:
			self.status = 'idle'
			player.set_is_dialoguing(self.name, False)
			if player.npc_dialoguing == self:
				player.set_npc_dialoguing(None)
				self.index_dialogue = 0



	def actions(self,player):
		if self.status == 'speak':
			pass

	def get_dialogue(self):
		if len(self.dialogue_list) <= self.index_dialogue:
			self.index_dialogue = len(self.dialogue_list) - 1
		
		text = self.dialogue_list[self.index_dialogue]
		return text

	def has_more_dialogue(self):
		return self.index_dialogue < len(self.dialogue_list) - 1

	def next_dialogue(self):
		self.index_dialogue += 1

	def close_dialogue(self, player):
		self.status = 'idle'
		player.set_is_dialoguing(self.name, False)
		if player.npc_dialoguing == self:
			player.set_npc_dialoguing(None)

	def npc_update(self,player):
		self.get_status(player)
