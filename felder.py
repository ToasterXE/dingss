import pygame
from einstellungen import *
import os
from objekte import * 
import random
from bilder import *

#hier fangen die klassen für die Felder an
bombe_verstärkung = 0
bombe_verstärkunge = 0
class border(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = borderImg
        self.image = pygame.transform.scale(self.image, (feld_pixel, feld_pixel),)
        self.rect = self.image.get_rect(topleft = pos)
        self.type = "grenzfeld"


class sprengbares(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = sprengbaresImg
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pos
        self.type = "sprengbares"

    def delete(self):
        self.replace(random.randint(0,100))
        self.kill()

    def replace(self,nummer):   #wichtige sachen
        global bombe_verstärkunge
        if nummer >= 95:
            slowness_potion(self.pos,[gutereSprites, slownessSprites])
        if nummer >= 10 and nummer < 20:
            speed_potion(self.pos, [gutereSprites, speedSprites])
        if nummer >= 0 and nummer < 8:
            bombe_objekt(self.pos,[gutereSprites, bombenobjekteSprites])
        if nummer >= 20 and nummer < 25:
            hp_boost(self.pos, [gutereSprites, hpboostSprites])
        if bombe_verstärkunge < 12:
            if nummer >= 25 and nummer < 30:
                bombe_boost(self.pos, {gutereSprites, bombeboostSprites})
                bombe_verstärkunge += 1


class spawnfeld(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "spawn.png")),(feld_pixel,feld_pixel))
        self.rect = self.image.get_rect(topleft = pos)
        self.type = "spawnfeld"


class wegraeumbares(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = wegraeumbaresImg
        self.rect = self.image.get_rect(topleft = pos)
        self.type = "wegraeumbares"

    def delete(self):
        self.kill()