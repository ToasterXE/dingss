import pygame
import os
from einstellungen import feld_pixel
from bilder import *
Horizontalzuletzt = "keine" 
Vertikalzuletzt = "keine"
zuletzt = "keine"

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,hindernisse,hp=10):
        super().__init__(groups)
        self.vorneImg = playervorneImg
        self.obenImg = playerobenImg
        self.untenImg = playeruntenImg
        self.rechtsImg = playerrechtsImg
        self.linksImg = playerlinksImg
        self.image = self.vorneImg
        self.image_normal = self.vorneImg
        self.image32 = playervorneImg32
        self.hit_image = playerhit_image
        self.rect = self.image.get_rect(topleft = pos)
        self.blickrichtung = pygame.math.Vector2()
        self.hindernisse = hindernisse
        self.speed = feld_pixel / 8
        self.hp = hp
        self.hit = False
        self.godmode = False
        self.hpcounter = 0
        self.gestorben = False
        self.damage_taken = 0
        self.stop_vertikal = False
        self.stop_horizontal = False
        self.type = 0

    def abstand_negativ(self,pos):      #ausrechnung der schrittgröße wenn der spieler sich in die mitte eines feldes bewegt
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
            self.image32 = playerobenImg32
            self.stop_vertikal = False
            self.stop_horizontal = True

        elif keys_pressed[pygame.K_s]:
            self.blickrichtung.x = 0    
            self.blickrichtung.y = 1
            Vertikalzuletzt = "s"
            zuletzt = "s"
            self.image = self.untenImg
            self.image32 = playeruntenImg32
            self.stop_vertikal = False
            self.stop_horizontal = True

        elif keys_pressed[pygame.K_a]:
            self.blickrichtung.x = -1
            self.blickrichtung.y = 0
            Horizontalzuletzt = "a"
            zuletzt = "a"
            self.image = self.linksImg
            self.image32 = playerlinksImg32
            self.stop_horizontal = False
            self.stop_vertikal = True

        elif keys_pressed[pygame.K_d]:
            self.blickrichtung.x = 1
            self.blickrichtung.y = 0
            Horizontalzuletzt = "d"
            zuletzt = "d"
            self.image = self.rechtsImg
            self.image32 = playerrechtsImg32
            self.stop_horizontal = False
            self.stop_vertikal = True

        else:
            self.blickrichtung.x = 0
            self.blickrichtung.y = 0            
            self.image = self.vorneImg
            self.image32 = playervorneImg32
            self.stop_horizontal = True
            self.stop_vertikal = True

        self.rect.topleft += self.blickrichtung * self.speed

        #der spieler soll nicht zwischen verschiedenen feldern stehen bleiben, sondern immer nur in der mitte eines feldes
        if self.stop_vertikal == True:
            
            if self.rect.top % feld_pixel == 0:
                pass
                
            else:
                if Vertikalzuletzt == "w":
                    self.image = self.obenImg
                    self.image32 = playerobenImg32
                    self.rect.top -= self.abstand_negativ(self.rect.top)

                if Vertikalzuletzt == "s":
                    self.rect.top += self.abstand_positiv(self.rect.top)
                    self.image = self.untenImg
                    self.image32 = playeruntenImg32
    
        if self.stop_horizontal == True:

            if self.rect.left % feld_pixel == 0:
                    pass
        
            else:
                if Horizontalzuletzt == "d":
                    self.rect.left += self.abstand_positiv(self.rect.left)
                    self.image = self.rechtsImg
                    self.image32 = playerrechtsImg32
                if Horizontalzuletzt == "a":
                    self.rect.left -= self.abstand_negativ(self.rect.left)
                    self.image = self.linksImg
                    self.image32 = playerlinksImg32
                    
        if not self.godmode:       
            for hinderniss in self.hindernisse:
            
                if hinderniss.rect.colliderect(self.rect):      #wenn der spieler in ein hinderniss hereinläuft wird die bewegung rückgängig gemacht, bevor alles gezeichnet wird
                    if not hinderniss.type == "wegraeumbares":               
        
                        if zuletzt == "w":
                            self.rect.top += hinderniss.rect.bottom - self.rect.top
                        if zuletzt == "s":
                            self.rect.top -= self.rect.bottom - hinderniss.rect.top 
                        if zuletzt == "d":
                            self.rect.left -= self.rect.right - hinderniss.rect.left
                        if zuletzt == "a":
                            self.rect.left += hinderniss.rect.right - self.rect.left
        else:
            self.image = player_godmodeImg
    def hp_update(self):
        if self.hit == True:
                self.hpcounter += 1
            
                if self.hpcounter == 10:
                    self.hp -= self.damage_taken
                    if self.hp <= 0:
                        self.gestorben = True

                if self.hpcounter >= 0 and self.hpcounter < 10 or self.hpcounter >= 20 and self.hpcounter < 30 or self.hpcounter >= 40 and self.hpcounter < 50:
                    self.image = self.hit_image
                    self.image32 = playerhit_image32
                
                else:
                    self.image = self.image_normal
                    self.image32 = playervorneImg32
                
                if self.hpcounter == 50:
                    self.hit = False
                    self.hpcounter = 0


    def update(self):
        self.player_movement()
        if not self.godmode:
            self.hp_update()