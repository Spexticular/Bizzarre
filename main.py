import pygame
from time import sleepa as wait

#Initallization of pygame
pygame.init()

#QoL functions
def flp():
  pygame.display.update()

# Making the window
win = pygame.display.set_mode((1200, 752))
bg = pygame.image.load("red.jpg")
win.blit(bg, (0, 0))
flp()

# Some values
grav = 5
screen = 1
level = 1
lives = 5

# Making the player
player = pygame.image.load("player.jpg")
class player(pygame.sprite.Sprite):
  def __init__(self, color, height, width):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill((0, 255, 0))
    self.image.set_colorkey((255, 0, 0))
    
    pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(0, 0, width, height))
    
    self.rect = self.image.get_rect()
   
 all_sprites = pygame.sprite.Group()

object_ = player((255, 255, 255), 50, 70)
object_.rect.x = 400
object_.rect.y = 400

all_sprites.add(object_)

exit = True
clock = pygame.time.Clock()

while exit:
  for event in pygame.events.get():
    if event.type == pygame.QUIT():
      exit = False
  all_sprites.update()
  win.fill((0, 255, 0))
  all_sprites.draw(win)
  flp()
  clock.tick(60)
pygme.quit()
