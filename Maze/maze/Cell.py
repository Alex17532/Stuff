class Cell:
	wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

	def __init__(self, x, y):
		self.x = x;
		self.y = y;
		self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

	def has_all_walls(self):
		return all(self.walls.values())

	def knock_down_wall(self, other, wall):
		# print("Knocking down",self.x, self.y, wall, "and other's ",other.x, other.y, Cell.wall_pairs[wall])
		self.walls[wall] = False
		other.walls[Cell.wall_pairs[wall]] = False
