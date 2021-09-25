from Cell import *
import random
from PIL import Image, ImageDraw


class Maze:
	def __init__(self, n):
		self.n = n
		self.maze_map = [[Cell(x, y) for y in range(n)] for x in range(n)]
		self.make_maze()
		self.draw()


	def cell_at(self, x, y):
		return self.maze_map[x][y]

	def find_valid_neighbour(self, cell):
		delta = [('W', (-1, 0)),
				 ('E', (1, 0)),
				 ('S', (0, 1)),
				 ('N', (0, -1))]
		neighbours = []

		for direction, (dx, dy) in delta:
			x2, y2 = cell.x+dx, cell.y+dy
			if(0 <= x2 < self.n) and (0 <= y2 < self.n):
				neighbour = self.cell_at(x2, y2)
				if neighbour.has_all_walls():
					neighbours.append((direction, neighbour))
		return neighbours


	def make_maze(self):
		n = self.n * self.n
		cell_stack = []			# contains final maze
		current_cell = self.cell_at(0, 0)
		nv = 1					# number of visited cells

		while nv < n:
			neighbours = self.find_valid_neighbour(current_cell)

			if not neighbours:
				current_cell = cell_stack.pop()
				continue

			direction, next_cell = random.choice(neighbours)
			current_cell.knock_down_wall(next_cell, direction)
			cell_stack.append(current_cell)
			current_cell = next_cell
			nv += 1

		self.cell_at(0, 0).walls['N'] = False
		self.cell_at(self.n-1, self.n-1).walls['S'] = False


	def draw(self):
		width = 50
		size = self.n
		img = Image.new("RGB", (width*size, width*size), (255, 255, 255))
		draw = ImageDraw.Draw(img)

		for row in self.maze_map:
			for cell in row:

				walls = cell.walls
				x = cell.x * width
				y = cell.y * width

				if walls['N']: draw.line([(x, y), (x+width, y)], fill=0, width=10)
				if walls['E']: draw.line([(x+width, y), (x+width, y+width)], fill=0, width=10)
				if walls['S']: draw.line([(x+width, y+width), (x, y+width)], fill=0, width=10)
				if walls['W']: draw.line([(x, y+width), (x, y)], fill=0, width=10)

		img.save("maze-layout.jpg")
		print("IMAGE SAVED.")
