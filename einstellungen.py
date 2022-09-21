import pygame

#generell wird b für breite/horizontalen abstand verwendet und h für höhe/vertikalen abstand

bListe = [] #Liste für die breite der map
hListe = [] #Liste für die höhe der map
fListe = hListe
Levelb = len(bListe)
Levelh = len(hListe)

realFensterBreite = 1600
LevelFensterBreite = 1200
FensterHoehe = 900
feld_pixel = 32
feld_pixele = 32
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