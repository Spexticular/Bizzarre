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
speed = 5
grav = 5
screen = 1
level = 1
lives = 5
playersprite = pygame.image.load('player.png')
isjump = False
isfall = False

# Making the player
class player(object):
  def __init__(self):
    self.image = playersprite
    self.xcor = 0
    self.ycor = 0
    self.rect = self.image.get_rect()
    self.rect.topleft = [self.xcor, self.ycor]
  def move(self):
    # This variable returns true on whatever key is currently being pressed
    key = pygame.key.get_pressed()
    # Checking if any directional keys that we're using to control the plater are being held
    if key[pygame.K_RIGHT]:
      self.x += speed
    if key[pygame.K_LEFT]:
      self.x -= speed
    if isfall:
      self.y += grav
flp()
