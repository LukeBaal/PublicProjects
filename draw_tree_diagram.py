import pygame as pyg
import math


pyg.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (128, 191, 255)
LEFT = 1
FILE = "tree-diagram.txt"
tree = open(FILE, "w")
# Window size
SIZE = (1121, 485)

# Font info
FONT = pyg.font.SysFont('Calibri', 22, True, False)


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


class Node:
    # Give grid coords, radius, and value for the node
    def __init__(self, coord=[0, 0], value="", radius=15, color=[0, 0, 0]):
        self.screen = screen
        self.color = color
        self.value = value
        self.radius = radius
        self.width = 1
        self.x = coord[0]
        self.y = coord[1]
        self.top_y = self.y - self.radius
        self.bot_y = self.y + self.radius
        self.parent = None

    def set_color(self, c):
        self.color = c

    def get_pos(self):
        return self.x, self.y

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def set_parent(self, parent):
        self.parent = parent

    def get_x(self):
        return self.x

    def get_bot_y(self):
        return self.bot_y

    def draw(self):
        pyg.draw.circle(self.screen, self.color, [self.x, self.y], self.radius, self.width)
        self.screen.blit(text(self.value, self.color), [self.x-5, self.y-7])
        if self.parent is not None:
            pyg.draw.line(self.screen, BLACK, [self.x, self.top_y], [self.parent.get_x(), self.parent.get_bot_y()], 1)


def get_x(r):
    return (MARGIN + WIDTH)*r + MARGIN + WIDTH/2


def get_y(cl):
    return (MARGIN + HEIGHT)*cl + MARGIN + HEIGHT/2


nodes = []
active = None
while not done:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            print "user asked to quit"
            done = True

        # When a key is pressed, create a node at mouse location with the key pressed as the value
        elif event.type == pyg.KEYDOWN:
            if event.key != pyg.K_DELETE:
                pos = pyg.mouse.get_pos()
                row = pos[0] // (WIDTH + MARGIN)
                column = pos[1] // (HEIGHT + MARGIN)

                nodes.append(Node([get_x(row), get_y(column)], pyg.key.name(event.key).upper()))
                tree.write(nodes[-1].value)
                # If another node is active, set it as parent for new node
                if active is not None:
                    nodes[-1].set_parent(active)

            else:
                nodes = []

        # When a node is clicked, activate or deactivate as needed
        elif event.type == pyg.MOUSEBUTTONDOWN:
            pos = pyg.mouse.get_pos()
            row = pos[0] // (WIDTH + MARGIN)
            col = pos[1] // (HEIGHT + MARGIN)

            x_pos = get_x(row)
            y_pos = get_y(col)

            for node in nodes:
                if node.get_pos() == (x_pos, y_pos):
                    if event.button == LEFT and active is None:
                        node.set_color(GREEN)
                        active = node
                    else:
                        node.set_color(BLACK)
                        active = None

    screen.fill(BLACK)
    for row in range(21):
        for column in range(9):
            pyg.draw.rect(screen, LIGHT_BLUE, [get_x(row) - WIDTH/2, get_y(column) - HEIGHT/2, WIDTH, HEIGHT])

    for item in nodes:
        item.draw()

    pyg.display.flip()

    clock.tick(60)

pyg.quit()
