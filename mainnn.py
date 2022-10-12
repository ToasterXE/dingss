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
updatelist = []
class button():
    def __init__(self, name, links, oben, breite, hoehe, teste, nummer):
        self.name = name
        self.teste = teste
        if teste:
            self.num = nummer
            updatelist.append(self)
        self.schrift = font.render(name, True, (230,230,230))
        self.schrift_rect = self.schrift.get_rect(center = (links + breite / 2, oben + hoehe / 2))
        self.linie_oben = pygame.Rect(links, oben, breite, 2)
        self.linie_links = pygame.Rect(links, oben, 2, hoehe)
        self.linie_unten = pygame.Rect(links, (oben + hoehe - 2), breite, 2)
        self.linie_rechts = pygame.Rect((links + breite - 2), oben, 2, hoehe)
        self.rect = pygame.Rect(links, oben, breite, hoehe)
        self.color = (50,50,50)
        self.col_hover = (40,40,40)
        self.color2 = (32,32,32)
        self.reaction = False                                                                                                                                  
        

    def update(self):
        global selected_levelreihenfolge
        maus_pos = pygame.mouse.get_pos()
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, self.color2, self.linie_links)
        pygame.draw.rect(window, self.color2, self.linie_oben)
        pygame.draw.rect(window, self.color2, self.linie_rechts)
        pygame.draw.rect(window, self.color2, self.linie_unten)
        window.blit(self.schrift, self.schrift_rect)
        self.color = (50,50,50)
        if self.teste:
            if not selected_levelreihenfolge == levelreihenfolgen[self.num]:
                self.reaction = False
        if self.rect.collidepoint(maus_pos):
            self.color = self.col_hover
            if pygame.mouse.get_pressed()[0] == 1:
                if self.reaction == False:
                    if self.teste:
                        selected_levelreihenfolge = levelreihenfolgen[self.num]
                        update_minimapSprites()
                    self.reaction = True
                    self.color = self.color2


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
selected_levelreihenfolge = levelreihenfolgen[0]        
start = button("Start", realFensterBreite / 2 - 150, FensterHoehe / 2 - 50, 300, 100, False, 0) 
weiter = button("weiter", 600, 700, 400, 100, False, 0)
retry_button = button("nochmal versuchen", 400, 700, 800, 100,False,0)
hauptmenu = button("Hauptmenü", 500, 700, 600, 100, False, 0)
spielstart = False
run = True
minimapSprites = pygame.sprite.Group()
nextxabstand = 35
maxmaphoehe = 0
nextyabstand = 150

def create_minimap(level):
    global nextxabstand, nextyabstand, maxmaphoehe
    mapBreite = len(level[0]) * 12+1
    mapHoehe = len(level) * 12 +1
    if mapBreite + nextxabstand > 1585:
        nextxabstand = 35
        nextyabstand += maxmaphoehe + 35
    else:
        maxmaphoehe = max(maxmaphoehe, mapHoehe)

    for spalte_index, spalte in enumerate(level):
        for zeile_index, spalte in enumerate(spalte):
            x = zeile_index * 12 + nextxabstand
            y = spalte_index * 12 + nextyabstand
            if spalte == 1:
                border((x,y),[minimapSprites])
            if spalte == 5:
                spawnfeld((x,y),[minimapSprites])              
            if spalte == 2:
                sprengbares((x,y),[minimapSprites])
            if spalte == 3:
                wegraeumbares((x,y), [minimapSprites])
            if spalte == 10:
                alien1((x,y),[minimapSprites])
            if spalte == 11:
                alien2((x,y),[minimapSprites],window)
            if spalte == 12:
                alien3((x,y),[minimapSprites])
            if spalte == 50:
                bombe_objekt((x,y), [minimapSprites])        
            if spalte == 51:
                slowness_potion((x,y), [minimapSprites])
            if spalte == 52:
                speed_potion((x,y),[minimapSprites])
            if spalte == 53:
                hp_boost((x,y),[minimapSprites])
    nextxabstand += mapBreite + 35



def update_minimapSprites():
    global nextxabstand, nextyabstand, maxmaphoehe
    nextxabstand = 35
    nextyabstand = 150
    maxmaphoehe = 0
    minimapSprites.empty()
    for level in selected_levelreihenfolge:
        create_minimap(level)

elementcounter = 0
for element in levelreihenfolgen:
    button(str(elementcounter),15 + ((realFensterBreite-30) / (len(levelreihenfolgen) +1)) * elementcounter, 100, (realFensterBreite-30) / (len(levelreihenfolgen)+1),20,True, elementcounter)
    elementcounter += 1
print(elementcounter)
def levelauswahl_main():
    run = True
    while run:
        window.fill((20,20,20))
        for sprite in minimapSprites:
            sprite.image = pygame.transform.scale(sprite.image,(12,12))
        minimapSprites.draw(window)
        for button in updatelist:
            button.update()


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

def main_menu():
    global level_counter, spielstart, run
    while run:
        window.fill((20,20,20))

        start.update()
        pygame.display.update()

        if start.reaction == True:   
            level_main(level_count(level_counter))      #hier wird zu einem anderen main loop gewechselt 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


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
                        weiter.reaction = True
                        level_counter += 1
                        level_main(level_count(level_counter))
            
                elif level_counter >= 3:
                    hauptmenu.update()
                    if keys_pressed[auswahl_taste]:
                        hauptmenu.reaction = True
                        level_counter += 0
                        main_menu()

            else:
                retry_button.update()
                if keys_pressed[auswahl_taste]:
                    retry_button.reaction = True
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
    levelauswahl_main()
    # main_menu()
    #level_main(benediktslevel6)