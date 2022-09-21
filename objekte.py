#die klassen für objekte sind in einer anderen datei, damit es übersichtlicher ist
import pygame
import os
from bilder import *

class bombe_boost(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = bombeboost_Img
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)

    def delete(self):
        self.kill()

class bombe_objekt(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = bombe_objektImg
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)  #get rekt du kek

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

class hp_boost(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = hp_boostImg
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
    def delete(self):
        self.kill()