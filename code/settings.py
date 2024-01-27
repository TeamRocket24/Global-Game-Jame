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
DIALOG_Y = 640
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
	'squid': {'health': 100,'yuka':3,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'yuka':1,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'yuka':2,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'yuka':1,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}



npc_data = {
 	"la_pura" : { 
 		"graphic": "../graphics/test/player.png",
 		"dialogue": [
 			"Hola hijito como estas aaaaaaaa a asdajs hdjash djahsjkhd ashda sgdasdasdasgdfa hsgdfas dfgasdgfasg dasf dhgafshgdfas fdha fsgdahsfhdafshgd",
 			"espero que hayas pasado una linda susna",
 			"tegno sueño, adios..."
 		]
 	},
 	"salinga" : { 
 		"graphic": "../graphics/test/player.png",
 		"dialogue": [
 			"Hola, buenos dias !",
 			"Soy amiga de Marti, el es mi esritor favorito",
 			"Si lo ves dile por favor que lo quiero ver urgentemente please",
 			"vale gracias, adios !."

 		]
 	}
}