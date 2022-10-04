import pygame
from einstellungen import *
from bilder import lebensanzeige,speed_potionImg32, explosionspritese, slowness_potionImg32, counterleiste, bombe_objekt32Img, bomben32Sprites, verstärkung_leerImg, bombeboost_32Img, bomben_objekte
pygame.font.init()
schrift20 = pygame.font.SysFont("candara", 40)
animiertebomben = 0
infoexplosionsliste = []
explodierendesachen = []
bombenExplosionsSprites = explosionspritese[0]
bombenObjektImg = bomben_objekte[0]

class infofeldbombe(pygame.sprite.Sprite):
    def __init__(self, xabstand, groups, bombenpos, fenster):
        super().__init__(groups)
        self.xabstand = xabstand - 1
        self.counter = 0
        self.bombenpos = bombenpos
        self.yabstand = self.xabstand // 7
        self.xabstand -= self.yabstand * 7
        self.fenster = fenster
        self.end = False
        self.num = xabstand - 1
        infoexplosionsliste.insert(self.num, self)
        self.image = bombenObjektImg
        self.rect = self.image.get_rect(topleft = (self.bombenpos.x + self.xabstand * 33, self.bombenpos.y + self.yabstand * 33))

    def explode(self):
        self.end = False
        infoexplosionsliste[self.num] = 0
        if not int(self.counter) >= len(bombenExplosionsSprites):
            self.image =  bombenExplosionsSprites[int(self.counter)]
            self.counter += 0.2
        else:
            self.end = True
            self.counter = 0
            self.image = bombenObjektImg
            infoexplosionsliste[self.num] = self

class infofeld():
    def __init__(self, hoehe, player, fenster, bombenanzahl):
        global animiertebomben, infoexplosionsliste, explodierendesachen
        explodierendesachen = []
        infoexplosionsliste = []
        animiertebomben = 0
        self.startx = realFensterBreite - 300
        self.breite = 300
        self.hoehe = hoehe
        self.bombenboostcounter = 0
        self.bombenanzahl = bombenanzahl
        self.animiertebomben = -1
        self.player = player
        self.fenster = fenster
        self.playerImgPos = pygame.math.Vector2(self.startx + 5 + int(self.breite/10), 35)
        self.lebensanzeigePos = pygame.math.Vector2(self.startx + 35, 90)
        self.speedpotionPos = pygame.math.Vector2(self.startx + 35, 150)
        self.slownesspotionPos = pygame.math.Vector2(self.startx + 35, 200)
        self.bombenPos = pygame.math.Vector2(self.startx + 35, 250)
        self.bg = pygame.rect.Rect(self.startx, 0, self.breite, self.hoehe)
        self.border = pygame.rect.Rect(self.startx + 5, 5, self.breite - 10, self.hoehe - 10)
        i = 1
        while i <= bombenanzahl:
            infofeldbombe(i, infofeldexplosionen, self.bombenPos, self.fenster)
            i += 1

    def createbombe(self):
        infofeldbombe(self.bombenanzahl, infofeldexplosionen, self.bombenPos, self.fenster)


    def update(self):
        #print (self.animiertebomben)
        #print (infoexplosionsliste)
        #print(self.animiertebomben, animiertebomben)
        #self.animiertebomben = animiertebomben
        pygame.draw.rect(self.fenster,(88,88,88),self.bg)
        pygame.draw.rect(self.fenster,(20,20,20),self.border)

        #spieler
        self.fenster.blit(self.player.image32, self.playerImgPos)
        player1 = schrift20.render("SPIELER1",False,(220,220,220))
        player1_rect = player1.get_rect(topleft = self.playerImgPos + (52,0))
        self.fenster.blit(player1, player1_rect)

        #lebensanzeige
        self.fenster.blit(lebensanzeige, self.lebensanzeigePos)
        breite = 22 * self.player.hp
        if self.player.hp > 10:
            breite = 220
        lebensanzeigerect = pygame.rect.Rect(self.lebensanzeigePos.x + 5, self.lebensanzeigePos.y + 5, breite, 37)
        pygame.draw.rect(self.fenster, (0,255,0), lebensanzeigerect)

        #speed/slowness anzeige
        counter = 0
        for potion_counter in speedcounterSprites:
            self.fenster.blit(speed_potionImg32,(self.speedpotionPos.x + counter * 40,self.speedpotionPos.y))
            self.fenster.blit(counterleiste,(self.speedpotionPos.x + counter * 40, self.speedpotionPos.y + 36))
            counterleisterect = pygame.rect.Rect(self.speedpotionPos.x + counter * 40 + 1, self.speedpotionPos.y + 37 , 30 - int(potion_counter.wert/20), 2)
            pygame.draw.rect(self.fenster, (183,0,255), counterleisterect)
            counter += 1
        
        counter = 0
        for potion_counter in slownesscounterSprites:
            self.fenster.blit(slowness_potionImg32,(self.slownesspotionPos.x + counter * 40, self.slownesspotionPos.y))
            self.fenster.blit(counterleiste,(self.slownesspotionPos.x + counter * 40, self.slownesspotionPos.y + 36))
            counterleisterect = pygame.rect.Rect(self.slownesspotionPos.x + counter * 40 + 1, self.slownesspotionPos.y + 37, 30 - int(potion_counter.wert/20), 2)
            pygame.draw.rect(self.fenster, (183,0,255), counterleisterect)
            counter += 1


        #bomben
        if self.animiertebomben >= 0:
            i = 0
            while i  < len(explodierendesachen):
                explodierendesachen[i].explode() 
                if explodierendesachen[i].end == True:
                    self.animiertebomben -= 1
                    del explodierendesachen[i]
                i += 1

        infofeldexplosionen.draw(self.fenster)

        #bombenverstärkung
        self.verstärkunganzeige_pos = pygame.math.Vector2(self.startx + 35, self.bombenPos.y + 50 + ((self.bombenanzahl - 1) // 7) * 40)
        self.fenster.blit(verstärkung_leerImg, (self.verstärkunganzeige_pos))
        i = 0
        while i < self.bombenboostcounter % 3:
            self.fenster.blit(bombeboost_32Img, (self.startx + 35 + i * 40, self.verstärkunganzeige_pos.y))
            i += 1
        if self.bombenboostcounter < 12:
            self.fenster.blit(bomben_objekte[self.bombenboostcounter//3 + 1], (self.verstärkunganzeige_pos.x + 156, self.verstärkunganzeige_pos.y))

    def bombe_explode(self):
        liste = True
        i = 0
        while liste == True:
            if i < len(infoexplosionsliste):
                if not infoexplosionsliste[i] == 0:
                    explodierendesachen.append(infoexplosionsliste[i])
                    liste = False
                else:
                    i += 1
            else:
                liste = False

    def update_bombenart(self, bombenart):
        global bombenObjektImg, bombenExplosionsSprites
        bombenObjektImg = bomben_objekte[bombenart]
        bombenExplosionsSprites = explosionspritese[bombenart]
        for bombe in infofeldexplosionen:
            bombe.image = bombenObjektImg        

