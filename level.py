import pygame, os
from maps import *
from level import *
from player import Player
from objekte import *
import random 

bombenanzahl = 3
explosionsListe = []
gegner = 0
gegner_eliminiert = 0
pygame.font.init()
font20 = pygame.font.SysFont("candara", 20)
font40 = pygame.font.SysFont("candara", 40)
font60 = pygame.font.SysFont("candara", 60)

#sichtbare spritegruppen
sichtbareSprites = pygame.sprite.Group()
bessereSprites = pygame.sprite.Group()
gutereSprites = pygame.sprite.Group()

#unsichtbare spritegruppen
collisionSprites = pygame.sprite.Group()    #hindernisse
bombenSprites = pygame.sprite.Group()    
wegraeumbareSprites = pygame.sprite.Group()
explosionSprites = pygame.sprite.Group()
sprengbaresSprites = pygame.sprite.Group()
speedSprites = pygame.sprite.Group()
slownessSprites = pygame.sprite.Group()
speedcounterSprites = pygame.sprite.Group() #keine sprites
slownesscounterSprites = pygame.sprite.Group()
bombenobjekteSprites = pygame.sprite.Group()
alienSprites = pygame.sprite.Group()

#bilder
bombeImg1  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe1.png" )),(feld_pixel, feld_pixel))
bombeImg2  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe2.png" )),(feld_pixel, feld_pixel))
bombeImg3  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe3.png" )),(feld_pixel, feld_pixel))
bombeImg4  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe4.png" )),(feld_pixel, feld_pixel))
bombeImg5  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe5.png" )),(feld_pixel, feld_pixel))
bombeImg6  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe6.png" )),(feld_pixel, feld_pixel))
bombeImg7  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe7.png" )),(feld_pixel, feld_pixel))
bombeImg8  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe8.png" )),(feld_pixel, feld_pixel))
bombeImg9  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe9.png" )),(feld_pixel, feld_pixel))
bombeImg10 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe10.png")),(feld_pixel, feld_pixel))
bombeImg11 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe11.png")),(feld_pixel, feld_pixel))
bombeImg12 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe12.png")),(feld_pixel, feld_pixel))

explosionsImg1 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel, feld_pixel))
explosionsImg2 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel+ 2, feld_pixel+2))
explosionsImg4 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel, feld_pixel))
explosionsImg5 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel+2, feld_pixel+2))
explosionsImg7 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel, feld_pixel))
explosionsImg8 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel+2, feld_pixel+2))
explosionsImg10 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel, feld_pixel))
explosionsImg11 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel+2, feld_pixel+2))

leerImg = pygame.image.load((os.path.join("dateien", "leer.png")))
nichtsImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien","nichts.png")),(feld_pixel, feld_pixel))
borderImg = pygame.image.load((os.path.join("dateien", "border.png")))
sprengbaresImg = pygame.transform.scale(pygame.image.load((os.path.join("dateien", "sprengbares.png"))),(feld_pixel, feld_pixel))
leerImg = pygame.transform.scale(pygame.image.load((os.path.join("dateien", "leer.png"))),(feld_pixel, feld_pixel))
wegraeumbaresImg = pygame.image.load((os.path.join("dateien", "wegräumbares.png")))

alien1Img = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien1.png"))),(feld_pixel,feld_pixel))
alien1Img_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien1_hit.png"))),(feld_pixel,feld_pixel))
alien2Img_unten = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_unten.png"))),(feld_pixel,feld_pixel))
alien2Img_rechts = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_rechts.png"))),(feld_pixel,feld_pixel))
alien2Img_oben = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_oben.png"))),(feld_pixel,feld_pixel))
alien2Img_links = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_links.png"))),(feld_pixel,feld_pixel))
alien2Img_unten_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_unten_hit.png"))),(feld_pixel,feld_pixel))
alien2Img_rechts_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_rechts_hit.png"))),(feld_pixel,feld_pixel))
alien2Img_oben_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_oben_hit.png"))),(feld_pixel,feld_pixel))
alien2Img_links_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien2_links_hit.png"))),(feld_pixel,feld_pixel))

alien3Img = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien3.png"))),(feld_pixel-3,feld_pixel-3))
alien3Img_hit = pygame.transform.scale(pygame.image.load((os.path.join("dateien","alien3_hit.png"))),(feld_pixel-3,feld_pixel-3))


class potion_counter(pygame.sprite.Sprite): #keine sprites
    def __init__(self,groups,speed):
        super().__init__(groups)
        self.wert = 0
        self.speed = speed
    def count(self):
        self.wert += 1
    def delete(self):
        self.kill()


class border(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = borderImg
        self.image = pygame.transform.scale(self.image, (feld_pixel, feld_pixel),)
        self.rect = self.image.get_rect(topleft = pos)


class sprengbares(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = sprengbaresImg
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pos

    def delete(self):
        self.replace(random.randint(0,100))
        self.kill()

    def replace(self,nummer):   #wichtige sachen
        if nummer >= 95:
            slowness_potion(self.pos,[gutereSprites,slownessSprites])
        if nummer >= 10 and nummer < 20:
            speed_potion(self.pos, [gutereSprites,speedSprites])
        if nummer >= 0 and nummer < 8:
            bombe_objekt(self.pos,[gutereSprites,bombenobjekteSprites])


class spawnfeld(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load((os.path.join("dateien", "spawn.png")))
        self.rect = self.image.get_rect(topleft = pos)


class wegraeumbares(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = wegraeumbaresImg
        self.rect = self.image.get_rect(topleft = pos)

    def delete(self):
        self.kill()


class explosionsAnimation(pygame.sprite.Sprite):
    def __init__(self,groups,pos,map):
        super().__init__(groups)
        
        self.levelmap = map
        self.pos = pos

        if self.levelmap[int(pos.y/32)][int(pos.x/32)] == "e":  
           self.kill()

        for i in range(0,len(explosionsListe)):
            if explosionsListe[i] == pos:
                self.kill()

        explosionsListe.append(self.pos)

        self.sprites = []
        self.sprites.append(explosionsImg1)
        self.sprites.append(explosionsImg2)
        self.sprites.append(explosionsImg4)
        self.sprites.append(explosionsImg5)
        self.sprites.append(explosionsImg7)
        self.sprites.append(explosionsImg8)
        self.sprites.append(explosionsImg10)
        self.sprites.append(explosionsImg11)

        self.counter = 0
        self.image = nichtsImg
        self.rect = self.image.get_rect(topleft = pos)        

    def animate(self):
        self.counter += 0.2

        if self.counter >= len(self.sprites):
            self.kill()
            explosionsListe.remove(self.pos)

        else:
            self.image = self.sprites[int(self.counter)]


class bombe(pygame.sprite.Sprite):
    def __init__(self, groups, pos, nummer,levelmap):
        super().__init__(groups)

        self.bombenSprites = []
        self.bombenSprites.append(bombeImg1)
        self.bombenSprites.append(bombeImg2)
        self.bombenSprites.append(bombeImg3)
        self.bombenSprites.append(bombeImg4)
        self.bombenSprites.append(bombeImg5)
        self.bombenSprites.append(bombeImg6)
        self.bombenSprites.append(bombeImg7)
        self.bombenSprites.append(bombeImg8)
        self.bombenSprites.append(bombeImg9)
        self.bombenSprites.append(bombeImg10)
        self.bombenSprites.append(bombeImg11)
        self.bombenSprites.append(bombeImg12)

        self.explosionsSprites = []
        self.explosionsSprites.append(explosionsImg1)
        self.explosionsSprites.append(explosionsImg2)
        self.explosionsSprites.append(explosionsImg4)
        self.explosionsSprites.append(explosionsImg5)
        self.explosionsSprites.append(explosionsImg7)
        self.explosionsSprites.append(explosionsImg8)
        self.explosionsSprites.append(explosionsImg10)
        self.explosionsSprites.append(explosionsImg11)
        
        self.counter = 0
        self.counter2 = 0
        self.nummer = nummer
        self.pos = pos
        self.map = levelmap

        self.image = self.bombenSprites[self.counter]
        self.rect = (self.image.get_rect(topleft = pos))

        self.exploding = False
        self.explosionsanimation = False
        #explosionsListe.append(self.pos)
        self.collision_rect = self.rect


    def explode(self):
        self.exploding = True
        self.explosionsanimation = False


    def update(self):
        global bombenanzahl

        if self.exploding == True:
            self.counter += 0.2

        if self.counter >= len(self.bombenSprites):
            self.counter = 0
            bombenanzahl += 1
            self.explosionsanimation = True
            self.exploding = False
            
            self.explosion_oben = explosionsAnimation([gutereSprites, explosionSprites],(self.pos - (0,feld_pixel)),self.map)
            self.explosion_unten = explosionsAnimation([gutereSprites, explosionSprites],(self.pos + (0,feld_pixel)),self.map)
            self.explosion_rechts = explosionsAnimation([gutereSprites, explosionSprites],(self.pos + (feld_pixel,0)),self.map)
            self.explosion_links = explosionsAnimation([gutereSprites, explosionSprites],(self.pos - (feld_pixel,0)),self.map)
            self.explosion = explosionsAnimation([gutereSprites,explosionSprites],self.pos,self.map)

        if self.exploding == True:            
            self.image = self.bombenSprites[int(self.counter)]
 
        if self.explosionsanimation == True:
            self.counter2 += 0.2
            self.explosion_oben.animate()
            self.explosion_unten.animate()
            self.explosion_rechts.animate()
            self.explosion_links.animate()
            self.explosion.animate()

        if int(self.counter2) >= len(self.explosionsSprites):
            self.explosionsanimation = False
            self.kill()
            

        if self.explosionsanimation == True:
            self.image = self.explosionsSprites[int(self.counter2)]


class alien1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.hit_image = alien1Img_hit
        self.image = alien1Img
        self.image_normal = alien1Img
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = random.randint(3,6)
        self.hp = 2
        self.hit = False
        self.counter = 0
        self.bild = 0

        if random.randint(1,2) == 1:
            self.speed *= -1
        
    def move(self):
        self.rect.left += self.speed
        for hinderniss in collisionSprites:
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

class alien2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
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
        self.rect = pygame.rect.Rect(self.rect.left -1, self.rect.top -1, self.rect.width +2, self.rect.height +2)
        
        self.hit = False
        self.hp = 1
        self.counter = 0
        self.speed = 2
        self.bild = 0

        if random.randint(1,2) == 2:
            self.speed = 4
        
        self.bewegungsrichtung = pygame.math.Vector2()


    def move(self):

        self.oben = False            
        self.rechts = False
        self.links = False
        self.unten = False
        
        for hinderniss in collisionSprites:
            if hinderniss.rect.colliderect(self.rect):

                if hinderniss.rect.collidepoint(self.rect.centerx, self.rect.bottom):   #unten
                    self.unten = True

                if hinderniss.rect.collidepoint(self.rect.right, self.rect.centery):  #rechts
                    self.rechts = True
                    self.unten = False

                if hinderniss.rect.collidepoint(self.rect.centerx, self.rect.top):   #oben                    
                    self.oben = True
                    self.rechts = False
                    self.unten = False

                if hinderniss.rect.collidepoint(self.rect.left, self.rect.centery):  #links
                    self.links = True
                    self.unten = False
                    self.oben = False
                    self.rechts = False

                if self.oben == False and self.rechts == False and self.links == False and self.unten == False:

                    if hinderniss.rect.collidepoint(self.rect.left, self.rect.bottom):
                        if hinderniss.rect.collidepoint(self.rect.left + self.speed, self.rect.bottom):   #unten
                            self.unten = True
                        else:
                            self.links = True

                    if hinderniss.rect.collidepoint(self.rect.right, self.rect.bottom):
                        if hinderniss.rect.collidepoint(self.rect.right, self.rect.bottom - self.speed):  #rechts
                            self.rechts = True
                        else:
                            self.unten = True

                    if hinderniss.rect.collidepoint(self.rect.right, self.rect.top):
                        if hinderniss.rect.collidepoint(self.rect.right - self.speed, self.rect.top):  #oben
                            self.oben = True
                        else:
                            self.rechts = True

                    if hinderniss.rect.collidepoint(self.rect.left, self.rect.top):
                        if hinderniss.rect.collidepoint(self.rect.left, self.rect.top + self.speed):  #links
                            self.links = True
                        else:
                            self.oben = True
            
            if self.links == True and self.rechts == True:
                self.rechts = False


        if self.oben == False and self.links == False and self.rechts == False and self.unten == False:
            self.bewegungsrichtung.x = 0
            self.bewegungsrichtung.y = 1
            if random.randint(1,4) == 1:
                self.image = self.image_oben
            if random.randint(1,4) == 2:
                self.image = self.image_rechts
            if random.randint(1,4) == 3:
                self.image = self.image_unten
            if random.randint(1,4) == 4:
                self.image = self.image_links       
        
        
        if self.links == True:    #links, bewegung nach unten
            self.image = self.image_links
            self.hit_image = self.image_links_hit
            self.bewegungsrichtung.x = 0
            self.bewegungsrichtung.y = 1
        
        if self.unten == True:   #unten, bewegung nach rechts
            self.image = self.image_unten
            self.hit_image = self.image_unten_hit
            self.bewegungsrichtung.x = 1
            self.bewegungsrichtung.y = 0
        
        if self.rechts == True:    #rechts, bewegung nach oben
            self.image = self.image_rechts
            self.hit_image = self.image_rechts_hit
            self.bewegungsrichtung.x = 0
            self.bewegungsrichtung.y = -1

        if self.oben == True: #oben, bewegung nach links
            self.image = self.image_oben
            self.hit_image = self.image_oben_hit
            self.bewegungsrichtung.x = -1
            self.bewegungsrichtung.y = 0

        self.rect.topleft += self.bewegungsrichtung * self.speed


    def delete(self):
        global gegner, gegner_eliminiert
        self.rect.topleft -= self.bewegungsrichtung * self.speed  
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
        self.hp = 3
        self.hit = False
        self.counter = 0
        self.bild = 0

        if random.randint(1,2) == 1:
            self.speedx *= -1

        if random.randint(1,2) == 1:
            self.speedy *= -1


    def move(self):

        self.rect.top += self.speedy
        self.rect.left += self.speedx
        self.test1 = False
        self.test2 = False

        for hinderniss in collisionSprites:

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


        for wegraeumbares in wegraeumbareSprites:
            if wegraeumbares.rect.colliderect(self.rect):
                wegraeumbares.delete()

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


def textfeld(schrift,rechts,oben,screen,text):
    if text == 20:
        schrift = font20.render(str(schrift), True, (255,255,255))
    elif text == 40:
        schrift = font40.render(str(schrift), True, (255,255,255))
    elif text == 60:
        schrift = font60.render(str(schrift), True, (255,255,255))
    schrift_rect = schrift.get_rect()
    if rechts == "center":
        schrift_rect.centerx = 400
        schrift_rect.top = oben
    else:
        schrift_rect.topleft = (rechts - schrift_rect.width, oben)
    screen.blit(schrift,schrift_rect)

class Level:
    def __init__(self, map):
        global bombenanzahl, gegner_eliminiert
        self.map = map
        self.mapBreite = 0
        self.mapHoehe = 0
        self.explosionSprite_count = 0
        self.runtime = 0
        self.display_surface = pygame.display.get_surface()
        self.camAbstand = pygame.math.Vector2()
        self.end = False
        self.punkte = 0
        self.bombenplatziert = 0
        self.objekte_eingesammelt = 0
        self.sprengbarescount = 0
        bombenanzahl = 3
        gegner_eliminiert = 0
        self.won = False

        self.create_map()


    def create_map(self):
        global gegner
        for spalte_index, spalte in enumerate(self.map):
            for zeile_index, spalte in enumerate(spalte):
                x = zeile_index * feld_pixel
                y = spalte_index * feld_pixel
                

                if spalte == "e":
                    border((x,y),[sichtbareSprites, collisionSprites])


                if spalte == "p":
                    self.player = Player((x,y),[bessereSprites], collisionSprites)
                    spawnfeld((x,y),[sichtbareSprites])

                
                if spalte == "s":
                    sprengbares((x,y),[sichtbareSprites, sprengbaresSprites, collisionSprites,])
                    self.sprengbarescount += 1

                if spalte == "w":
                    wegraeumbares((x,y), [sichtbareSprites, wegraeumbareSprites])
                
                if spalte == "x1":
                    alien1((x,y),[bessereSprites, alienSprites])
                    gegner += 1

                if spalte == "x2":
                    alien2((x,y),[bessereSprites, alienSprites])
                    gegner += 1

                if spalte == "x3":
                    alien3((x,y),[bessereSprites, alienSprites])
                    gegner += 1

                self.mapBreite += 32    
            self.mapHoehe += 32
        self.mapBreite = self.mapBreite // (self.mapHoehe / 32)       


    def update_player(self):
        global bombenanzahl

        for alien in alienSprites:
            alien.move()

            for explosion in explosionSprites:
                if alien.rect.colliderect(explosion.rect):
                    if alien.hit == False:
                        alien.hit = True
            
            if alien.hit == True:
                alien.counter += 1
            
                if alien.counter == 1:
                    alien.hp -= 1

                if alien.counter >= 0 and alien.counter < 15 or alien.counter >= 30 and alien.counter < 45 or alien.counter >= 60 and alien.counter < 75:
                    alien.image = alien.hit_image
                
                else:
                    alien.image = alien.image_normal
                
                if alien.counter == 75:
                    alien.hit = False
                    alien.counter = 0

            if alien.hp == 0:
                alien.delete()
                

            if self.player.rect.colliderect(alien.rect):
                if self.player.hit == False:
                    self.player.hit = True


        for eee in explosionSprites:
            if self.player.rect.colliderect(eee.rect):
                if self.player.hit == False:
                    self.player.hit = True

        for wegraeumbares in wegraeumbareSprites:
            if self.player.rect.colliderect(wegraeumbares.rect):
                wegraeumbares.delete()


        for explosion in explosionSprites:
            for wegraeumbares in wegraeumbareSprites:
                if wegraeumbares.rect.colliderect(explosion.rect):
                    wegraeumbares.delete()
    
            for sprengbares in sprengbaresSprites:
                if sprengbares.rect.colliderect(explosion.rect):
                    sprengbares.delete()


        for speed_pot in speedSprites:
            if self.player.rect.colliderect(speed_pot.rect):
                speed_pot.delete()
                self.objekte_eingesammelt += 1
                self.player.speed += 2
                potion_counter([speedcounterSprites],2)

        for slowness_pot in slownessSprites:
            if self.player.rect.colliderect(slowness_pot.rect):
                slowness_pot.delete()
                self.objekte_eingesammelt += 1
                if self.player.speed > 2:
                    self.player.speed -= 2
                    potion_counter([slownesscounterSprites],2)
                else:
                    self.player.speed = 1
                    potion_counter([slownesscounterSprites],1)


        for counter in speedcounterSprites:
            counter.count()
            if counter.wert == 600:
                self.player.speed -= counter.speed 
                counter.delete()

        for counter in slownesscounterSprites:
            counter.count()
            if counter.wert == 600:
                self.player.speed += counter.speed
                counter.delete()


        if self.player.speed <= 0:
            self.player.speed = 1


        for bombe in bombenobjekteSprites:
            if self.player.rect.colliderect(bombe.rect):
                bombenanzahl += 1
                bombe.delete()
                self.objekte_eingesammelt += 1
        #print (gegner)

    def draw(self, player):

        for sprite in sichtbareSprites:    #ebene1: unbewegte felder
            self.camAbstand.y = (player.rect.top - 225) 
            self.camAbstand.x = (player.rect.left - 400) 


            if self.player.rect.top <= 224:
                self.camAbstand.y = 0
            

            if self.player.rect.top >= self.mapHoehe - 224:
                self.camAbstand.y = self.mapHoehe - 448
            

            if self.player.rect.left <= 400:
                self.camAbstand.x = 0
            

            if self.player.rect.left >= self.mapBreite - 399:
                self.camAbstand.x = self.mapBreite - 798


            self.display_surface.blit(sprite.image, (sprite.rect.topleft - self.camAbstand))



        for sprite in gutereSprites:   #ebene2: bomben/objekte
            self.display_surface.blit(sprite.image, sprite.rect.topleft - self.camAbstand)

            

        for sprite in bessereSprites:  #ebene3: spieler und gegner
            self.display_surface.blit(sprite.image, sprite.rect.topleft - self.camAbstand)            



    def dings(self):
        self.bombenplatziert += 1
        global bombenanzahl
        pos = pygame.math.Vector2((self.player.rect.left - self.player.rect.left % feld_pixel, self.player.rect.top - self.player.rect.top % feld_pixel))        
        pos_neu = True
        
        for rect in bombenSprites:
            if rect.rect.collidepoint(pos):
                pos_neu = False
            else:
                pos_neu = True        

        if bombenanzahl == 0:
            pass
        
        else:
            if pos_neu == True:
                e = bombe([gutereSprites, bombenSprites],pos,1,self.map)
                bombenanzahl -= 1
                e.explode()
                e.update()
        

    def run(self):
        self.runtime += 1
        sichtbareSprites.update()
        bessereSprites.update()
        gutereSprites.update()
        self.update_player()
        self.draw(self.player)
        if gegner == 0:
            self.won = True
        if self.won == True or self.player.tot == True:
            self.end = True

    def statistiken(self): 
        self.zeit_punkte = 1800 - int(self.runtime/10)
        self.gegner_punkte = gegner_eliminiert * 100
        self.objekt_punkte = self.objekte_eingesammelt * 50
        self.bombenpunkte = self.bombenplatziert * 25
        self.bombenanzahlpunkte = bombenanzahl * 50

        self.max_zeit_punkte = 1800
        self.max_gegner_punkte = gegner_eliminiert * 100
        self.max_objekt_punkte = (self.sprengbarescount*0.08*50) + (self.sprengbarescount*0.05*50)
        self.max_bombenpunkte = ((self.runtime / 180) * (self.sprengbarescount*0.08*25)) * 10
        self.max_bombenanzahlpunkte = (self.sprengbarescount*0.08*25) * 30

        self.maximalpunkte = int(self.max_zeit_punkte + self.max_gegner_punkte + self.max_objekt_punkte + self.max_bombenpunkte + self.max_bombenanzahlpunkte)
        self.punkte = self.zeit_punkte + self.gegner_punkte + self.objekt_punkte + self.bombenanzahlpunkte + self.bombenpunkte
        
        #sachen
        self.oben_linie = pygame.rect.Rect(0,70,800,1)
        pygame.draw.rect(self.display_surface, (255,255,255), self.oben_linie)
        if self.player.tot == True:
            textfeld("Du bist gestorben", "center", 5, self.display_surface, 60)
        elif gegner == 0:
            textfeld("Level gewonnen!", "center", 5, self.display_surface, 60)
        textfeld("Statistiken", "center", 80, self.display_surface, 40)

        textfeld("Punkte", 200,150,self.display_surface, 20)
        textfeld(self.punkte,300,150,self.display_surface, 20)
        textfeld("Objekte eingesammelt", 200, 210, self.display_surface, 20)
        textfeld(self.objekte_eingesammelt, 300, 210, self.display_surface, 20)
        textfeld("Gegner eliminiert", 200, 270, self.display_surface, 20)
        textfeld(gegner_eliminiert, 300, 270, self.display_surface, 20)
        textfeld("Bomben platziert", 570, 270, self.display_surface, 20)
        textfeld(self.bombenplatziert, 670, 270, self.display_surface, 20)
        textfeld("Zeit", 570, 150, self.display_surface, 20)
        textfeld(int(self.runtime/60), 670, 150, self.display_surface, 20)
        textfeld("Sekunden", 760, 150, self.display_surface, 20)
        textfeld("Gesundheit übrig", 570, 210, self.display_surface, 20)
        textfeld((str(self.player.hp) + '/' + str(5)), 670, 210, self.display_surface, 20)