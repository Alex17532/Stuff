from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time

app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
obsidian_texture = load_texture('assets/obsidian_texture.png')
portal_texture = load_texture('assets/portal_texture.png')
ct_texture = load_texture('assets/Craftingtableblock.png')
furnace_texture = load_texture('assets/Furnaceblock.png')
snow_texture = load_texture('assets/snow_texture.png')
punch_sound   = Audio('assets/punch_sound.mp3',loop = False, autoplay = False)
nuke_sound   = Audio('assets/nuke.mp3',loop = False, autoplay = False)
block_pick = 1
window.exit_button.visible = False
def update():
	global block_pick
	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = obsidian_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = portal_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = ct_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = furnace_texture)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = snow_texture)
			if key == 'right mouse down':
				punch_sound.play()
				destroy(self)
			if held_keys['n']:
				nuke_sound.play()
				time.sleep(11)
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)
#20 60fps
for z in range(25):
	for x in range(25):
		voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
sky = Sky()
app.run()