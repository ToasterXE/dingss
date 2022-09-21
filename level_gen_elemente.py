import random
class element1():
    def __init__(self, map, startx, starty):
        self.map = map
        self.startx = startx
        self.starty = starty
        self.width = 1
        self.height = 1

    def gen(self):
        self.map[self.startx][self.starty] = 1

class element2():
    def __init__(self, map, startx, starty):
        self.map = map
        self.startx = startx
        self.starty = starty
        self.width = 2
        self.height = 2
    def gen(self):
        self.map[self.startx][self.starty] = 2
        self.map[self.startx + 1][self.starty] = 2
        self.map[self.startx][self.starty + 1] = 2
        self.map[self.startx + 1][self.starty +1] = 2

class element3():
    def __init__(self, map, startx, starty):
        self.map = map
        self.startx = startx
        self.starty = starty
        self.width = 6
        self.height = 6
        self.platzhalter = random.randint(1,4)
    def gen(self):
        i = 0
        while i < self.height:
            e = 0
            while e < self.width:
                if not self.map[self.startx - 1 + i][self.starty - 1 + e] == 0:
                    return False
                
                self.map[self.startx - 1 + i][self.starty - 1 + e] = 9
                e += 1

            i += 1
        
        #obere seite
        self.map[self.startx][self.starty] = 1
        self.map[self.startx + 1][self.starty] = 1
        self.map[self.startx + 2][self.starty] = 1
        self.map[self.startx + 3][self.starty] = 1
        #seiten
        self.map[self.startx][self.starty + 1] = 1
        self.map[self.startx][self.starty + 2] = 1
        self.map[self.startx + 3][self.starty + 1] = 1
        self.map[self.startx + 3][self.starty + 2] = 1
        #untere seite
        self.map[self.startx][self.starty + 3] = 1
        self.map[self.startx + 1][self.starty + 3] = 1
        self.map[self.startx + 2][self.starty + 3] = 1
        self.map[self.startx + 3][self.starty + 3] = 1

        if self.platzhalter == 1:
            #oben
            e = 0
            while e < self.width:
                self.map[self.startx + e - 1][self.starty - 1] = 0
                e += 1

        elif self.platzhalter == 2:
            #links
            i = 0
            while i < self.height:
                self.map[self.startx - 1][self.starty + i - 1] = 0
                i += 1

        elif self.platzhalter == 3:
            #unten
            e = 0
            while e < self.width:
                self.map[self.startx + e - 1][self.starty + self.height - 2] = 0
                e += 1

        elif self.platzhalter == 4:
            #rechts
            i = 0
            while i < self.height:
                self.map[self.startx + self.width - 2][self.starty + i - 1] = 0
                i += 1

class element4():
    def __init__(self, map, startx, starty):
        self.map = map
        self.startx = startx
        self.starty = starty
        self.width = 1
        self.height = 1
    def gen(self):
        self.map[self.startx][self.starty] = 2