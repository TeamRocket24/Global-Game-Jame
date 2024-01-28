class Dialogue:
	def __init__(self, dialogue, npc):
		self.index_dialogue = 0
		self.dialogue_list = dialogue
		
		self.npc_name = npc.name
		self.npc = npc

	def get_dialogue(self):
		if len(self.dialogue_list) <= self.index_dialogue and len(self.dialogue_list) > 0:
			self.index_dialogue = len(self.dialogue_list) - 1
	
		text = self.dialogue_list[self.index_dialogue]
		return text

	def has_more_dialogue(self):
		return self.index_dialogue < len(self.dialogue_list) - 1

	def is_empty(self):
		return len(self.dialogue_list) == 0

	def next_dialogue(self):
		self.index_dialogue += 1

	def close_dialogue(self, player):
		self.npc.status = "idle"
		player.set_is_dialoguing(self.npc_name, False)
		player.set_npc_dialoguing(None)
		player.set_can_move(True)
		self.npc.finish_dialogue = True