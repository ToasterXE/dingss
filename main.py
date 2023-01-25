import pygame
from multiprocessing import Process, freeze_support
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
pygame.mixer.init()

class normal_button():
    def __init__(self, topleft, str, fn):
        self.schrift = font.render(str, True, (230,230,230))
        self.schrift_rect = self.schrift.get_rect(topleft = topleft)
        self.rect = pygame.rect.Rect(self.schrift_rect.left - 5, self.schrift_rect.top -5, self.schrift_rect.width + 10, self.schrift_rect.height + 10)
        self.color = (50,50,50)
        self.fn = fn
    def update(self):
        pygame.draw.rect(window, self.color, self.rect, border_radius=4)
        window.blit(self.schrift, self.schrift_rect)
        maus_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(maus_pos):
            self.color = (35,35,35)
            if pygame.mouse.get_pressed()[0] == 1:
                self.fn()
        else: 
            self.color = (50,50,50)

def level_main():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join("sound","level_music.mp3"))
    pygame.mixer.music.play(loops=-1)
    global level_counter, run
    map = level_count(level_counter)
    level = Level(map)
    run = True
    while run:     


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
                    level_main()

        if level.end == False:
            clock.tick(60)
            level.run()
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    level.godmode_update()

            if event.type ==  pygame.KEYDOWN: 
                if event.key == bomben_taste:
                    if level.end == False:
                        level.dings()
        
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

def levelauswahl_main():
    run = True
    while run:

        window.fill((20,20,20))
        for sprite in minimapSprites:
            window.blit(sprite.image, (sprite.rect.left, sprite.rect.top + scrollabstand))
        for button in updatelist:
            button.update()
        update_scrollbutton()
        zurückbutton.update()
        pygame.draw.rect(window,scrollrect_color,scrollrect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

start = normal_button((70,70), "Start", level_main)
levelselect = normal_button((70,220), "Select Levels", levelauswahl_main)

def main_menu():
    global level_counter, spielstart, run
    pygame.mixer.music.load(os.path.join("sound","main_menu.mp3"))
    pygame.mixer.music.play(loops=-1)
    while run:
        window.fill((20,20,20))
        start.update()
        levelselect.update()
        pygame.display.update()
    #hier wird zu einem anderen main loop gewechselt 

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

class levelselect_button():
    def __init__(self, name, links, oben, breite, hoehe, teste, nummer):
        self.name = name
        self.teste = teste
        if teste:
            self.num = nummer
            updatelist.append(self)
        self.schrift = font.render(name, True, (230,230,230))
        self.schrift_rect = self.schrift.get_rect(center = (links + breite / 2, oben + hoehe / 2))
        self.rect = pygame.Rect(links, oben - self.schrift_rect.height / 2, breite, self.schrift_rect.height)
        self.color = (50,50,50)
        self.col_hover = (40,40,40)
        self.color2 = (32,32,32)
        self.reaction = False                                                                                                                                  
        self.draw_schrift_rect = self.schrift.get_rect(center = (links + breite / 2, oben + hoehe / 2))
        self.draw_rect = pygame.Rect(links, oben - self.schrift_rect.height / 2, breite, self.schrift_rect.height)
   
    def update(self):
        global selected_levelreihenfolge
        self.draw_rect.top = self.rect.top + scrollabstand
        self.draw_schrift_rect.top = self.schrift_rect.top + scrollabstand
        maus_pos = pygame.mouse.get_pos()
        pygame.draw.rect(window, self.color, self.draw_rect,0,4)
        window.blit(self.schrift, self.draw_schrift_rect)
        self.color = (50,50,50)
        if self.teste:
            if not selected_levelreihenfolge == levelreihenfolgen[self.num]:
                self.reaction = False
        if self.draw_rect.collidepoint(maus_pos):
            self.color = self.col_hover
            if pygame.mouse.get_pressed()[0] == 1:
                if self.reaction == False:
                    if self.teste:
                        selected_levelreihenfolge = levelreihenfolgen[self.num]
                        update_minimapSprites()
                    self.reaction = True
                    self.color = self.color2


#init_counter = 0
weiter = levelselect_button("weiter", 600, 700, 400, 100, False, 0)
retry_button = levelselect_button("nochmal versuchen", 400, 700, 800, 100,False,0)
hauptmenu = levelselect_button("Hauptmenü", 500, 700, 600, 100, False, 0)
spielstart = False
run = True
minimapSprites = pygame.sprite.Group()
updatelist = []
selected_levelreihenfolge = levelreihenfolgen[0]        
nextxabstand = 35
maxmaphoehe = 0
nextyabstand = 0
scrollabstand = 0
zurückbutton = normal_button((1200,780), "zurück", main_menu)

def create_minimap(level):
    global nextxabstand, nextyabstand, maxmaphoehe, potmax
    mapBreite = len(level[0]) * 12+1
    mapHoehe = len(level) * 12 +1
    if mapBreite + nextxabstand > 1585:
        nextxabstand = 35
        nextyabstand += maxmaphoehe + 35
        maxmaphoehe = mapHoehe
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

scrollrect = pygame.rect.Rect(1525, 35, 50, 100)
scrollrect_color = (20,20,20)
scrolling = False
old_mouse = 0
multi = 0

def update_minimapSprites():
    global nextxabstand, nextyabstand, maxmaphoehe, selected_levelreihenfolge,scrollrect, multi, scrollabstand
    nextxabstand = 35
    nextyabstand = 138  #hier ändern
    maxmaphoehe = 0
    scrollabstand = 0
    minimapSprites.empty()
    for level in selected_levelreihenfolge:
        create_minimap(level)
    scrollrect = pygame.rect.Rect(1525, 25, 50, get_scrollrecthoehe())
    for sprite in minimapSprites:
        sprite.image = pygame.transform.scale(sprite.image,(12,12))

def get_scrollrecthoehe():  #dings
    global multi
    if nextyabstand + maxmaphoehe < 900:
        return 840
    e = 900 / (nextyabstand + maxmaphoehe)
    multi = ((nextyabstand + maxmaphoehe )) / 830 #- (830 * e)) 

    #print((nextyabstand + maxmaphoehe),830 * multi * e)
    return 830 * e - 35*e

def update_scrollbutton():
    global scrollrect_color, scrolling, scrollabstand, old_mouse, multi
    if not old_mouse:
        old_mouse = (0,0)
    maus_pos = pygame.mouse.get_pos()
    scrollrect_color = (50,50,50)
    if scrollrect.collidepoint(maus_pos):
            scrollrect_color = (70,70,70)
            if pygame.mouse.get_pressed()[0] == 1:
                scrolling = True  
            else:
                scrolling = False             
    else:
        scrolling = False     
    if scrolling:
        scrollabstand -= (maus_pos[1] - old_mouse[1]) * multi 
        scrollrect.top += maus_pos[1] - old_mouse[1] 
        if scrollrect.top <= 35:
            scrollrect.top = 35
            scrollabstand = 0
        if scrollrect.bottom >= 900-35:
            scrollrect.bottom = 900-35
            scrollabstand += (maus_pos[1] - old_mouse[1]) * multi           
    old_mouse = maus_pos


elementcounter = 0
for element in levelreihenfolgen:
    levelselect_button(str(elementcounter), 15 + 15 * elementcounter + ((realFensterBreite-30) / (len(levelreihenfolgen) +1))  * elementcounter, 68, (realFensterBreite-30) / (len(levelreihenfolgen)+1),20,True, elementcounter)
    elementcounter += 1
#print(elementcounter)
def level_count(zahl):
    if zahl >= len(selected_levelreihenfolge):
        zahl = 0

    return (selected_levelreihenfolge[zahl])
clock = pygame.time.Clock()
level_counter = 1




     #   init_counter += 1
if run == True:
    #levelauswahl_main()
    main_menu()
    #level_main(benediktslevel6)