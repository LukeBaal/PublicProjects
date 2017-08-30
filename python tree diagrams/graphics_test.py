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

size = (255, 255)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
screen = pyg.display.set_mode(size)
LEFT = 1
RIGHT = 3

grid = [[0 for row in range(10)] for column in range(10)]
grid[1][5] = 1

#Set Window Title
pyg.display.set_caption("Grid")

#Keep Window open
done = False

clock = pyg.time.Clock()

while not done:
    for event in pyg.event.get():
      if event.type == pyg.QUIT:
        print "user asked to quit"
        done = True

      elif event.type == pyg.KEYDOWN:
        if event.key == pyg.K_q:
          pos = pyg.mouse.get_pos()

          column = pos[0] // (WIDTH + MARGIN)
          row = pos[1] // (WIDTH + MARGIN)
          grid[row][column]=1
        elif event.key == pyg.K_w:
          pos = pyg.mouse.get_pos()

          column = pos[0] // (WIDTH + MARGIN)
          row = pos[1] // (WIDTH + MARGIN)
          grid[row][column]=0

      elif event.type == pyg.MOUSEBUTTONDOWN:
        if event.button == LEFT:
          pos = pyg.mouse.get_pos()

          column = pos[0] // (WIDTH + MARGIN)
          row = pos[1] // (WIDTH + MARGIN)
          grid[row][column]=1
        elif event.button == RIGHT:
          pos = pyg.mouse.get_pos()

          column = pos[0] // (WIDTH + MARGIN)
          row = pos[1] // (WIDTH + MARGIN)
          grid[row][column]=0

	
      screen.fill(BLACK)
      # Drawing Code here
      for row in range(10):
        for column in range(10):
          color = WHITE
          if grid[row][column] == 1:
            color = GREEN
          pyg.draw.rect(screen, color, [(MARGIN + WIDTH)*column + MARGIN, (MARGIN + HEIGHT)*row + MARGIN, WIDTH, HEIGHT])
          
        
	
	
      pyg.display.flip()
	
      #White out screen
      #screen.fill(WHITE)
	
      #pyg.display.flip()

      clock.tick(60)

pyg.quit()
