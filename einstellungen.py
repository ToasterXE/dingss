import pygame

#generell wird b für breite/horizontalen abstand verwendet und h für höhe/vertikalen abstand
realFensterBreite = 1600
LevelFensterBreite = int(realFensterBreite*0.125)
FensterHoehe = int(realFensterBreite*(9/16))
feld_pixel = int(realFensterBreite/50)
feld_pixele = int(realFensterBreite/50)
player_speed = max(int(realFensterBreite/300),1)
alien2_speed = max(int(realFensterBreite/800),1)
max_speed = max(int(realFensterBreite/380),1)
min_speed = max(int(realFensterBreite/500),1)


bListe = [] #Liste für die breite der map
hListe = [] #Liste für die höhe der map
fListe = hListe
Levelb = len(bListe)
Levelh = len(hListe)

seed = "12345"
buttonColor = (50,50,50)
hoverColor = (35,35,35)
bgColor = (20,20,20)

window = pygame.display.set_mode((realFensterBreite, FensterHoehe))
bombenart = 0

#sichtbare spritegruppen
sichtbareSprites = pygame.sprite.Group()
bessereSprites = pygame.sprite.Group()
gutereSprites = pygame.sprite.Group()
infofeldexplosionen = pygame.sprite.Group()

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
hpboostSprites = pygame.sprite.Group()
bombeboostSprites = pygame.sprite.Group()
aliencollisionSprites = pygame.sprite.Group()

spritegroups = [sichtbareSprites,bessereSprites,gutereSprites,infofeldexplosionen,collisionSprites,bombenSprites,wegraeumbareSprites,explosionSprites,sprengbaresSprites,speedSprites,slownessSprites,
                speedcounterSprites,slownesscounterSprites,bombenobjekteSprites,alienSprites,hpboostSprites,bombeboostSprites,aliencollisionSprites]