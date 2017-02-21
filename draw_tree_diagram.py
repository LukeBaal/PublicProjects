import pygame as pyg
import math


pyg.init()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653

#Window size
SIZE = (710, 710)

#Font info
FONT = pyg.font.SysFont('Calibri', 22, True, False)

def text(text="", color=[0, 0, 0]):
  return FONT.render(text, True, color)
                     
screen = pyg.display.set_mode(SIZE)

#Grid System
grid = [[0 for row in range(10)] for column in range(10)]
WIDTH = 60
HEIGHT = 60
MARGIN = 10

#Set Window Title
pyg.display.set_caption("Tree Diagram")

#Keep Window open
done = False

clock = pyg.time.Clock()

class Node:
  # Give grid coords, radius, and value for the node
  def __init__(self,pos=[0, 0], value="", radius=15, color=[0, 0, 0]):
    self.screen = screen
    self.color = color
    self.value = value
    self.radius = radius
    self.width = 1
    self.x = pos[0]
    self.y = pos[1]

  def update_pos(self, x, y):
    self.x = x
    self.y = y
    
  def draw(self):
    pyg.draw.circle(self.screen, self.color, [self.x, self.y], self.radius, self.width)
    self.screen.blit(text(self.value), [self.x-5, self.y-7])

    
nodes = []
while not done:
    for event in pyg.event.get():
      if event.type == pyg.QUIT:
        print "user asked to quit"
        done = True

      elif event.type == pyg.KEYDOWN:
        if event.key != pyg.K_DELETE:
          pos = pyg.mouse.get_pos()

          row = pos[0] // (WIDTH + MARGIN)
          column = pos[1] // (HEIGHT + MARGIN)
          nodes.append(Node([(MARGIN + WIDTH)*row + MARGIN + WIDTH/2, (MARGIN + HEIGHT)*column + MARGIN + HEIGHT/2], pyg.key.name(event.key).upper()))
          #nodes[-1].update_pos((MARGIN + WIDTH)*row + MARGIN + WIDTH/2, (MARGIN + HEIGHT)*column + MARGIN + HEIGHT/2)
        else:
          nodes = []

      
      screen.fill(BLACK)
      # Drawing Code here
      for row in range(10):
       for column in range(10):
        pyg.draw.rect(screen, WHITE, [(MARGIN + WIDTH)*column + MARGIN, (MARGIN + HEIGHT)*row + MARGIN, WIDTH, HEIGHT])

      
      for item in nodes::
        item.draw()

      pyg.display.flip()

      clock.tick(60)

pyg.quit()
