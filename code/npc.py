from entity import Entity
import pygame
from dialogue import Dialogue

class NPC(Entity):
	def __init__(
		self,
		npc_name,
		npc_data,
		pos,
		groups 
	):

		# general setup
		super().__init__(groups)
		self.sprite_type = 'npc'

		# graphics
		self.status = 'idle'
		self.image = pygame.image.load(npc_data["graphic"])
		self.rect = self.image.get_rect(topleft = pos)

		# stats
		self.name = npc_name
		self.notice_radius = 100

		# Dialogue
		self.finish_dialogue = False
		self.let_move = npc_data["let_move"]
		self.index_dialogue = 0
		# Comprobar si el nombre del npc esta en la lista
		# de misiones y la mision no ha sido completada 
		# y si esta agregar el dialogo de la mision
		# 
		# Si no se cumple lo anteriro 
		# comprobar las reacciones del npc
		# si tiene alguna reaccion poner su dialogo
		# 
		# Si no tiene ninguna de las anteriores
		# entonces que tenga el dialogo por default
		self.dialogue_list = npc_data["dialogue"]
		self.dialogue = Dialogue(self.dialogue_list, self)


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

		if distance <= self.notice_radius and not self.finish_dialogue:
			self.status = 'speak'
			player.set_is_dialoguing(self.name, True)
			player.set_npc_dialoguing(self.dialogue)
			player.set_can_move(self.let_move)

		else:
			self.status = 'idle'
			player.set_is_dialoguing(self.name, False)
			if player.npc_dialoguing == self.dialogue:
				player.set_npc_dialoguing(None)
				self.dialogue.index_dialogue = 0



	def actions(self,player):
		if self.status == 'speak':
			pass
			

	def npc_update(self,player):
		self.get_status(player)
