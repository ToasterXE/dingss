import random
sprengbaresDingsTeilListe = [[],[],[],[],[],[]]

def inrange(ycoord,xcoord,Levelb, Levelh):
    if ycoord < Levelh and xcoord < Levelb:
        if ycoord > 0 and xcoord > 0:
            return True

class sdings(): #sprengbaresdings
    def __init__(self, hindex, bindex, sListe, Levelb, Levelh):
        self.midx = bindex
        self.midy = hindex
        self.size = random.randint(1,5)
        self.Liste = sListe
        self.Levelb = Levelb
        self.Levelh = Levelh

    def gen(self):
        global fListe
        i = 0
        while i <= self.size:
            typlen = len(sprengbaresDingsTeilListe[i])
            typlenc = 0
            while typlenc < typlen:
                ycoord = self.midy + sdtListeNamen[sprengbaresDingsTeilListe[i][typlenc]].yabstand
                xcoord = self.midx + sdtListeNamen[sprengbaresDingsTeilListe[i][typlenc]].xabstand
                if inrange(ycoord,xcoord,self.Levelb,self.Levelh):
                    self.Liste[ycoord][xcoord] = 20 + i
                typlenc += 1
            i+=1

class sdt():    #sprengbaresdingsteil
    def __init__(self, typ, xabstand, yabstand, num):
        self.typ = typ
        self.xabstand = xabstand
        self.yabstand = yabstand
        self.num = num
        sprengbaresDingsTeilListe[typ].append(self.num)

t0 = sdt(0,0,0,0)
t1 = sdt(1,1,0,1)
t2 = sdt(1,-1,0,2)
t3 = sdt(1,0,1,3)
t4 = sdt(1,0,-1,4)
t5 = sdt(2,2,0,5)
t6 = sdt(2,2,1,6)
t7 = sdt(2,2,-1,7)
t8 = sdt(2,1,1,8)
t9 = sdt(2,1,-1,9)
t10 = sdt(2,1,2,10)
t11 = sdt(2,1,-2,11)
t12 = sdt(2,-2,0,12)
t13 = sdt(2,-2,1,13)
t14 = sdt(2,-2,-1,14)
t15 = sdt(2,-1,1,15)
t16 = sdt(2,-1,-1,16)
t17 = sdt(2,-1,2,17)
t18 = sdt(2,-1,-2,18)
t19 = sdt(2,0,2,19)
t20 = sdt(2,0,-2,20)
t21 = sdt(3,3,0,21)
t22 = sdt(3,3,1,22)
t23 = sdt(3,3,-1,23)
t24 = sdt(3,-3,0,24)
t25 = sdt(3,-3,1,25)
t26 = sdt(3,-3,-1,26)
t27 = sdt(3,0,3,27)
t28 = sdt(3,1,3,28)
t29 = sdt(3,-1,3,29)
t30 = sdt(3,0,-3,30)
t31 = sdt(3,1,-3,31)
t32 = sdt(3,-1,-3,32)
t33 = sdt(3,2,2,33)
t34 = sdt(3,2,-2,34)
t35 = sdt(3,-2,2,35)
t36 = sdt(3,-2,-2,36)
t37 = sdt(4,4,0,37)
t38 = sdt(4,4,1,38)
t39 = sdt(4,4,-1,39)
t40 = sdt(4,-4,0,40)
t41 = sdt(4,-4,1,41)
t42 = sdt(4,-4,-1,42)
t43 = sdt(4,0,4,43)
t44 = sdt(4,1,4,44)
t45 = sdt(4,-1,4,45)
t46 = sdt(4,0,-4,46)
t47 = sdt(4,1,-4,47)
t48 = sdt(4,-1,-4,48)
t49 = sdt(4,3,2,49)
t50 = sdt(4,3,3,50)
t51 = sdt(4,2,3,51)
t52 = sdt(4,-3,2,52)
t53 = sdt(4,-3,3,53)
t54 = sdt(4,-2,3,54)
t55 = sdt(4,3,-2,55)
t56 = sdt(4,3,-3,56)
t57 = sdt(4,2,-3,57)
t58 = sdt(4,-3,-2,58)
t59 = sdt(4,-3,-3,59)
t60 = sdt(4,-2,-3,60)
t61 = sdt(5,5,0,61)
t62 = sdt(5,5,1,62)
t63 = sdt(5,5,-1,63)
t64 = sdt(5,-5,0,64)
t65 = sdt(5,-5,1,65)
t66 = sdt(5,-5,-1,66)
t67 = sdt(5,0,5,67)
t68 = sdt(5,1,5,68)
t69 = sdt(5,-1,5,69)
t70 = sdt(5,0,-5,70)
t71 = sdt(5,1,-5,71)
t72 = sdt(5,-1,-5,72)
t73 = sdt(5,3,4,73)
t74 = sdt(5,3,-4,74)
t75 = sdt(5,-3,4,75)
t76 = sdt(5,-3,-4,76)
t77 = sdt(5,4,3,77)
t78 = sdt(5,4,-3,78)
t79 = sdt(5,-4,3,79)
t80 = sdt(5,-4,-3,80)
t81 = sdt(5,2,4,81)
t82 = sdt(5,2,-4,82)
t83 = sdt(5,-2,4,83)
t84 = sdt(5,-2,-4,84)
t85 = sdt(5,4,2,85)
t86 = sdt(5,4,-2,86)
t87 = sdt(5,-4,2,87)
t88 = sdt(5,-4,-2,88)

#print(sprengbaresDingsTeilListe)
sdtListeNamen = [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,
           t41,t42,t43,t44,t45,t46,t47,t48,t49,t50,t51,t52,t53,t54,t55,t56,t57,t58,t59,t60,t61,t62,t63,t64,t65,t66,t67,t68,t69,t70,t71,t72,t73,t74,t75,t76,t77,t78,t79,t80,
           t81,t82,t83,t84,t85,t86,t87,t88]
