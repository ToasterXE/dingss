import pygame
import os
from einstellungen import *

lebensanzeige = pygame.image.load(os.path.join("dateien", "lebensanzeigerahmen.png"))
slowness_potionImg32 = pygame.image.load(os.path.join("dateien", "slowness_potion.png"))
speed_potionImg32 = pygame.image.load(os.path.join("dateien","speed_potion.png"))
counterleiste = pygame.image.load(os.path.join("dateien", "counterleiste.png"))

playervorneImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_vorne.png")),(feld_pixel, feld_pixel))
playerobenImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_oben.png")),(feld_pixel, feld_pixel))
playeruntenImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_unten.png")),(feld_pixel, feld_pixel))
playerrechtsImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_rechts.png")), (feld_pixel, feld_pixel))
playerlinksImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_links.png")),(feld_pixel, feld_pixel))
playerhit_image = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_hit.png")),(feld_pixel, feld_pixel))

player_godmodeImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_godmode.png")),(feld_pixel,feld_pixel))

player_godmodeImg32 = pygame.image.load(os.path.join("dateien", "player_godmode.png"))
playervorneImg32 = pygame.image.load(os.path.join("dateien", "player_vorne.png"))
playerobenImg32 = pygame.image.load(os.path.join("dateien", "player_oben.png"))
playeruntenImg32 = pygame.image.load(os.path.join("dateien", "player_unten.png"))
playerrechtsImg32 = pygame.image.load(os.path.join("dateien", "player_rechts.png"))
playerlinksImg32 = pygame.image.load(os.path.join("dateien", "player_links.png"))
playerhit_image32 = pygame.image.load(os.path.join("dateien", "player_hit.png"))

bombeboost_Img = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe_verstärkung.png")),(feld_pixel,feld_pixel))
slowness_potionImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "slowness_potion.png")),(feld_pixel,feld_pixel))
speed_potionImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien","speed_potion.png")),(feld_pixel,feld_pixel))
bombe_objektImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien","bombe_objekt.png")),(feld_pixel,feld_pixel))
hp_boostImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "hp_boost.png")),(feld_pixel, feld_pixel))

bildImg = pygame.transform.scale(pygame.image.load((os.path.join("dateien", "bild.png"))),(feld_pixel * 14, feld_pixel * 12))
leerImg = pygame.image.load((os.path.join("dateien", "leer.png")))
nichtsImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien","nichts.png")),(feld_pixel, feld_pixel))
borderImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "border.png")),(feld_pixel,feld_pixel))
sprengbaresImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "sprengbares.png")),(feld_pixel, feld_pixel))
leerImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "leer.png")),(feld_pixel, feld_pixel))
wegraeumbaresImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "wegräumbares.png")),(feld_pixel, feld_pixel))

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

bombeImg1_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg2_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg3_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg4_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg5_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg6_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg7_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg8_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg9_verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg10_verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung1.png")),(feld_pixel, feld_pixel))
bombeImg11_verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung1.png")),(feld_pixel, feld_pixel))
bombeImg12_verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung1.png")),(feld_pixel, feld_pixel))

bombeImg1_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg2_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg3_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg4_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg5_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg6_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg7_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg8_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg9_verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg10_verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung2.png")),(feld_pixel, feld_pixel))
bombeImg11_verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung2.png")),(feld_pixel, feld_pixel))
bombeImg12_verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung2.png")),(feld_pixel, feld_pixel))

bombeImg1_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg2_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg3_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg4_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg5_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg6_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg7_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg8_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg9_verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg10_verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung3.png")),(feld_pixel, feld_pixel))
bombeImg11_verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung3.png")),(feld_pixel, feld_pixel))
bombeImg12_verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung3.png")),(feld_pixel, feld_pixel))

bombeImg1_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg2_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg3_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg4_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg5_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg6_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg7_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg8_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg9_verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg10_verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung4.png")),(feld_pixel, feld_pixel))
bombeImg11_verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung4.png")),(feld_pixel, feld_pixel))
bombeImg12_verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung4.png")),(feld_pixel, feld_pixel))

explosionsImg1 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel, feld_pixel))
explosionsImg2 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel+ 2, feld_pixel+2))
explosionsImg4 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel, feld_pixel))
explosionsImg5 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel+2, feld_pixel+2))
explosionsImg7 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel, feld_pixel))
explosionsImg8 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel+2, feld_pixel+2))
explosionsImg10 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel, feld_pixel))
explosionsImg11 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel+2, feld_pixel+2))

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

feld_pixel = 32
player32_godmodeImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "player_godmode.png")),(feld_pixel,feld_pixel))
bombeImg1_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg2_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg3_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg4_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg5_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg6_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg7_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg8_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg9_32verstärkung1  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung1.png" )),(feld_pixel, feld_pixel))
bombeImg10_32verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung1.png")),(feld_pixel, feld_pixel))
bombeImg11_32verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung1.png")),(feld_pixel, feld_pixel))
bombeImg12_32verstärkung1 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung1.png")),(feld_pixel, feld_pixel))

bombeImg1_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg2_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg3_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg4_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg5_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg6_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg7_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg8_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg9_32verstärkung2  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung2.png" )),(feld_pixel, feld_pixel))
bombeImg10_32verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung2.png")),(feld_pixel, feld_pixel))
bombeImg11_32verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung2.png")),(feld_pixel, feld_pixel))
bombeImg12_32verstärkung2 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung2.png")),(feld_pixel, feld_pixel))

bombeImg1_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg2_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg3_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg4_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg5_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg6_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg7_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg8_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg9_32verstärkung3  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung3.png" )),(feld_pixel, feld_pixel))
bombeImg10_32verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung3.png")),(feld_pixel, feld_pixel))
bombeImg11_32verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung3.png")),(feld_pixel, feld_pixel))
bombeImg12_32verstärkung3 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung3.png")),(feld_pixel, feld_pixel))

bombeImg1_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe1_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg2_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe2_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg3_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe3_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg4_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe4_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg5_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe5_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg6_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe6_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg7_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe7_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg8_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe8_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg9_32verstärkung4  = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe9_verstärkung4.png" )),(feld_pixel, feld_pixel))
bombeImg10_32verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe10_verstärkung4.png")),(feld_pixel, feld_pixel))
bombeImg11_32verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe11_verstärkung4.png")),(feld_pixel, feld_pixel))
bombeImg12_32verstärkung4 = pygame.transform.scale(pygame.image.load(os.path.join("bomben", "bombe12_verstärkung4.png")),(feld_pixel, feld_pixel))

verstärkung_leerImg = pygame.image.load(os.path.join("dateien", "verstärkung_leer.png"))
objekt_leerImg = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "objekt_leer.png")),(feld_pixel,feld_pixel))
bombeboost_32Img = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe_verstärkung.png")),(feld_pixel,feld_pixel))
bombe_objekt32Img = pygame.transform.scale(pygame.image.load(os.path.join("dateien","bombe_objekt.png")),(feld_pixel,feld_pixel))
bombe32Img1  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe1.png" )),(feld_pixel, feld_pixel))
bombe32Img2  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe2.png" )),(feld_pixel, feld_pixel))
bombe32Img3  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe3.png" )),(feld_pixel, feld_pixel))
bombe32Img4  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe4.png" )),(feld_pixel, feld_pixel))
bombe32Img5  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe5.png" )),(feld_pixel, feld_pixel))
bombe32Img6  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe6.png" )),(feld_pixel, feld_pixel))
bombe32Img7  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe7.png" )),(feld_pixel, feld_pixel))
bombe32Img8  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe8.png" )),(feld_pixel, feld_pixel))
bombe32Img9  = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe9.png" )),(feld_pixel, feld_pixel))
bombe32Img10 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe10.png")),(feld_pixel, feld_pixel))
bombe32Img11 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe11.png")),(feld_pixel, feld_pixel))
bombe32Img12 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "bombe12.png")),(feld_pixel, feld_pixel))

explosions32Img1 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel, feld_pixel))
explosions32Img2 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion1.png")),(feld_pixel+ 2, feld_pixel+2))
explosions32Img4 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel, feld_pixel))
explosions32Img5 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion2.png")),(feld_pixel+2, feld_pixel+2))
explosions32Img7 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel, feld_pixel))
explosions32Img8 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion3.png")),(feld_pixel+2, feld_pixel+2))
explosions32Img10 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel, feld_pixel))
explosions32Img11 = pygame.transform.scale(pygame.image.load(os.path.join("dateien", "explosion4.png")),(feld_pixel+2, feld_pixel+2))

bombe_objekt_1 = pygame.image.load(os.path.join("dateien", "bombe_objekt_verstärkt1.png"))
bombe_objekt_2 = pygame.image.load(os.path.join("dateien", "bombe_objekt_verstärkt2.png"))
bombe_objekt_3 = pygame.image.load(os.path.join("dateien", "bombe_objekt_verstärkt3.png"))
bombe_objekt_4 = pygame.image.load(os.path.join("dateien", "bombe_objekt_verstärkt4.png"))

feld_pixel = feld_pixele

bomben_objekte = [bombe_objekt32Img, bombe_objekt_1, bombe_objekt_2, bombe_objekt_3, bombe_objekt_4, bombe_objekt_4]

bombenSpritesverst1 = [bombeImg1_32verstärkung1, bombeImg2_32verstärkung1,bombeImg3_32verstärkung1,bombeImg4_32verstärkung1,bombeImg5_32verstärkung1,bombeImg6_32verstärkung1,
bombeImg7_32verstärkung1,bombeImg8_32verstärkung1,bombeImg9_32verstärkung1,bombeImg10_32verstärkung1,bombeImg11_32verstärkung1,bombeImg12_32verstärkung1]

bombenSpritesverst2 = [bombeImg1_32verstärkung2, bombeImg2_32verstärkung2,bombeImg3_32verstärkung2,bombeImg4_32verstärkung2,bombeImg5_32verstärkung2,bombeImg6_32verstärkung2,
bombeImg7_32verstärkung2,bombeImg8_32verstärkung2,bombeImg9_32verstärkung2,bombeImg10_32verstärkung2,bombeImg11_32verstärkung2,bombeImg12_32verstärkung2]

bombenSpritesverst3 = [bombeImg1_32verstärkung3, bombeImg2_32verstärkung3,bombeImg3_32verstärkung3,bombeImg4_32verstärkung3,bombeImg5_32verstärkung3,bombeImg6_32verstärkung3,
bombeImg7_32verstärkung3,bombeImg8_32verstärkung3,bombeImg9_32verstärkung3,bombeImg10_32verstärkung3,bombeImg11_32verstärkung3,bombeImg12_32verstärkung3]

bombenSpritesverst4 = [bombeImg1_32verstärkung4, bombeImg2_32verstärkung4,bombeImg3_32verstärkung4,bombeImg4_32verstärkung4,bombeImg5_32verstärkung4,bombeImg6_32verstärkung4,
bombeImg7_32verstärkung4,bombeImg8_32verstärkung4,bombeImg9_32verstärkung4,bombeImg10_32verstärkung4,bombeImg11_32verstärkung4,bombeImg12_32verstärkung4]

bomben32Sprites = [bombe32Img1,bombe32Img2,bombe32Img3,bombe32Img4,bombe32Img5,bombe32Img6,bombe32Img7,bombe32Img8,bombe32Img9,bombe32Img10,bombe32Img11,bombe32Img12]

explosionspritese = [bomben32Sprites, bombenSpritesverst1, bombenSpritesverst2, bombenSpritesverst3, bombenSpritesverst4]