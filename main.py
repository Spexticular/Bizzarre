import pygame, webbrowser
from time import sleep as wait

#Initallization of pygame
pygame.init()

#QoL functions
def flp():
  pygame.display.update()

# Some values
speed = 5
grav = 5
screen = 1
level = 1
lives = 5
isjump = False
isfall = False
play = False

# Making the player
# Player Sprites
playersprite = pygame.image.load('player-removebg-preview.png')
playerleft = pygame.image.load('player-left-removebg-preview.png')

# Player Class
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
      self.image = playerleft
    if isfall:
      self.y += grav
# Making the main menu
def mainmenu():
  win = pygame.display.set_mode((1200, 752))
  bg = pygame.image.load('placeholder')
  win.blit(bg, (0, 0)
  
# Main game loop and a check.
if play:
  # Making the window
  win = pygame.display.set_mode((1200, 752))
  win.fill((0, 0, 0))
  bg = pygame.image.load("red.jpg")
  win.blit(bg, (0, 0))
  flp()
  # Making the player
  # Player Sprites
  playersprite = pygame.image.load('player-removebg-preview.png')
  playerleft = pygame.image.load('player-left-removebg-preview.png')

  # Player Class
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
        self.image = playerleft
      if isfall:
        if not isjump:
          self.y += grav
      if isjump:
        if not isfall:
          # Making the variables for the jump
          v=10
          m=1
          # The formula to make a smooth jump
          F = (1/2)*m*(v**2)
          # adding this value to the Y cordinate
          y -= F
          # changing the vel so that eventually you come back down
          v -= 1
          # Some shenanigans to make the jump better
          if v < 0:
            m = -1
          # Reset when jump is finished
          if v == -11:
            isjump = False
            isfall = False
            v = 10
            m = 1
    def draw(self, screen):
      screen.blit(self.image, self.rect)
  pl = player()
