import pygame
from time import sleepa as wait

#Initallization of pygame
pygame.init()

# Making the window
win = pygame.display.set_mode((1200, 752))
bg = pygame.image.load("red.jpg")
win.blit(bg, (0, 0))


#QoL functions
def flp():
  pygame.display.update()
def drawrect(x, y, width, height):
  pygame.draw.rect((x, y, width, height))
