# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0,
	"arbustos": -10,
	"terreno": 0,
	"Arboles": 0
	}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 100
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 20

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#000000'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# Dialogue Box
DIALOG_X = 120
DIALOG_Y = 660
DIALOG_TEXT_SIZE = 30
DIALOG_TEXT_COLOR = [0, 0, 0]
DIALOG_BG_COLOR = (255, 240, 210)
DIALOG_BORDER_COLOR = (10, 10, 10)
DIALOG_BORDER_SIZE = 5
DIALOG_RECT_WIDTH = 1000
DIALOG_RECT_HEIGHT = 80
DIALOG_RECT_RADIUS = 10
DIALOG_BUTTON_SIZE = 30
DIALOG_BUTTON_COLOR = (125, 125, 125)
DIALOG_BUTTON_X = 1085
DIALOG_BUTTON_Y = 680

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

# enemy
monster_data = {
	'conejo': {'health': 100,'exp':100,'damage':0,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360, 'can_dialogue': False, 'dialogue' : []},
	'unicornio': {'health': 100,'exp':110,'damage':0,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350, 'can_dialogue': False, 'dialogue' : []},
	'lobo': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/wolf-howl.mp3', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'ardilla': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/wolf-howl.mp3', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'ninja': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/kung-fu-yell.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'pollo': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/pollitos-chiken.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'ninja_boss': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/pollitos-chiken.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'bandido': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/yee-haw.mp3', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
    'compinche_eugenio': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : ['Te vamos a aniquilar, haaa !']},
    'soldado': {'health': 70,'exp':120,'damage':0,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300, 'can_dialogue': False, 'dialogue' : []},
}



NPC_DATA = {
 	"27" : { 
 		"name": "Evaristo",
 		"let_move" : True,
 		"dialogue": [
 			"Hola. Mi nombre es Evaristo, llevo muchos años viviendo en este pueblo. Parece que vas a Pueblo Prospero en búsqueda de Yukacoins... ",
 			"Ten cuidado, hay animales peligrosos en el camino."
 		]
 	},
 	"34" : { 
 		"name": "Guardia",
 		"let_move" : True,
 		"dialogue": [
 			"Oh, he visto tu pelea con los lobos. Pude haberte ayudado, pero no quise, prefiero observar y servir al Lord desde la distancia.",
 		]
 	},
 	"47" : { 
 		"name": "Eugenio",
 		"let_move" : False,
 		"dialogue": []
 	},
 	"28" : { 
 		"name": "Porroncho",
 		"let_move" : True,
 		"dialogue": [
 			"Oye , si tu , quieres que te cuente un chiste , si tienes cara de querer alli va! ",
 			"Como estornudan los tomates .....",
 			"Ketchup.",
 			"jajajajajajajjaja.",
 			"¿ Has escuchado este chiste antes ?",
 			"Seguro alguien ya me lo ha copiado."
 		]
 	},
 	"29" : { 
 		"name": "Manolo",
 		"let_move" : True,
 		"dialogue": [
 			"2+2 eraaaaa , eraaaaaa...",
 			"Ah me has interrumpido insolente estoy aprendiendo matematicas...",
 			"hace poco paso un sabio por aqui y nos motivo a aprender matemáticas, ahora no me rendire !"
 			"a este paso podré dentro de poco resolver uno de los problemas del milienio y ganarme 1 millon de Yucacions "
 			
 		]
 	},
 	"35" : { 
 		"name": "Isidora",
 		"let_move" : True,
 		"dialogue": [
 			"Hola, buenos dias !",
 			"Soy amiga de Marti, el es mi esritor favorito...",
 			"Si lo ves dile por favor que lo quiero ver urgentemente al parecer el Lord a enviado a alguien a cazar animales del bosque.",
 			"Debemos detener a ese rufian."
 		]
 	},
 	 "36" : { 
 		"name": "Lubina",
 		"let_move" : True,
 		"dialogue": [
 			"Dicen que un gran sabio se encuentra en el bosque no puedo esperar para ir a conocerlo.",
 		]
 	},
	 "37" : { 
 		"name": "Raimunda",
 		"let_move" : True,
 		"dialogue": [
 			"Que te parece mi jardin he puesto mucho esfuerzo en él, espero que estas bellas flores le alegren la vida a todos los que la vean.",
 			
 		]
 	},
	 "42" : { 
 		"name": "Poderoso señor del castillo",
 		"let_move" : True,
 		"dialogue": [
 			"Quien Eres, ¿Un nuevo mendigo en mi ciudad.?",
 		]
 	},
	 "49" : { 
 		"name": "Patroclo",
 		"let_move" : True,
 		"dialogue": [
 			"Esto no me lo enseñaron en la academia de ninjas...",
 		]
 	},
	 "15" : { 
 		"name": "Jose Marti",
 		"let_move" : True,
 		"dialogue": [
 			"Hola, buenos me llamo Marti , y me entristece ver que vienes dispuesto a cazar estos pobres animalitos !",
 			"Cualquier daño que causemos a estos seres vivos es injusto; por favor, se responsable y respetuoso con el entorno natura",
 			"La naturaleza inspira, cura, consuela, fortalece y prepara para la virtud al hombre. ",
 			"Espero puedas reflexionar sobre tus acciones "
 		]
 	},
	 "48" : { 
 		"name": "Jose Marti",
 		"let_move" : True,
 		"dialogue": [
 			"¿ Como es posible que no sepas calcular ?",
 			"Veras como los conocimientos vendran a ti y seras una de las personas mas sabias por estos lugares."
 		]
 	},
}



# Esta data es para guardar las misiones
# El campo npc_name es para saber con que npc esta hablando el player
# El cmapo npc_dialogue es el que contiene
# el dialogo que va a decicir el npc
# 
# El player cuando se acerca a un npc primero se revisa
# si el npc esta aqui en las misiones
# si esta en las misioes renderiza el dialogo de las misiones
# si no renderiza el de el npc por defecto
mision_data = [
	{
		"id": "1",
		"name": "Misión 1",
		"obj": "Conseguir medicina para mamá.",
		"npc_id": "",
		"npc_dialogue": [],
		"is_completed": False,
		"yukas": 0

	},
	{
		"id": "2",
		"name": "Misión 2",
		# Nombre de la mision
		"obj": "Matar Indefensos animalitos del Bosque.",
		# Nombre del npc que da la mision
		"npc_id": "47",
		# dialogo que habla el npc para dar la mision
		"npc_dialogue": [
			"No te conozco, pero tienes cara de venir mendigando Yukacoins; estás de suerte.", 
 			"Me llamo Eugenio, dirijo este lugar para nuestro señor y quizás tenga un trabajo para ti.",
 			"Gracias a que apareciste nuestro Lord podrá tener los animales del bosque como trofeo (y así no tendré que ir yo)...", 
 			"ve al bosque… por cada animal aniquilado obtendrás algunas monedas… Animales tontos, no hacen más que estorbar. "
		],

		"is_completed": False,
		"yukas": 50

	},
	{
		"id": "3",
		"name": "Misión 3",
		"obj": "Terminar con los problemáticos bandidos.",
		"npc_id": "",
		"npc_dialogue": [],
		"is_completed": False,
		"yukas": 50

	},
	{
		"id": "4",
		"name": "Misión 4",
		"obj": "Ajustar cuentas.",
		"npc_id": "",
		"npc_dialogue": [],
		"is_completed": False,
		"yukas": 100
	},
	{
		"id": "5",
		"name": "Misión 5",
		"obj": "Liberar al pueblo del yugo del lord.",
		"npc_id": "",
		"npc_dialogue": [],
		"is_completed": False,
		"yukas": 100

	}
 ]