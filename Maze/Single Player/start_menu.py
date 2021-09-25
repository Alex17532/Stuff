from ursina import *
from scene import *

class MenuButton(Button):
	def __init__(self, position, text, scale=(0.7,0.06), texture='../icons/button'):
		super().__init__(
			parent=camera.ui,
			position=position,
			model='quad',
			texture=texture,
			scale=scale,
			color=color.white,
			text=text,
		)



def start_game():
	background = Entity(model='quad', texture='shore', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.white)
	icon = Entity(parent=camera.ui, model='quad', texture='../icons/maze-game', position=(0,0.2,0), scale=(1.2, 0.3))

	btn_start = MenuButton(
		position=(0,-0.15,0), 
		text='Start Game',
	)

	btn_level = MenuButton(
		position=(0,-0.23,0), 
		text='Level 3', 
		scale=(0.6,0.06), 
		texture='../icons/btn_level'
	)

	btn_level_dec = MenuButton(
		position=(-0.32,-0.23,0), 
		text="<", 
		texture='../icons/btn_level_dec', 
		scale=(0.05,0.06)
	)

	btn_level_inc = MenuButton(
		position=(0.32,-0.23,0), 
		text=">", 
		texture='../icons/btn_level_inc', 
		scale=(0.05,0.06)
	)

	btn_quit = MenuButton(
		position=(0,-0.31,0), 
		text='Quit'
	)

	def start():
		level = int(btn_level.text.split()[1])
		scene.clear()
		print("level =", level)
		draw_maze(level)

	def decrease_level():
		text = btn_level.text
		level = int(text.split()[1])
		if(level > 3): btn_level.text = f'Level {level-1}'


	def increase_level():
		text = btn_level.text
		level = int(text.split()[1])
		btn_level.text = f'Level {level+1}'


	btn_level_dec.on_click = decrease_level
	btn_level_inc.on_click = increase_level
	btn_quit.on_click = application.quit
	btn_start.on_click = start



if __name__ == '__main__':
	from ursina import *
	app = Ursina()

	Text.default_font = 'consola.ttf'
	Text.size = 0.03
	draw_menu_btns()

	app.run()

