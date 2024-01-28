import pygame
from settings import *
# missions_text = {"Mision 1": "Conseguir medicina para mamá", "Mission 2": "Matar indefensos animalitos del bosque", "Mision 3": "Terminar con los problemáticos bandidos", "Mision 3":"Ajustar cuentas", "Mision 4":"Liberar al pueblo del yugo del lord"}
missions_text = mision_data 

page = 0
def missions (page):
	surface = pygame.display.get_surface()
	pergamino = pygame.image.load ("../graphics/pergamino_cut.png")
	surface.blit(pergamino, [349, 191])
	#pygame.draw.rect(surface ,[251, 232, 96], [348, 191, 552, 347])
	font = pygame.font.Font('freesansbold.ttf', 25)
	h = 302+3
	w = 431+3
	if page == 0:
		for i in missions_text[0:2]:
			text = font.render(i["name"], True, [0, 0, 0])
			textRect = text.get_rect(topleft = [w, h])
			h+=text.get_height()
			surface.blit(text, textRect)
			if not i["is_completed"]:
				for j in i["obj"].split(" "):
					text = font.render(j+" ", True, [0, 0, 0])
					if w+text.get_width()>670:
						h+=text.get_height()
						w = 431+3
					textRect = text.get_rect(topleft = [w, h])
					w+=text.get_width()
					surface.blit(text, textRect)
				w = 431+3
				h+=text.get_height()*2
			else:
				text = font.render("Completada. ", True, [0, 255, 0])
				textRect = text.get_rect(topleft = [w, h])
				surface.blit(text, textRect)

	if page == 2:
		for i in missions_text[2:4]:
			text = font.render(i["name"], True, [0, 0, 0])
			textRect = text.get_rect(topleft = [w, h])
			h+=text.get_height()
			surface.blit(text, textRect)
			if not i["is_completed"]:
				for j in i["obj"].split(" "):
					text = font.render(j+" ", True, [0, 0, 0])
					if w+text.get_width()>670:
						h+=text.get_height()
						w = 431+3
					textRect = text.get_rect(topleft = [w, h])
					w+=text.get_width()
					surface.blit(text, textRect)
				w = 431+3
				h+=text.get_height()*2
			else:
				text = font.render("Completada. ", True, [0, 255, 0])
				textRect = text.get_rect(topleft = [w, h])
				surface.blit(text, textRect)

class Upgrade:
	def __init__(self,player):
		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.attribute_nr = len(player.stats)
		self.attribute_names = list(player.stats.keys())
		self.max_values = list(player.max_stats.values())
		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		# item creation
		self.height = self.display_surface.get_size()[1] * 0.8
		self.width = self.display_surface.get_size()[0] // 6

		# selection system 
		self.selection_index = 0
		self.selection_time = None
		self.can_move = True

		#my vars
		self.menu_elem = ["misiones", " stats", "config"]
		self.num_elem =  len (self.menu_elem)
		self.menu_sel = 0

		self.create_items()

	def input(self):
		global page
		keys = pygame.key.get_pressed()
		if self.menu_sel==1:
			if self.can_move:
				if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
					self.selection_index += 1
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()
				elif keys[pygame.K_LEFT] and self.selection_index >= 1:
					self.selection_index -= 1
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()

				if keys[pygame.K_SPACE]:
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()
					self.item_list[self.selection_index].trigger(self.player)
		else:
			if self.can_move:
				if keys[pygame.K_DOWN] and self.selection_index < self.num_elem - 1:
					self.selection_index += 1
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()
				elif keys[pygame.K_UP] and self.selection_index >= 1:
					self.selection_index -= 1
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()


				elif keys[pygame.K_RIGHT] and self.menu_sel == 2:
					if page == 0:
						page = 2
						missions (page)
				elif keys[pygame.K_LEFT] and self.menu_sel == 2:
					if page == 2:
						page = 0
						missions (page)

				elif keys[pygame.K_SPACE]:
					self.can_move = False
					self.selection_time = pygame.time.get_ticks()
					if self.menu_sel==2 and self.selection_index == 0:
						self.menu_sel=0
					elif self.selection_index == 0 and self.menu_sel==0:
						self.menu_sel=2
						missions(page)
	def selection_cooldown(self):
		if not self.can_move:
			current_time = pygame.time.get_ticks()
			if current_time - self.selection_time >= 300:
				self.can_move = True

	def create_items(self):
		self.item_list = []
		if self.menu_sel == 0:
			for item, index in enumerate(range(self.num_elem)):
				# horizontal position
				full_height = self.display_surface.get_size()[1]
				#increment = full_height // self.num_elem
				increment =  50
				self.height = 25 
				top = ((item) * increment) + 261
			
				# vertical position 
				left = 502


				# create the object 
				self.width = self.display_surface.get_size()[0]//4 -10
				item = Item(left,top,self.width,self.height,index,self.font)
				self.item_list.append(item)
		if self.menu_sel == 1:
			for item, index in enumerate(range(self.attribute_nr)):
				# horizontal position
				full_width = self.display_surface.get_size()[0]
				increment = full_width // self.attribute_nr
				left = (item * increment) + (increment - self.width) // 2
			
				# vertical position 
				top = self.display_surface.get_size()[1] * 0.1

				# create the object 
				item = Item(left,top,self.width,self.height,index,self.font)
				self.item_list.append(item)


	def display(self):
		self.input()
		self.selection_cooldown()
		if self.menu_sel == 0:
			pygame.draw.rect(self.display_surface,UI_BG_COLOR,[411, 207, 573, 321], 0, 10)
			for index, item in enumerate(self.item_list):
				self.s_height = self.display_surface.get_size()[1]
				self.s_width = self.display_surface.get_size()[0]
				name=self.menu_elem[index]
				item.display2(self.display_surface,self.selection_index,name)
		elif self.menu_sel==2:
			missions (page)
		else:
			for index, item in enumerate(self.item_list):

				# get attributes
				name = self.attribute_names[index]
				value = self.player.get_value_by_index(index)
				max_value = self.max_values[index]
				cost = self.player.get_cost_by_index(index)
				item.display(self.display_surface,self.selection_index,name,value,max_value,cost)

class Item:
	def __init__(self,l,t,w,h,index,font):
		self.rect = pygame.Rect(l,t,w,h)
		self.index = index
		self.font = font

	def display_names(self,surface,name,cost,selected):
		color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

		# title
		title_surf = self.font.render(name,False,color)
		title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

		# cost 
		cost_surf = self.font.render(f'{int(cost)}',False,color)
		cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

		# draw 
		surface.blit(title_surf,title_rect)
		surface.blit(cost_surf,cost_rect)

	def display_bar(self,surface,value,max_value,selected):

		# drawing setup
		top = self.rect.midtop + pygame.math.Vector2(0,60)
		bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
		color = BAR_COLOR_SELECTED if selected else BAR_COLOR

		# bar setup
		full_height = bottom[1] - top[1]
		relative_number = (value / max_value) * full_height
		value_rect = pygame.Rect(top[0] - 15,bottom[1] - relative_number,30,10)

		# draw elements
		pygame.draw.line(surface,color,top,bottom,5)
		pygame.draw.rect(surface,color,value_rect)

	def trigger(self,player):
		upgrade_attribute = list(player.stats.keys())[self.index]

		if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
			player.exp -= player.upgrade_cost[upgrade_attribute]
			player.stats[upgrade_attribute] *= 1.2
			player.upgrade_cost[upgrade_attribute] *= 1.4

		if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
			player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]
	def missions (self):
		surface = pygame.display.get_surface()
		pygame.draw.rect(surface ,[255, 255, 0], [348, 191, 552, 347])
		title_surf = self.font.render("mision1",False,[0, 0, 0])
		title_rect = title_surf.get_rect(topleft = [348, 191] + pygame.math.Vector2(3, 3))
		surface.blit(title_surf,title_rect)
		

	def display(self,surface,selection_num,name,value,max_value,cost):
		if self.index == selection_num:
			pygame.draw.rect(surface,[255, 255, 0],self.rect)
			pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
		else:
			pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
			pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
	
		self.display_names(surface,name,cost,self.index == selection_num)
		self.display_bar(surface,value,max_value,self.index == selection_num)
	
	def display2(self,surface,selection_num,name,):
		#pygame.draw.rect(surface,UI_BG_COLOR,[self.height/4, self.width, self.height*3/4, self.width*3/4])
		"""


		text_surf = self.font.render(str(int(exp)),False,[255, 0, 0])
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
		"""
		#text_surf = self.font.render("hola",False,[255, 0, 0])
		#text_rect = text_surf.get_rect(topleft=[self.rect[0], self.rect [1]])
		title_surf = self.font.render(name,False,[0, 0, 0])
		title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 0))
		#pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		#pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
		if self.index == selection_num:
			pygame.draw.rect(surface,[255, 255, 0], self.rect, 0, 10)
			pygame.draw.rect(surface,[255, 255, 0], self.rect, 3, 10)
		else:
			pygame.draw.rect(surface,[255, 0, 0],self.rect, 0, 10)
			pygame.draw.rect(surface,[255, 0, 0],self.rect, 3, 10)
		surface.blit(title_surf,title_rect)
		#self.display_names(surface,name,cost,self.index == selection_num)
		#self.display_bar(surface,value,max_value,self.index == selection_num)



		