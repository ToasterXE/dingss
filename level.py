from threading import Thread
from numpy import true_divide
import pygame, os
from maps import *
from player import Player
from objekte import *
import random 
from einstellungen import *
from felder import * 
from infofeld import *
from bilder import *
from sdings import sdtListeNamen

#globale variablen
bombenanzahl = 3
explosionsListe = []
gegner = 0
gegner_eliminiert = 0
explosionsmap = []
pygame.font.init()
font40 = pygame.font.SysFont("candara", 20)
font80 = pygame.font.SysFont("candara", 40)
font120 = pygame.font.SysFont("candara", 60)


#nur für ein "Fenster" im Level 7
class linie(pygame.sprite.Sprite):
    def __init__(self, groups, topleft, width, height):
        super().__init__(groups)
        self.image = pygame.transform.scale(leerImg,(width, height))
        self.rect = self.image.get_rect(topleft = topleft)


#nur für ein "Fenster" im Level 7
class bild(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = bildImg
        self.rect = self.image.get_rect(topleft = pos)
        self.linie_oben = linie(groups, self.rect.topleft, self.rect.width, 8)
        self.linie_rechts = linie(groups, (self.rect.right - 8, self.rect.top), 8, self.rect.height)
        self.linie_links = linie(groups, (self.rect.left, self.rect.top), 8, self.rect.height)
        self.linie_unten = linie(groups, (self.rect.left, self.rect.bottom - 8), self.rect.width, 8)
        self.linie_oben_mitte = linie(groups, (self.rect.left, self.rect.top + 15), self.rect.width, 8)
        self.linie_rechts_mitte = linie(groups, (self.rect.right - 15 - 8, self.rect.top), 8, self.rect.height)
        self.linie_links_mitte = linie(groups, (self.rect.left + 15, self.rect.top), 8, self.rect.height)
        self.linie_unten_mitte = linie(groups, (self.rect.left, self.rect.bottom - 15 - 8), self.rect.width, 8)


class potion_counter(pygame.sprite.Sprite): #keine sprites
    def __init__(self,groups,speed):
        super().__init__(groups)
        self.wert = 0
        self.speed = speed
    def count(self):
        self.wert += 1
    def delete(self):
        self.kill()

def neben_explosion(pos, wert, num = 0):
    if pos.x + wert[0] < len(explosionsmap) and pos.y + wert[1] < len(explosionsmap[0]):
        # print("e",pos.x+wert[0], pos.y+wert[1])
        if explosionsmap[int(pos.x + wert[0])][int(pos.y + wert[1])] == 8:
            return True
        else:
            if num == 3:
                return False
            e = wert[0]
            wert[0] = wert[1]
            wert[1] = e *-1
            return neben_explosion(pos,wert, num+1)

class expAnimation(pygame.sprite.Sprite):    
    def __init__(self,groups,pos,map,damage, num):
        super().__init__(groups)
        self.levelmap = map
        self.pos = pos
        self.end = False
        self.mapPos = pygame.math.Vector2(int(pos.y/feld_pixel),int(pos.x/feld_pixel))
        # print(int(pos.y/feld_pixel), len(explosionsmap), int(pos.x/feld_pixel), len(explosionsmap[0]))
        if int(pos.y/feld_pixel) >= len(explosionsmap) or int(pos.x/feld_pixel) >= len(explosionsmap[0]):
            self.kill()
        else:
            #self.feld = explosionsmap[int(self.mapPos.x)][int(self.mapPos.y)]
            if explosionsmap[int(self.mapPos.x)][int(self.mapPos.y)] == 1 or explosionsmap[int(self.mapPos.x)][int(self.mapPos.y)] == 8:  #keine explosionen auf unveränderbaren feldern
                self.kill()
            if num > 0:
                if not neben_explosion(self.mapPos, [1,0]):
                #if not (explosionsmap[int(self.mapPos.x+1)][int(self.mapPos.y)] == 8 or explosionsmap[int(self.mapPos.x)][int(self.mapPos.y+1)] == 8 or explosionsmap[int(self.mapPos.x-1)][int(self.mapPos.y)] == 8 or explosionsmap[int(self.mapPos.x)][int(self.mapPos.y-1)] == 8):
                    # print("E")
                    self.kill()

            self.feld = explosionsmap[int(self.mapPos.x)][int(self.mapPos.y)]
            explosionsmap[int(self.mapPos.x)][int(self.mapPos.y)] = 8

        #explosionsListe.append(self.pos)

        self.sprites = []
        self.sprites.append(explosionsImg1)
        self.sprites.append(explosionsImg2)
        self.sprites.append(explosionsImg4)
        self.sprites.append(explosionsImg5)
        self.sprites.append(explosionsImg7)
        self.sprites.append(explosionsImg8)
        self.sprites.append(explosionsImg10)
        self.sprites.append(explosionsImg11)
        self.damage = damage
        self.counter = 0
        self.image = nichtsImg
        self.rect = self.image.get_rect(topleft = pos)        

    def animate(self):
        self.counter += 0.2

        if self.counter >= len(self.sprites):
            self.levelmap[int(self.mapPos.x)][int(self.mapPos.y)] = self.feld
            self.kill()

        else:
            self.image = self.sprites[int(self.counter)]


bombenSprites_bilder = [bombeImg1,bombeImg2,bombeImg3,bombeImg4,bombeImg5,bombeImg6,bombeImg7,bombeImg8,bombeImg9,bombeImg10,bombeImg11,bombeImg12]

bomben_verstärkung1Sprites = [bombeImg1_verstärkung1,bombeImg2_verstärkung1,bombeImg3_verstärkung1,bombeImg4_verstärkung1,bombeImg5_verstärkung1,
bombeImg6_verstärkung1,bombeImg7_verstärkung1,bombeImg8_verstärkung1,bombeImg9_verstärkung1,bombeImg10_verstärkung1,bombeImg11_verstärkung1,bombeImg12_verstärkung1]

bomben_verstärkung2Sprites = [bombeImg1_verstärkung2,bombeImg2_verstärkung2,bombeImg3_verstärkung2,bombeImg4_verstärkung2,bombeImg5_verstärkung2,
bombeImg6_verstärkung2,bombeImg7_verstärkung2,bombeImg8_verstärkung2,bombeImg9_verstärkung2,bombeImg10_verstärkung2,bombeImg11_verstärkung2,bombeImg12_verstärkung2]

bomben_verstärkung3Sprites = [bombeImg1_verstärkung3,bombeImg2_verstärkung3,bombeImg3_verstärkung3,bombeImg4_verstärkung3,bombeImg5_verstärkung3,
bombeImg6_verstärkung3,bombeImg7_verstärkung3,bombeImg8_verstärkung3,bombeImg9_verstärkung3,bombeImg10_verstärkung3,bombeImg11_verstärkung3,bombeImg12_verstärkung3]

bomben_verstärkung4Sprites = [bombeImg4_verstärkung1,bombeImg2_verstärkung4,bombeImg3_verstärkung4,bombeImg4_verstärkung4,bombeImg5_verstärkung4,
bombeImg6_verstärkung4,bombeImg7_verstärkung4,bombeImg8_verstärkung4,bombeImg9_verstärkung4,bombeImg10_verstärkung4,bombeImg11_verstärkung4,bombeImg12_verstärkung4]

explosionsSprites = [explosionsImg1,explosionsImg2,explosionsImg4,explosionsImg5,explosionsImg7,explosionsImg8,explosionsImg10,explosionsImg11]


class bombe_verstärkt4(pygame.sprite.Sprite):
    def __init__(self, groups, pos, levelmap):
        super().__init__(groups)
        self.pos = pos
        self.levelmap = levelmap
        self.counter = 0
        self.bombenSprites = bomben_verstärkung4Sprites
        self.image = self.bombenSprites[self.counter]
        self.rect = self.image.get_rect(topleft = pos)
        self.explosionsSprites = explosionsSprites
        self.counter2 = 0
        self.damage = 3
        self.explosionen = pygame.sprite.Group()
        self.exploding = False
        self.explosionsanimation = False
    
    def explode(self):
        self.exploding = True
    def update(self):
        global bombenanzahl
        if self.exploding:
            self.counter += 0.2

        if int(self.counter) >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False
            i = 0
            while i <= 88:
                expAnimation([gutereSprites, explosionSprites, self.explosionen],
                (self.pos + (sdtListeNamen[i].xabstand * feld_pixel, sdtListeNamen[i].yabstand * feld_pixel)),self.levelmap,self.damage,sdtListeNamen[i].num)
                i += 1
        if self.exploding:
            self.image = self.bombenSprites[int(self.counter)]
        
        if self.explosionsanimation:
            self.counter2 += 0.2
            for explosion in self.explosionen:
                explosion.animate()
                
        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            
        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]

class bombe_verstärkt3(pygame.sprite.Sprite):
    def __init__(self, groups, pos, levelmap):
        super().__init__(groups)
        self.pos = pos
        self.levelmap = levelmap
        self.counter = 0
        self.bombenSprites = bomben_verstärkung3Sprites
        self.image = self.bombenSprites[self.counter]
        self.rect = self.image.get_rect(topleft = pos)
        self.explosionsSprites = explosionsSprites
        self.counter2 = 0
        self.damage = 3
        self.explosionen = pygame.sprite.Group()
        self.exploding = False
        self.explosionsanimation = False
    def explode(self):
        self.exploding = True
    def update(self):
        global bombenanzahl
        if self.exploding:
            self.counter += 0.2

        if int(self.counter) >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False
            i = 0
            while i <= 36:
                expAnimation([gutereSprites, explosionSprites, self.explosionen],
                (self.pos + (sdtListeNamen[i].xabstand * feld_pixel, sdtListeNamen[i].yabstand * feld_pixel)),self.levelmap,self.damage,sdtListeNamen[i].num)
                i += 1
        if self.exploding:
            self.image = self.bombenSprites[int(self.counter)]
        
        if self.explosionsanimation:
            self.counter2 += 0.2
            for explosion in self.explosionen:
                explosion.animate()
                
        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            
        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]

class bombe_verstärkt2(pygame.sprite.Sprite):
    def __init__(self, groups, pos, levelmap):
        super().__init__(groups)
        self.pos = pos
        self.levelmap = levelmap
        self.counter = 0
        self.bombenSprites = bomben_verstärkung2Sprites
        self.image = self.bombenSprites[self.counter]
        self.rect = self.image.get_rect(topleft = pos)
        self.explosionsSprites = explosionsSprites
        self.counter2 = 0
        self.damage = 2
        self.explosionen = pygame.sprite.Group()
        self.exploding = False
        self.explosionsanimation = False
    
    def explode(self):
        self.exploding = True
    def update(self):
        global bombenanzahl
        if self.exploding:
            self.counter += 0.2

        if int(self.counter) >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False
            i = 0
            while i <= 20:
                expAnimation([gutereSprites, explosionSprites, self.explosionen],
                (self.pos + (sdtListeNamen[i].xabstand * feld_pixel, sdtListeNamen[i].yabstand * feld_pixel)),self.levelmap,self.damage,sdtListeNamen[i].num)
                i += 1
        if self.exploding:
            self.image = self.bombenSprites[int(self.counter)]
        
        if self.explosionsanimation:
            self.counter2 += 0.2
            for explosion in self.explosionen:
                explosion.animate()
                
        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            
        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]

class bombe_verstärkt1(pygame.sprite.Sprite):
    def __init__(self, groups, pos, levelmap):
        super().__init__(groups)

        self.counter = 0
        self.bombenSprites = bomben_verstärkung1Sprites
        self.image = self.bombenSprites[self.counter]
        self.rect = self.image.get_rect(topleft = pos)
        self.explosionsSprites = explosionsSprites
        self.counter2 = 0
        self.pos = pos
        self.levelmap = levelmap
        self.exploding = False
        self.explosionsanimation = False
        self.damage = 2
        self.explosionen = pygame.sprite.Group()

    def explode(self):
        self.exploding = True

    def update(self):
        global bombenanzahl
        if self.exploding:
            self.counter += 0.2
            
        
        if self.counter >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False

            i = 0
            while i <= 4:
                expAnimation([gutereSprites, explosionSprites, self.explosionen],
                (self.pos + (sdtListeNamen[i].xabstand * feld_pixel, sdtListeNamen[i].yabstand * feld_pixel)),self.levelmap,self.damage,sdtListeNamen[i].num)
                i += 1
        if self.exploding:
            self.image = self.bombenSprites[int(self.counter)]

        if self.explosionsanimation:
            self.counter2 += 0.2
            for explosion in self.explosionen:
                explosion.animate()


        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            
        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]

class bombe(pygame.sprite.Sprite):
    def __init__(self, groups, pos, levelmap):   #nummer argument ist nicht gebraucht
        super().__init__(groups)

        self.counter = 0
        self.bombenSprites = bombenSprites_bilder
        self.image = self.bombenSprites[self.counter]
        self.rect = (self.image.get_rect(topleft = pos))
        self.explosionsSprites = explosionsSprites

        self.counter2 = 0
        self.pos = pos
        self.levelmap = levelmap
        self.damage = 1
        
        self.exploding = False
        self.explosionsanimation = False
        self.explosionen = pygame.sprite.Group()

    def explode(self):
        self.exploding = True
        self.explosionsanimation = False


    def update(self):
        global bombenanzahl

        if self.exploding == True:
            self.counter += 0.2         #bei größeren zahlen wäre die animation sehr schnell vorbei

        if self.counter >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False
            
            i = 0
            while i <= 4:
                expAnimation([gutereSprites, explosionSprites, self.explosionen],(self.pos + (sdtListeNamen[i].xabstand * feld_pixel, sdtListeNamen[i].yabstand * feld_pixel)),self.levelmap,self.damage, sdtListeNamen[i].num)
                i += 1

        if self.exploding == True:            
            self.image = self.bombenSprites[int(self.counter)]
 
        if self.explosionsanimation == True:
            self.counter2 += 0.2
            for explosion in self.explosionen:
                explosion.animate()

        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            
        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]


#hier fangen die klassen für die gegner an

class alien1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.hit_image = alien1Img_hit
        self.image = alien1Img
        self.image_normal = alien1Img
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = random.randint(3,6)
        self.hp = 3
        self.hit = False
        self.counter = 0
        self.bild = 0
        self.type = 1

        if random.randint(1,2) == 1:
            self.speed *= -1
        
    def move(self):
        self.rect.left += self.speed
        for hinderniss in aliencollisionSprites:
            if self.rect.colliderect(hinderniss.rect):
                self.rect.left -= self.speed
                self.speed *= -1

    def delete(self):
        global gegner, gegner_eliminiert
        self.rect.left -= self.speed        
        if self.bild == 10:
            self.kill()
            gegner -= 1
            gegner_eliminiert += 1
        self.image = pygame.transform.scale(self.image,(feld_pixel - int(self.bild*3), feld_pixel - int(self.bild*3)))
        self.bild += 0.5


class bewegungsrichtung():  #für die grünen gegner
    def __init__(self, rect, speed):
        self.wert = 1
        self.Vector = pygame.math.Vector2()
        self.rect = rect
        self.rect_relevant = pygame.rect.Rect(self.rect.left - 1, self.rect.top -1, self.rect.width + 2, self.rect.height + 2)
        self.wert_collide = self.rect
        self.wert_space = pygame.math.Vector2()
        self.hinderniss_links = False
        self.hinderniss_oben = False
        self.hinderniss_rechts = False
        self.hinderniss_unten = False
        self.speed = speed
        self.zuletzt = 0
        self.schritt_counter = 0
        self.image = alien2Img_oben
        self.image_hit = alien2Img_links_hit
        self.verwirrung = False
        self.counter = 0

    def wert_check(self, wert):
        if self.wert > 4:
            self.wert -= 4

        if self.wert <= 0:
            self.wert += 4
        
        if self.verwirrung == True:
            self.Vector.x = 0
            self.Vector.y = 0
            return True

        if self.hinderniss_links == False and self.hinderniss_oben == False and self.hinderniss_rechts == False and self.hinderniss_unten == False:
            self.Vector = pygame.math.Vector2(0,1)
            return True

        

        if wert == 1:    #rechts
            self.Vector.x = 1
            self.Vector.y = 0
            if self.hinderniss_rechts == True or self.hinderniss_unten == False:
                return False
            elif self.hinderniss_unten == True:
                self.zuletzt = "rechts"
                self.image = alien2Img_unten
                self.image_hit = alien2Img_unten_hit
                return True

        if wert == 2:    #unten
            self.Vector.x = 0
            self.Vector.y = 1
            if self.hinderniss_unten == True or self.hinderniss_links == False:
                return False
            elif self.hinderniss_links == True:
                self.zuletzt = "unten"
                self.image = alien2Img_links
                self.image_hit = alien2Img_links_hit
                return True

        if wert == 3:    #links
            self.Vector.x = -1
            self.Vector.y = 0
            if self.hinderniss_links == True or self.hinderniss_oben == False:
                return False
            elif self.hinderniss_oben  == True:
                self.zuletzt = "links"
                self.image = alien2Img_oben
                self.image_hit = alien2Img_oben_hit
                return True

        if wert == 4:  #oben
            self.Vector.x = 0
            self.Vector.y = -1
            if self.hinderniss_oben == True or self.hinderniss_rechts == False:
                return False
            elif self.hinderniss_rechts == True:
                self.zuletzt = "oben"
                self.image = alien2Img_rechts
                self.image_hit = alien2Img_rechts_hit
                return True


    def update(self):       #teile dieser lösung sind nicht erforderlich
        if self.verwirrung == True:
            if self.counter % 3 == 0:
                self.e = random.randint(1,4)
                if self.e == 1:
                    self.image = alien2Img_links
                if self.e == 2:
                    self.image = alien2Img_oben
                if self.e == 3:
                    self.image = alien2Img_rechts
                if self.e == 4:
                    self.image = alien2Img_unten
            self.counter += 1

        if self.schritt_counter > 0:
            self.schritt_counter += 1
            if self.schritt_counter == feld_pixel / self.speed:
                self.schritt_counter = 0
        else:
            self.rect_relevant = pygame.rect.Rect(self.rect.left - 1, self.rect.top -1, self.rect.width + 2, self.rect.height + 2)
            self.hinderniss_links = False
            self.hinderniss_oben = False
            self.hinderniss_rechts = False
            self.hinderniss_unten = False
            self.hinderniss_ecke_links_oben = False
            self.hinderniss_ecke_links_unten = False
            self.hinderniss_ecke_rechts_oben = False
            self.hinderniss_ecke_rechts_unten = False
            self.verwirrung = False
        

            for hinderniss in aliencollisionSprites:
                if hinderniss.rect.colliderect(self.rect_relevant):
                    self.Vector = pygame.math.Vector2(0,0)
                    if hinderniss.rect.colliderect((self.rect.left, self.rect.bottom, self.rect.width / 2, 1)):
                        self.hinderniss_unten = True
                
                    if hinderniss.rect.colliderect((self.rect.right, self.rect.centery, 1, self.rect.height / 2)):
                        self.hinderniss_rechts = True
                
                    if hinderniss.rect.colliderect((self.rect.centerx, self.rect.top - 1, self.rect.width / 2, 1)):
                        self.hinderniss_oben = True
                
                    if hinderniss.rect.colliderect((self.rect.left - 1, self.rect.top, 1, self.rect.height / 2)):
                        self.hinderniss_links = True
                
                    if hinderniss.rect.collidepoint(self.rect_relevant.right, self.rect_relevant.top):
                        self.hinderniss_ecke_rechts_oben = True

                    if hinderniss.rect.collidepoint(self.rect_relevant.left, self.rect_relevant.top):
                        self.hinderniss_ecke_links_oben = True

                    if hinderniss.rect.collidepoint(self.rect_relevant.left, self.rect_relevant.bottom):
                        self.hinderniss_ecke_links_unten = True

                    if hinderniss.rect.collidepoint(self.rect_relevant.right, self.rect_relevant.bottom):
                        self.hinderniss_ecke_rechts_unten = True

                    if self.hinderniss_links == False and self.hinderniss_oben == False and self.hinderniss_rechts == False and self.hinderniss_unten == False:     #um die ecke gehen
                        if self.zuletzt == "links" and self.hinderniss_ecke_rechts_oben == True:
                            self.hinderniss_rechts = True
                            
                        elif self.zuletzt == "unten" and self.hinderniss_ecke_links_oben == True:
                            self.hinderniss_oben = True
                        
                        elif self.zuletzt == "rechts" and self.hinderniss_ecke_links_unten == True:
                            self.hinderniss_links = True

                        elif self.zuletzt == "oben" and self.hinderniss_ecke_rechts_unten == True:
                            self.hinderniss_unten = True

            if self.hinderniss_links and self.hinderniss_oben and self.hinderniss_rechts and self.hinderniss_unten:
                    self.verwirrung = True
            else:
                if self.zuletzt == "oben" and self.hinderniss_ecke_rechts_unten and (self.hinderniss_oben or self.hinderniss_links) and self.hinderniss_rechts == False:
                    self.hinderniss_oben = False
                    self.hinderniss_links = False
                    self.hinderniss_unten = True

            if self.zuletzt == "rechts" and self.hinderniss_ecke_links_unten and (self.hinderniss_oben or self.hinderniss_rechts) and self.hinderniss_unten == False:
                    self.hinderniss_oben = False
                    self.hinderniss_rechts = False
                    self.hinderniss_links = True

            if self.hinderniss_links and self.hinderniss_unten and self.hinderniss_rechts and self.zuletzt == "unten":
                    self.hinderniss_oben = False
                    self.verwirrung = False
                    #print("e")
            #if self.hinderniss_ecke_links_oben and self.hinderniss_ecke_links_oben:
             #       if  
            #print(self.verwirrung, self.zuletzt)

            self.wert += 1
            if self.wert > 4:
                self.wert -= 4

            if self.wert <= 0:
                self.wert += 4
            while self.wert_check(self.wert) == False:
                self.wert -= 1
                if self.wert > 4:
                    self.wert -= 4

                if self.wert <= 0:
                    self.wert += 4
            #print(self.wert)
            self.schritt_counter += 1


class alien2(pygame.sprite.Sprite):
    def __init__(self,pos,groups,eee):
        super().__init__(groups)

        self.image = alien2Img_unten
        self.image_normal = alien2Img_unten
        
        self.image_unten = alien2Img_unten
        self.image_rechts = alien2Img_rechts
        self.image_oben = alien2Img_oben
        self.image_links = alien2Img_links

        self.image_unten_hit = alien2Img_unten_hit
        self.image_rechts_hit = alien2Img_rechts_hit
        self.image_oben_hit = alien2Img_oben_hit
        self.image_links_hit = alien2Img_links_hit

        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = eee

        self.hit = False
        self.hp = 2
        self.counter = 0
        self.speed = 2
        self.bild = 0
        self.type = 2

        if random.randint(1,2) == 2:
            self.speed = 4
        
        self.bewegungsrichtung = bewegungsrichtung(self.rect, self.speed)


    def move(self):
        self.bewegungsrichtung.update()
        self.rect.topleft += self.bewegungsrichtung.Vector * self.speed
        self.image = self.bewegungsrichtung.image
        self.hit_image = self.bewegungsrichtung.image_hit
        #pygame.draw.rect(self.display_surface, (255,0,0), self.bewegungsrichtung.rect_relevant)

    def delete(self):
        global gegner, gegner_eliminiert
        self.rect.topleft -= self.bewegungsrichtung.Vector * self.speed  
        if self.bild == 10:
            self.kill()
            gegner -= 1
            gegner_eliminiert += 1
        self.image = pygame.transform.scale(self.image,(feld_pixel - int(self.bild*3), feld_pixel - int(self.bild*3)))
        self.bild += 0.5


class alien3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.hit_image = alien3Img_hit
        self.image = alien3Img
        self.image_normal = alien3Img
        self.rect = self.image.get_rect(topleft = pos)
        self.speedx = random.randint(2,4)
        self.speedy = self.speedx
        self.hp = 1
        self.hit = False
        self.counter = 0
        self.bild = 0
        self.tpye = 3

        if random.randint(1,2) == 1:
            self.speedx *= -1

        if random.randint(1,2) == 1:
            self.speedy *= -1

    def move(self):     #noch in arbeit

        self.rect.top += self.speedy
        self.rect.left += self.speedx
        self.test1 = False
        self.test2 = False

        
        for wegraeumbares in wegraeumbareSprites:
            if wegraeumbares.rect.colliderect(self.rect):
                wegraeumbares.delete()

        for hinderniss in aliencollisionSprites:

            if hinderniss.rect.colliderect(self.rect):
                if hinderniss.rect.collidepoint(self.rect.centerx, self.rect.top) or hinderniss.rect.collidepoint(self.rect.centerx, self.rect.bottom):
                    self.rect.top -= self.speedy
                    self.speedy *= -1
                    self.test1 = True

                if hinderniss.rect.collidepoint(self.rect.left, self.rect.centery) or hinderniss.rect.collidepoint(self.rect.right, self.rect.centery):
                    self.rect.left -= self.speedx
                    self.speedx *= -1
                    self.test2 = True

                if self.test1 == True and self.test2 == True:
                    
                    if hinderniss.rect.collidepoint(self.rect.left+1, self.rect.top) and not hinderniss.rect.collidepoint(self.rect.left, self.rect.top+1):
                        self.rect.top -= self.speedy
                        self.speedy *= -1

                    elif hinderniss.rect.collidepoint(self.rect.left, self.rect.top+1) and not hinderniss.rect.collidepoint(self.rect.left+1, self.rect.top):
                        self.rect.left -= 1
                        self.speedx *= -1


                    if hinderniss.rect.collidepoint(self.rect.right-1, self.rect.top) and not hinderniss.rect.collidepoint(self.rect.right, self.rect.top+1):
                        self.rect.top -= self.speedy
                        self.speedy *= -1

                    elif hinderniss.rect.collidepoint(self.rect.right, self.rect.top+1) and not hinderniss.rect.collidepoint(self.rect.right-1, self.rect.top):
                        self.rect.left -= self.speedx
                        self.speedx *= -1


                    if hinderniss.rect.collidepoint(self.rect.left+1, self.rect.bottom) and not hinderniss.rect.collidepoint(self.rect.left, self.rect.bottom-1):
                        self.rect.top -= self.speedy
                        self.speedy *= -1

                    elif hinderniss.rect.collidepoint(self.rect.left, self.rect.bottom-1) and not hinderniss.rect.collidepoint(self.rect.left+1, self.rect.bottom):
                        self.rect.left -= self.speedx
                        self.speedx *= -1


                    if hinderniss.rect.collidepoint(self.rect.right-1, self.rect.bottom) and not hinderniss.rect.collidepoint(self.rect.right, self.rect.bottom -1):
                        self.rect.top -= self.speedy
                        self.speedy *= -1

                    elif hinderniss.rect.collidepoint(self.rect.right, self.rect.bottom -1) and not hinderniss.rect.collidepoint(self.rect.right-1, self.rect.bottom):
                        self.rect.left -= self.speedx
                        self.speedx *= -1    


    def delete(self):
        global gegner, gegner_eliminiert
        self.rect.top -= self.speedy
        self.rect.left -= self.speedx
        if self.bild == 10:
            self.kill()
            gegner -= 1
            gegner_eliminiert += 1
        self.image = pygame.transform.scale(self.image,(feld_pixel - int(self.bild*3), feld_pixel - int(self.bild*3)))
        self.bild += 0.5


def textfeld(schrift,rechts,oben,screen,text):  #für statistiken am ende
    if text == 20:
        schrift = font40.render(str(schrift), True, (255,255,255))
    elif text == 40:
        schrift = font80.render(str(schrift), True, (255,255,255))
    elif text == 60:
        schrift = font120.render(str(schrift), True, (255,255,255))
    schrift_rect = schrift.get_rect()
    if rechts == "center":
        schrift_rect.centerx = realFensterBreite / 2
        schrift_rect.top = oben
    else:
        schrift_rect.topleft = (rechts - schrift_rect.width, oben)
    screen.blit(schrift,schrift_rect)


bombenart = 0
def bombenart_update():
    global bombe_verstärkung
    bombe_verstärkung += 1
    if bombe_verstärkung >= 4:
        bombe_verstärkung = 4
    

class Level:        #dieser teil ist wichtig
    def __init__(self, map):
        global bombenanzahl, gegner_eliminiert, gegner, bombenart, bombe_verstärkung, explosionsmap
        self.draw_sichtbaresThread = Thread(target = self.draw_sichtbares(), name = "sichtbaresThread")
        self.draw_guteresThread = Thread(target = self.draw_guteres(), name = "guteresThread")
        self.draw_besseresThread = Thread(target = self.draw_besseres(), name = "besseresThread")
        self.bombenboostcounter = 0        
        self.map = map
        bombenart = 0
        bombe_verstärkung = 0
        self.mapBreite = 0
        self.mapHoehe = 0
        self.explosionSprite_count = 0
        self.runtime = 0
        self.fenster = pygame.display.get_surface()
        self.camAbstand = pygame.math.Vector2()
        self.end = False
        self.punkte = 0
        self.gegner_moving = 0
        self.bombenplatziert = 0
        self.objekte_eingesammelt = 0
        self.sprengbarescount = 0
        self.bombeverstalt = 0
        self.spielerhp = 10
        self.godmode = False
        self.spielerhpalt = 0
        bombenanzahl = 3
        gegner_eliminiert = 0
        gegner = 0
        explosionsmap = self.map.copy()
        self.won = False
        self.create_map()  
        self.infofeld = infofeld(FensterHoehe, self.spieler, self.fenster, bombenanzahl)
    
    def update_bombenboost(self):
        global bombenart
        if self.bombenboostcounter < 3:
            pass
        else:
            bombenart += 1
            self.bombenboostcounter = 0
            bombenart_update()
            self.infofeld.update_bombenart(bombenart)

    def create_map(self):
        global gegner
        for spalte_index, spalte in enumerate(self.map):
            for zeile_index, spalte in enumerate(spalte):
                x = zeile_index * feld_pixel
                y = spalte_index * feld_pixel
                

                if spalte == 1:
                    border((x,y),[sichtbareSprites, collisionSprites, aliencollisionSprites])


                if spalte == 5:
                    self.spieler = Player((x,y),[bessereSprites], collisionSprites, self.spielerhp)
                    spawnfeld((x,y),[sichtbareSprites])

                
                if spalte == 2:
                    sprengbares((x,y),[sichtbareSprites, sprengbaresSprites, collisionSprites, aliencollisionSprites])
                    self.sprengbarescount += 1


                if spalte == 3:
                    wegraeumbares((x,y), [sichtbareSprites, wegraeumbareSprites, collisionSprites, aliencollisionSprites])


                if spalte == 10:
                    alien1((x,y),[bessereSprites, alienSprites])
                    gegner += 1

                if spalte == 11:
                    alien2((x,y),[bessereSprites, alienSprites], self.fenster)
                    gegner += 1

                if spalte == 12:
                    alien3((x,y),[bessereSprites, alienSprites])
                    gegner += 1

                if spalte == 50:
                    bombe_objekt((x,y), [gutereSprites, bombenobjekteSprites, aliencollisionSprites])
                
                if spalte == 51:
                    slowness_potion((x,y), [gutereSprites, slownessSprites, aliencollisionSprites])

                if spalte == 52:
                    speed_potion((x,y),[gutereSprites, speedSprites, aliencollisionSprites])

                if spalte == 53:
                    hp_boost((x,y),[gutereSprites, hpboostSprites, aliencollisionSprites])


                if spalte == 6:
                    bild((x,y),[sichtbareSprites])

                #if spalte == 9:
                 #   wegraeumbares((x,y),[sichtbareSprites])

                self.mapBreite += feld_pixel   
            self.mapHoehe += feld_pixel
        #self.mapHoehe -= feld_pixel
        self.mapBreite = self.mapBreite // (self.mapHoehe / feld_pixel)       


    def update(self):
        #print (bombenart, self.bombenboostcounter)
        global bombenanzahl

        self.gegner_moving = 0
        for alien in alienSprites:
            if alien.rect.top - self.camAbstand.y <= 1000 and alien.rect.top - self.camAbstand.y > -100:
                if alien.rect.left - self.camAbstand.x < 1300 and alien.rect.left - self.camAbstand.x > -100:
                    alien.move()
                    self.gegner_moving += 1
            for explosion in explosionSprites:
                if alien.rect.colliderect(explosion.rect):
                    if alien.hit == False:
                        dmg = explosion.damage
                        alien.hit = True
            
            if alien.hit == True:
                alien.counter += 1
            
                if alien.counter == 1:
                    alien.hp -= dmg

                if alien.counter >= 0 and alien.counter < 15 or alien.counter >= 30 and alien.counter < 45 or alien.counter >= 60 and alien.counter < 75:
                    alien.image = alien.hit_image
                
                else:
                    alien.image = alien.image_normal
                
                if alien.counter == 75:
                    alien.hit = False
                    alien.counter = 0

            if alien.hp <= 0:
                alien.delete()
                

            if self.spieler.rect.colliderect(alien.rect):
                if self.spieler.hit == False:
                    self.spieler.hit = True
                    self.spieler.damage_taken = 1

        if not self.godmode:
            for wegraeumbares in wegraeumbareSprites:
                if self.spieler.rect.colliderect(wegraeumbares.rect):
                    wegraeumbares.delete()


            for explosion in explosionSprites:
                if self.spieler.rect.colliderect(explosion.rect):
                    if self.spieler.hit == False:
                        self.spieler.hit = True
                        self.spieler.damage_taken = explosion.damage

                for wegraeumbares in wegraeumbareSprites:
                    if wegraeumbares.rect.colliderect(explosion.rect):
                        wegraeumbares.delete()
        
                for sprengbares in sprengbaresSprites:
                    if sprengbares.rect.colliderect(explosion.rect):
                        sprengbares.delete()

            for hpboost in hpboostSprites:
                if self.spieler.rect.colliderect(hpboost.rect):
                    hpboost.delete()
                    self.objekte_eingesammelt += 1
                    self.spieler.hp += 1

            for speed_pot in speedSprites:
                if self.spieler.rect.colliderect(speed_pot.rect):
                    speed_pot.delete()
                    self.objekte_eingesammelt += 1
                    self.spieler.speed += 2
                    potion_counter([speedcounterSprites], 2)

            for slowness_pot in slownessSprites:
                if self.spieler.rect.colliderect(slowness_pot.rect):
                    slowness_pot.delete()
                    self.objekte_eingesammelt += 1
                    if self.spieler.speed > 2:
                        self.spieler.speed -= 2
                        potion_counter([slownesscounterSprites], 2)
                    else:
                        self.spieler.speed = 1
                        potion_counter([slownesscounterSprites],1)

            for bombeboost in bombeboostSprites:
                if self.spieler.rect.colliderect(bombeboost.rect):
                    bombeboost.delete()
                    self.objekte_eingesammelt += 1
                    self.infofeld.bombenboostcounter += 1
                    self.bombenboostcounter += 1
                    self.update_bombenboost()

            for counter in speedcounterSprites:
                counter.count()
                if counter.wert == 600:
                    self.spieler.speed -= counter.speed 
                    counter.delete()

            for counter in slownesscounterSprites:
                counter.count()
                if counter.wert == 600:
                    self.spieler.speed += counter.speed
                    counter.delete()


        if self.spieler.speed <= 0:
            self.spieler.speed = 2



        for bombe in bombenobjekteSprites:
            if self.spieler.rect.colliderect(bombe.rect):
                bombenanzahl += 1
                self.infofeld.bombenanzahl += 1
                self.infofeld.createbombe()
                bombe.delete()
                self.objekte_eingesammelt += 1

    def draw_sichtbares(self):
        for spritee in sichtbareSprites:
            self.fenster.blit(spritee.image, (spritee.rect.topleft - self.camAbstand))

    def draw_guteres(self):
        for sprite in gutereSprites:   #ebene2: bomben/objekte
            self.fenster.blit(sprite.image, sprite.rect.topleft - self.camAbstand)

    def draw_besseres(self):
        for sprite in bessereSprites:  #ebene3: spieler und gegner
            self.fenster.blit(sprite.image, sprite.rect.topleft - self.camAbstand) 

    def kameraabstand(self, spieler):        #eigentlich kann man alle sprites zeichnen mit spritegruppe.update() aber aufgrund der kamerabewegung geht dies hier nicht
        
        if self.mapBreite <= LevelFensterBreite: #kamerabewegung x
            self.camAbstand.x = 0
        else:
            self.camAbstand.x = (spieler.rect.left - LevelFensterBreite/2) 
            
            if self.spieler.rect.left <= LevelFensterBreite/2:
                self.camAbstand.x = 0
            
            if self.spieler.rect.left >= self.mapBreite - LevelFensterBreite/2:
                self.camAbstand.x = self.mapBreite - LevelFensterBreite
        
        if self.mapHoehe <= FensterHoehe:   #kamerabewegung y
            self.camAbstand.y = 0
        else:
            self.camAbstand.y = (spieler.rect.top - FensterHoehe/2) 
        
            if self.spieler.rect.top <= FensterHoehe/2:     
                self.camAbstand.y = 0
            
            if self.spieler.rect.top >= self.mapHoehe - FensterHoehe/2:
                self.camAbstand.y = self.mapHoehe - FensterHoehe
            

        #test
        #self.camAbstand.x = 0
        #self.camAbstand.y = 0
            #self.fenster.blit(sprite.image, (sprite.rect.topleft - self.camAbstand))

            #if sprite.type == "grenzfeld":
             #   pygame.draw.rect(self.fenster, (150,150,150), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))

            #if sprite.type == "sprengbares":
              #  pygame.draw.rect(self.fenster, (100,15,15), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))

            #if sprite.type == "spawnfeld":
             #   pygame.draw.rect(self.fenster, (15,100,15), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))
        
           

            #if sprite.type == 1:
             #   pygame.draw.rect(self.fenster, (11,130,239), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))

            #if sprite.type == 2:
             #   pygame.draw.rect(self.fenster, (0,255,0), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))
    
        #    if sprite.type == 0:
         #       pygame.draw.rect(self.fenster, (255,0,0), (sprite.rect.left - self.camAbstand.x, sprite.rect.top - self.camAbstand.y, sprite.rect.width, sprite.rect.height))
    
    
    def dings(self):    #bomben
        global bombenanzahl
        self.bombenplatziert += 1
        pos = pygame.math.Vector2((self.spieler.rect.left - self.spieler.rect.left % feld_pixel, self.spieler.rect.top - self.spieler.rect.top % feld_pixel))    
        pos_neu = True
        
        for rect in bombenSprites:      #bomben sollen nicht übereinander platziert werden
            if rect.rect.collidepoint(pos):
                pos_neu = False
       

        if bombenanzahl == 0:
            pass

        else:
            if pos_neu == True:
                if bombe_verstärkung == 0:
                    e = bombe([gutereSprites, bombenSprites],pos,self.map)
                elif bombe_verstärkung == 1:
                    e = bombe_verstärkt1([gutereSprites, bombenSprites],pos,self.map)
                elif bombe_verstärkung == 2:
                    e = bombe_verstärkt2([gutereSprites, bombenSprites],pos,self.map)                    
                elif bombe_verstärkung == 3:
                    e = bombe_verstärkt3([gutereSprites, bombenSprites],pos,self.map)
                elif bombe_verstärkung == 4:
                    e = bombe_verstärkt4([gutereSprites, bombenSprites],pos,self.map)
                bombenanzahl -= 1
                self.infofeld.animiertebomben += 1
                e.explode()
                self.infofeld.bombe_explode()
                e.update()


    def godmode_update(self):
        global bombe_verstärkung
        if self.godmode:
            self.godmode = False
            bombe_verstärkung = self.bombeverstalt
            self.spielerhp = self.spielerhpalt
            self.infofeld.update_bombenart(self.bombeverstalt)
            self.spieler.godmode = False
            self.spieler.godmode = False
        else:
            self.godmode = True
            self.bombeverstalt = bombe_verstärkung
            bombe_verstärkung = 4
            self.infofeld.update_bombenart(4)
            self.spielerhpalt = self.spielerhp
            self.hp = 10000
            self.spieler.speed = feld_pixel / 4
            self.spieler.godmode = True
            self.infofeld.godmode = True

    def run(self):
        #print(self.gegner_moving)
        #print(gegner)
        #print(self.spielerhp, self.spieler.hp)
        #print (explosionsListe)
        #print(bombenanzahl)
        #print (self.spieler.hp)
        self.draw_sichtbaresThread = Thread(target = self.draw_sichtbares(), name = "sichtbaresThread")
        self.draw_guteresThread = Thread(target = self.draw_guteres(), name = "guteresThread")
        self.draw_besseresThread = Thread(target = self.draw_besseres(), name = "besseresThread")
        self.runtime += 1
        self.update()
        self.draw_sichtbaresThread.start()
        self.draw_guteresThread.start()
        self.draw_besseresThread.start()
        self.kameraabstand(self.spieler)
        self.draw_sichtbaresThread.join()
        self.draw_guteresThread.join()
        self.draw_besseresThread.join()
        sichtbareSprites.update()
        bessereSprites.update()
        gutereSprites.update()
        
        self.infofeld.update()
        if gegner == 0:
            self.won = True
        if self.won or self.spieler.gestorben:
            self.end = True
            
    def statistiken(self):  #statistiken am ende des levels

        self.zeit_punkte = 1800 - int(self.runtime/10)
        self.gegner_punkte = gegner_eliminiert * 200
        self.objekt_punkte = self.objekte_eingesammelt * 50
        self.bombenpunkte = self.bombenplatziert * 25
        self.bombenanzahlpunkte = bombenanzahl * 50

        self.punkte = self.zeit_punkte + self.gegner_punkte + self.objekt_punkte + self.bombenanzahlpunkte + self.bombenpunkte
        
        #sachen
        self.oben_linie = pygame.rect.Rect(0,70,realFensterBreite,1)
        pygame.draw.rect(self.fenster, (255,255,255), self.oben_linie)
        if self.spieler.gestorben == True:
            textfeld("Du bist gestorben", "center", 5, self.fenster, 60)
        elif gegner == 0:
            textfeld("Level gewonnen!", "center", 5, self.fenster, 60)
        textfeld("Statistiken", "center", 80, self.fenster, 40)
        textfeld("Punkte", 200, 150,self.fenster, 20)
        textfeld(self.punkte,300, 150,self.fenster, 20)
        textfeld("Objekte eingesammelt", 200, 210, self.fenster, 20)
        textfeld(self.objekte_eingesammelt, 300, 210, self.fenster, 20)
        textfeld("Gegner eliminiert", 200, 260, self.fenster, 20)
        textfeld(gegner_eliminiert, 300, 260, self.fenster, 20)
        textfeld("Bomben platziert",570, 270, self.fenster, 20)
        textfeld(self.bombenplatziert, 670, 270, self.fenster, 20)
        textfeld("Zeit", 570, 150, self.fenster, 20)
        textfeld(int(self.runtime/60), 670, 150, self.fenster, 20)
        textfeld("Sekunden", 760, 150, self.fenster, 20)
        textfeld("Gesundheit übrig", 570, 210, self.fenster, 20)
        textfeld((str(self.spieler.hp) + '/' + str(self.spielerhp)), 670, 210, self.fenster, 20)