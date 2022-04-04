import pygame
from time import sleep as wait

#Initallization of pygame
pygame.init()

#QoL functions
def flp():
  pygame.display.update()

# Making the window
win = pygame.display.set_mode((1200, 752))
win.fill((0, 0, 0))
bg = pygame.image.load("red.jpg")
win.blit(bg, (0, 0))
flp()

# Some values
grav = 5
screen = 1
level = 1
lives = 5

# Making the player
player = pygame.image.load("player.png")
class player(pygame.sprite.Sprite):
  def __init__(self):
      self.xcor = 100
      self.ycor = 150
      self.image = pygame.image.load('player.png')
      self.Rect(self.xcor, self.ycor, 100, 100)
flp()
