import pygame as pyg
pyg.init()
LIGHT_BLUE = (128, 191, 255)
BLACK = [255, 255, 255]
LEFT = 1
FILE = "tree-diagram.txt"
tree_file = open(FILE, "w")
# Window size
SIZE = (1121, 485)

# Font info
FONT = pyg.font.SysFont('Arial', 22, True, False)


def text(txt="", color=[0, 0, 0]):
    return FONT.render(txt, True, color)


screen = pyg.display.set_mode(SIZE)

# Grid System
grid = [[0 for row in range(9)] for column in range(21)]
WIDTH = 45
HEIGHT = 45
MARGIN = 8

# Set Window Title
pyg.display.set_caption("Tree Diagram")

# Keep Window open
done = False

clock = pyg.time.Clock()

def get_x(r):
    return (MARGIN + WIDTH)*r + MARGIN + WIDTH/2


def get_y(cl):
    return (MARGIN + HEIGHT)*cl + MARGIN + HEIGHT/2
    

class Node():
	def __init__(self, value, xy_pos, c=[0, 0, 0]):
		self.value = value
		self.left = None
		self.right = None
		self.x = xy_pos[0]
		self.y = xy_pos[1]
		self.radius = 15
		self.width = 1
		self.color = c
 
	
	def get_value(self):
		return self.value
	
	def set_left(self, left):
		self.left = left
		# draw line from this node to new child
	
	def set_right(self, right):
		self.right = right
		# draw line from this node to new child
	
	def get_color(self):
		return self.color
		
	def get_pos(self):
		return [self.x, self.y]
		
	def get_radius(self):
		return self.radius
	
	def get_width(self):
		return self.width
		
	def get_value(self):
		return self.value
	
	def get_top_pos(self):
		return [self.x, self.y - self.radius]
		
	def get_bot_pos(self):
		return [self.x, self.y + self.radius]
		

class Tree():
	def __init__(self, s=screen):
		self.top = None
		self.ls = []
		self.screen = s
	
	def is_empty(self):
		return self.top is None
	
	def make_tree(self, ls, active=None, side="top"):
		op = ls[1]
		left = ls[0]
		right = ls[2]
		
		if side == "top":
			self.top = op
		elif side == "left":
			active.set_left(op)
		elif side == "right":
			active.set_right(op)
		
		active = op
		
		if len(left) > 1:
			self.make_tree(left, active, "left")
		else:
			self.active.set_left(left)
		
		if len(right) > 1:
			self.make_tree(right, active, "right")
		else:
			self.active.set_right(right)
			self.ls.append(op, left, right)
	
	def draw_leaf(self, leaf):
		pyg.draw.circle(self.screen, leaf.get_color(), leaf.get_pos(), leaf.get_radius(), leaf.get_width())
		self.screen.blit(text(leaf.get_value(), leaf.get_color()), leaf.get_pos())
		
	def draw_leaves(self, ls):
		parent = ls[0]
		left = ls[1]
		right = ls[2]
		
		# Draw left child node & attach to parent
		self.draw_leaf(left)
		pyg.draw.line(self.screen, left.get_color(), left.get_top_pos(), parent.get_bot_pos())
		
		# Draw right child node & attach to parent
		sself.draw_leaf(right)
		pyg.draw.line(self.screen, right.get_color(), right.get_top_pos(), parent.get_bot_pos())
	
	#def set_top(se;lf
			
pyg.quit()
tree_file.close()
