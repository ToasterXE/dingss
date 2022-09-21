import pygame
import os
from maps import feld_pixel



Horizontalzuletzt = "keine" 
Vertikalzuletzt = "keine"
zuletzt = "keine"


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,hindernisse):
        super().__init__(groups)
        self.vorneImg = pygame.image.load((os.path.join("dateien", "player_vorne.png")))
        self.obenImg = pygame.image.load((os.path.join("dateien", "player_oben.png")))
        self.untenImg = pygame.image.load((os.path.join("dateien", "player_unten.png")))
        self.rechtsImg = pygame.image.load((os.path.join("dateien", "player_rechts.png")))
        self.linksImg = pygame.image.load((os.path.join("dateien", "player_links.png")))
        self.image = self.vorneImg
        self.image_normal = self.vorneImg
        self.hit_image = pygame.image.load((os.path.join("dateien", "player_hit.png")))
        self.rect = self.image.get_rect(topleft = pos)
        self.blickrichtung = pygame.math.Vector2()
        self.hindernisse = hindernisse
        self.speed = 4
        self.hp = 8
        self.hit = False
        self.hpcounter = 0
        self.tot = False

        self.stop_vertikal = False
        self.stop_horizontal = False

    def abstand_negativ(self,pos):
        if pos % feld_pixel >= self.speed:
            return self.speed
        else:
            return pos % feld_pixel

    def abstand_positiv(self,pos):
        soll_pos = ((pos // feld_pixel) + 1) * feld_pixel
        if soll_pos == pos:
            pass
        elif soll_pos - pos >= self.speed:
            return self.speed
        else:
            return soll_pos - pos

    def player_movement(self):
        keys_pressed = pygame.key.get_pressed()
        global i, zuletzt, Vertikalzuletzt, Horizontalzuletzt

        if keys_pressed[pygame.K_w]:
            self.blickrichtung.x = 0
            self.blickrichtung.y = -1
            Vertikalzuletzt = "w"
            zuletzt = "w"
            self.image = self.obenImg
            self.stop_vertikal = False
            self.stop_horizontal = True

        elif keys_pressed[pygame.K_s]:
            self.blickrichtung.x = 0    
            self.blickrichtung.y = 1
            Vertikalzuletzt = "s"
            zuletzt = "s"
            self.image = self.untenImg
            self.stop_vertikal = False
            self.stop_horizontal = True

        elif keys_pressed[pygame.K_a]:
            self.blickrichtung.x = -1
            self.blickrichtung.y = 0
            Horizontalzuletzt = "a"
            zuletzt = "a"
            self.image = self.linksImg
            self.stop_horizontal = False
            self.stop_vertikal = True

        elif keys_pressed[pygame.K_d]:
            self.blickrichtung.x = 1
            self.blickrichtung.y = 0
            Horizontalzuletzt = "d"
            zuletzt = "d"
            self.image = self.rechtsImg
            self.stop_horizontal = False
            self.stop_vertikal = True

        else:
            self.blickrichtung.x = 0
            self.blickrichtung.y = 0            
            self.image = self.vorneImg
            self.stop_horizontal = True
            self.stop_vertikal = True

        self.rect.topleft += self.blickrichtung * self.speed


        if self.stop_vertikal == True:
            
            if self.rect.top % feld_pixel == 0:
                pass
                
            else:
                if Vertikalzuletzt == "w":
                    self.image = self.obenImg
                    self.rect.top -= self.abstand_negativ(self.rect.top)

                if Vertikalzuletzt == "s":
                    self.rect.top += self.abstand_positiv(self.rect.top)
                    self.image = self.untenImg
    
        if self.stop_horizontal == True:

            if self.rect.left % feld_pixel == 0:
                    pass
        
            else:
                if Horizontalzuletzt == "d":
                    self.rect.left += self.abstand_positiv(self.rect.left)
                    self.image = self.rechtsImg
                if Horizontalzuletzt == "a":
                    self.rect.left -= self.abstand_negativ(self.rect.left)
                    self.image = self.linksImg
                    
               
        for hinderniss in self.hindernisse:
        

            if hinderniss.rect.colliderect(self.rect):

                if zuletzt == "w":
                    self.rect.top += hinderniss.rect.bottom - self.rect.top
                if zuletzt == "s":
                    self.rect.top -= self.rect.bottom - hinderniss.rect.top 
                if zuletzt == "d":
                    self.rect.left -= self.rect.right - hinderniss.rect.left
                if zuletzt == "a":
                    self.rect.left += hinderniss.rect.right - self.rect.left

    def hp_update(self):
        if self.hit == True:
                self.hpcounter += 1
            
                if self.hpcounter == 10:
                    self.hp -= 1
                    if self.hp == 0:
                        self.tot = True

                if self.hpcounter >= 0 and self.hpcounter < 10 or self.hpcounter >= 20 and self.hpcounter < 30 or self.hpcounter >= 40 and self.hpcounter < 50:
                    self.image = self.hit_image
                
                else:
                    self.image = self.image_normal
                
                if self.hpcounter == 50:
                    self.hit = False
                    self.hpcounter = 0


    def update(self):
        self.player_movement()
        self.hp_update()