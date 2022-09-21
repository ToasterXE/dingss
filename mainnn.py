import pygame
from maps import *
from level import *

hintergrundImg = pygame.transform.scale(pygame.image.load((os.path.join("dateien", "hintergrund.png"))),(windowBreite,windowHoehe))

pygame.font.init()
window = pygame.display.set_mode((windowBreite, windowHoehe))
pygame.display.set_caption("dingss")
font = pygame.font.SysFont("candara", 30)

mouse_clicked = False
def button(name, links, oben, breite, hoehe, color, color_hover,linecolor):
    buttonSchrift = font.render(name, True, (230, 230, 230))
    buttonSchrift_rect = buttonSchrift.get_rect(center = (links + breite / 2, oben + hoehe / 2))
    linie_oben = pygame.rect.Rect(links,oben,breite,2)
    linie_links = pygame.rect.Rect(links,oben,2,hoehe)
    linie_unten = pygame.rect.Rect(links,(oben+hoehe-2),breite,2)
    linie_rechts = pygame.rect.Rect((links+breite-2),oben,2,hoehe)
    name = pygame.Rect(links, oben, breite, hoehe)
    mausPos = pygame.mouse.get_pos()
    
    pygame.draw.rect(window, color, name)
    pygame.draw.rect(window, linecolor, linie_oben)
    pygame.draw.rect(window, linecolor, linie_links)
    pygame.draw.rect(window, linecolor, linie_unten)
    pygame.draw.rect(window, linecolor, linie_rechts)
    window.blit(buttonSchrift, buttonSchrift_rect)

    if name.collidepoint(mausPos):
        pygame.draw.rect(window, color_hover, name)
        window.blit(buttonSchrift, buttonSchrift_rect)
        if pygame.mouse.get_pressed()[0] == True:
            return True

clock = pygame.time.Clock()
i = 0
level_counter = 1


def level_count(zahl):
    if zahl == 1:
        return Level1_map
    if zahl == 2:
        return Level2_map
    if zahl == 3:
        return Level3_map
    else:
        return Level1_map
        

def main_menu():
    global level_counter
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
        window.blit(hintergrundImg,(0,0))
        if level_counter == 1:
            if button("Start", 300, 100, 200, 80, (50,50,50), (70,70,70), (20,20,20)) == True:    
                level_main(Level1_map)

        else:
            if button ("Nächstet Level", 250, 100, 300, 80, (50,50,50), (70,70,70), (20,20,20)) == True:
                    level_main(level_count(level_counter))

        pygame.display.update()


def level_main(map):
    global i, level_counter
    run = True
    while run:
        i += 1
        if i == 1:
            level = Level(map)
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    level.dings()
        
        #print (level.won)
        window.fill((20,20,20))
        
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
            if level.won == True:
                if button("weiter", 650, 380, 100, 50, (50,50,50), (70,70,70), (30,30,30)) == True:
                    i = 0
                    level_counter += 1
                    level_main(level_count(level_counter))
                if button("Hauptmenü",300,380,200,50,(50,50,50), (70,70,70), (30,30,30)) == True:
                    i = 0
                    level_counter += 1
                    main_menu() 
            else:
                if button("nochmal versuchen", 530, 380, 250, 50, (50,50,50), (70,70,70), (30,30,30)) == True:
                    i = 0
                    level_main(level_count(level_counter))
                if button("Hauptmenü",300,380,200,50,(50,50,50), (70,70,70), (30,30,30)) == True:
                    i = 0
                    main_menu()

        if level.end == False:
            level.run()

                #main_menu()
        pygame.display.update()

main_menu()
#level_main(Level4_map)