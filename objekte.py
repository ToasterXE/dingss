import pygame
import os
#from level import gutereSprites

slowness_potionImg = pygame.image.load(os.path.join("dateien", "slowness_potion.png"))
speed_potionImg = pygame.image.load(os.path.join("dateien","speed_potion.png"))
bombe_objektImg = pygame.image.load(os.path.join("dateien","bombe_objekt.png"))

class bombe_objekt(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = bombe_objektImg
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)

    def delete(self):
        self.kill()

class slowness_potion(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = slowness_potionImg
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)

    def delete(self):
        self.kill()

class speed_potion(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = speed_potionImg
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)

    def delete(self):
        self.kill()
