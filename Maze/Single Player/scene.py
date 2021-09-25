from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

import sys
sys.path.insert(1, '../maze')
from Maze import *

wall_length = 5		# do not change, changing this might disrupt the wall creation methods.
wall_height = 3
size = 6

class Wall(Entity):
	def __init__(self, x, z, texture, color=color.red, scale_y=wall_height):
		super().__init__(
			position=(x,1.5,z),
			model='cube',
			collider='box',
			texture=texture,
			texture_scale=(1,wall_height),
			scale_y=scale_y
		)


class Sky(Entity):
	def __init__(self):
		self.sky_texture=load_texture('../textures/skybox.png')
		super().__init__(
			parent=scene,
			model='sphere',
			texture=self.sky_texture,
			scale=150,
			double_sided=True)


def createWall(x1, z1, x2, z2):
	crate = load_texture('../textures/stone.jpg')


	if x1 != x2:
		for x in range(min(x1, x2), max(x1, x2)):
			c = Wall(x, z1, texture=crate)
	if z1 != z2:
		for z in range(min(z1, z2), max(z1, z2)):
			c = Wall(x1, z, texture=crate)


def addWalls(maze, size):

	ursina_y = (size*wall_length) // 2
	ursina_x = - (size*wall_length) // 2

	for y in range(maze.n):
		ursina_x = - (size*wall_length) // 2

		for x in range(maze.n):
			cell = maze.cell_at(x, y)      

			if cell.walls['N']:
				createWall(ursina_x, ursina_y, ursina_x+wall_length, ursina_y)

			if cell.walls['E']:
				createWall(ursina_x+wall_length, ursina_y, ursina_x+wall_length, ursina_y-wall_length)
			
			if cell.walls['S']:
				createWall(ursina_x+wall_length, ursina_y-wall_length, ursina_x, ursina_y-wall_length)
			
			if cell.walls['W']:
				createWall(ursina_x, ursina_y-wall_length, ursina_x, ursina_y)

			ursina_x += wall_length
		ursina_y -= wall_length



def draw_maze(size):

	# sky_texture=load_texture('../textures/skybox.png'),
	sky = Sky()

	maze = Maze(size)
	val_floor = size * wall_length
	ground_texture = load_texture('../textures/grass.jpg')
	ground = Entity(model='plane', scale=val_floor, texture=ground_texture, texture_scale=(val_floor,val_floor), collider='box')


	max_x = - (size*wall_length) // 2
	player1 = FirstPersonController(collider='box', mouse_sensitivity=Vec2(70,70), position=Vec3(max_x+wall_length/2, -0.5, abs(max_x)-3))

	start_banner = load_texture('../textures/start_banner.png')
	finish_banner = load_texture('../textures/finish_banner.png')
	start_banner = Entity(model='quad', scale=(4,2), position=(max_x+wall_length/2, 2, abs(max_x)-1), texture=start_banner)
	finish_banner = Entity(model='quad', scale=(5, 2), position=(-(max_x+wall_length/2), 2, max_x+1),rotation=(0,180,0), texture=finish_banner)
	addWalls(maze, size)



# cube1 = Wall(-15, 15, color=color.blue, scale_y=5)
# cube2 = Wall(15, 15, color=color.black, scale_y=5)
# cube3 = Wall(15, -15, color=color.green, scale_y=5)
# cube4 = Wall(-15, -15, color=color.magenta, scale_y=5)


# BANNER :
# for now, the scale of start_banner and finish_banner are hard coded to work well with wall length of 5
# if you want to change wall length, do change the scale of start and finish banner.
