import pygame
import settings
from settings import * 
import pygame.camera

class UI:
	def __init__(self):
		
		self.cont = 0
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)


	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,exp):
		text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

	def show_npc_label(self, npc_name, *pos):
		font = pygame.font.Font(None, 50)
		text_surface = font.render(npc_name, True, (255, 255, 255))
		rect = text_surface.get_rect()
		label_height = text_surface.get_height()
		self.display_surface.blit(
			text_surface, 
			pos
		)


	def show_npc_dialogue(self,npc):
		w = 120
		h = 630
		text_font = pygame.font.Font(None, 30)
		text_dialogue = npc.get_dialogue()
		text_displayed = ""

		for j in text_dialogue.split(" "):
			text = text_font.render(j+" ", True, [0, 0, 0])
			if w+text.get_width()>1200:
				h+=text.get_height()
				w = 120
			textRect = text.get_rect(topleft = [w, h])
			w+=text.get_width()
			self.display_surface.blit(text, textRect)

		button_font = pygame.font.Font(None, 35)
		if npc.has_more_dialogue():
			button_surface = button_font.render("siguiente", True, (255, 0, 0))
			self.display_surface.blit(
				button_surface, 
				(1000, 600)
			)
		else:
			button_surface = button_font.render("Dejar de Hablar", True, (255, 0, 0))
			self.display_surface.blit(
				button_surface, 
				(1000, 600)
			)


	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(10,630,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def display(self,player, npc_sprites):
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)

		self.show_exp(player.exp)

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)

		if player.npc_dialoguing:
			npc = player.npc_dialoguing
			self.show_npc_dialogue(npc)