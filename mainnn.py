import pygame
from maps import *
from level import *
from einstellungen import *

hintergrundImg = pygame.transform.scale(pygame.image.load((os.path.join("dateien", "hintergrund.png"))),(realFensterBreite,FensterHoehe))

pygame.font.init()
pygame.display.set_caption("dingss")
pygame.display.set_icon(pygame.image.load(os.path.join("dateien", "player_vorne.png")))
font = pygame.font.SysFont("candara", 80)
#tasten
auswahl_taste = pygame.K_l
bomben_taste = pygame.K_p

#wurde programmiert für die nutzung mit der maus, dann aber auf den Spielautomaten angepasst
class button():
    def __init__(self, name, links, oben, breite, hoehe):
        self.name = name
        self.schrift = font.render(name, True, (230,230,230))
        self.schrift_rect = self.schrift.get_rect(center = (links + breite / 2, oben + hoehe / 2))
        self.linie_oben = pygame.Rect(links, oben, breite, 2)
        self.linie_links = pygame.Rect(links, oben, 2, hoehe)
        self.linie_unten = pygame.Rect(links, (oben + hoehe - 2), breite, 2)
        self.linie_rechts = pygame.Rect((links + breite - 2), oben, 2, hoehe)
        self.rect = pygame.Rect(links, oben, breite, hoehe)
        self.color = (50,50,50)
        self.color2 = (32,32,32)
        self.true = False                                                                                                                                  

    def update(self):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, self.color2, self.linie_links)
        pygame.draw.rect(window, self.color2, self.linie_oben)
        pygame.draw.rect(window, self.color2, self.linie_rechts)
        pygame.draw.rect(window, self.color2, self.linie_unten)
        window.blit(self.schrift, self.schrift_rect)

clock = pygame.time.Clock()
level_counter = 1

def level_count(zahl):
    if zahl == 1:
        return Level4_map  
    
    if zahl == 2:
        return Level5_map
    if zahl == 3:
        return Level6_map
    if zahl == 4:
        return Level7_map
    if zahl == 5:
        return Level8_map
    if zahl > 5:
        zahl = 1
        return (level_count(zahl))



#init_counter = 0        
start = button("Start", realFensterBreite / 2 - 150, FensterHoehe / 2 - 50, 300, 100) 
weiter = button("weiter", 600, 700, 400, 100)
retry_button = button("nochmal versuchen", 400, 700, 800, 100)
hauptmenu = button("Hauptmenü", 500, 700, 600, 100)
spielstart = False
run = True

def main_menu():
    global level_counter, spielstart, run
    while run:
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == auswahl_taste:
                    spielstart = True 

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        window.blit(hintergrundImg, (0,0))

        start.update()
        pygame.display.update()

        if spielstart == True:   
            level_main(level_count(level_counter))      #hier wird zu einem anderen main loop gewechselt 



def level_main(map):
    global level_counter, run
    level = Level(map)
    run = True
    while run:     
        clock.tick(60)


      #  if init_counter == 1:
       #     level = Level(map)
        
        window.fill((20,20,20)) 
        keys_pressed = pygame.key.get_pressed()
        if level.end == True:
            level.statistiken()

            #sichtbare spritegruppen
            sichtbareSprites.empty() 
            bessereSprites.empty()
            gutereSprites.empty()
            collisionSprites.empty()   
            bombenSprites.empty()    
            wegraeumbareSprites.empty()
            explosionSprites.empty()
            sprengbaresSprites.empty()
            speedSprites.empty()
            slownessSprites.empty()
            speedcounterSprites.empty()
            slownesscounterSprites.empty()
            bombenobjekteSprites.empty()
            alienSprites.empty()
            explosionsListe.clear()
            hpboostSprites.empty()
            bombeboostSprites.empty()
            infofeldexplosionen.empty()
            aliencollisionSprites.empty()

            if level.won == True:
                if level_counter < 3:
                    weiter.update()
                    if keys_pressed[auswahl_taste]:
                        weiter.true = True
                        level_counter += 1
                        level_main(level_count(level_counter))
            
                elif level_counter >= 3:
                    hauptmenu.update()
                    if keys_pressed[auswahl_taste]:
                        hauptmenu.true = True
                        level_counter += 0
                        main_menu()

            else:
                retry_button.update()
                if keys_pressed[auswahl_taste]:
                    retry_button.true = True
                    level_main(level_count(level_counter))

        if level.end == False:
            level.run()

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    level.godmode_update()

            if event.type ==  pygame.KEYDOWN:       #events wie KEYDOWN können nur im main loop aufgerufen werden (?)
                if event.key == bomben_taste:
                    if level.end == False:
                        level.dings()
        
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

     #   init_counter += 1
if run == True:
    #main_menu()
    level_main(test21323)