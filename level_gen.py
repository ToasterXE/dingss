from einstellungen import *
import random
from level import Level
from wahrscheinlichkeiten import *
from sdings import *

fListe = hListe

def gen_Liste():
    global Levelb, Levelh
    b = 0
    h = 0
    for b in range(random.randint(bListemin, bListemax)):
        bListe.append(0)
        b += 1
    for h in range(random.randint(hListemin, hListemax)):
        tempListe = bListe.copy()   #ansonsten beziehen sich alle Listen in der Breite auf bListe und sind daher identisch
        hListe.append(tempListe)
        h += 1
    Levelb = len(bListe)
    Levelh = len(hListe)


def gen_rand():
    b = 0
    h = 0
    while b < Levelb:
        fListe[0][b] = 1
        fListe[-1][b] = 1
        b += 1
    for h in range(Levelh):
        fListe[h][0] = 1
        fListe[h][-1] = 1
        h += 1
    	

def place_player():
    fListe[1][1] = 5

def gen_layer1():   #sprengbares wird in sListe generiert
    sListe = fListe
    count = 1
    while count <= random.randint(sdingscmin, sdingscmax):
        hindex = random.randint(1,Levelh - 2)
        bindex = random.randint(1,Levelb - 2)
        objekt = sdings(hindex, bindex, sListe, Levelb, Levelh)
        objekt.gen()
        count += 1

def gen_map():
    gen_Liste()
    gen_layer1()

    place_player()
    gen_rand()
    #print(fListe)


#print (Liste)
gen_map()
Level1 = Level(fListe)
clock = pygame.time.Clock()
def Levelrun():
    run = True
    while run:
        clock.tick(60)
        window.fill((20,20,20)) 
        Level1.run()
        pygame.display.update()

        for event in pygame.event.get():

        
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
Levelrun()