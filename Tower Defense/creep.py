import random

class Creep():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.vivant = True
        self.vie = 10  * self.parent.niveauVague
        self.cibleX = None
        self.cibleY = None
        self.angle = None
        self.vitesseX = 0
        self.vitesseY = 1
        self.rayon = 6
        self.collisionX1 = posX - self.rayon
        self.collisionY1 = posY - self.rayon
        self.collisionX2 = posX + self.rayon
        self.collisionY2 = posX + self.rayon
        self.couleur = "red"
        self.valeurArgent = 10 * self.parent.niveauVague
        self.dommageOverTime = []
        self.dommages = []
        self.currentRoute = None

    def CreepCible(self):
        if self.currentRoute is None:
            self.currentRoute = 0
        else:
            self.currentRoute += 1

        if self.currentRoute < len(self.parent.routes):
            if self.parent.routes[self.currentRoute].posX == self.parent.routes[self.currentRoute].posX2:
                self.cibleX = self.parent.routes[self.currentRoute].posX2
                self.cibleY = self.parent.routes[self.currentRoute].posY2

            else:
                self.cibleX = self.parent.routes[self.currentRoute].posX2
                self.cibleY = self.parent.routes[self.currentRoute].posY2

            if self.currentRoute == 1:
                self.vitesseX = 1
                self.vitesseY = 0
            elif self.currentRoute == 2:
                self.vitesseX = 0
                self.vitesseY = -1
            elif self.currentRoute == 3:
                self.vitesseX = 1
                self.vitesseY = 0
            elif self.currentRoute == 4:
                self.vitesseX = 0
                self.vitesseY = -1
            elif self.currentRoute == 5:
                self.vitesseX = -1
                self.vitesseY = 0
            elif self.currentRoute == 6:
                self.vitesseX = 0
                self.vitesseY = 1
            elif self.currentRoute == 7:
                self.vitesseX = 1
                self.vitesseY = 0

        else:
            self.parent.vie -= 1
            self.vie = 0

    def Mouvement(self):
        if self.parent.routes[self.currentRoute].posX == self.parent.routes[self.currentRoute].posX2:
            if self.cibleY - 5 <= self.posY <= self.cibleY + 5:
                self.CreepCible()
        elif self.parent.routes[self.currentRoute].posY == self.parent.routes[self.currentRoute].posY2:
            if self.cibleX - 5 <= self.posX <= self.cibleX + 5:
                self.CreepCible()

        self.posX = self.posX + self.vitesseX
        self.posY = self.posY + self.vitesseY


    def CreepVie(self):
        for dommage in self.dommages:
            self.vie = self.vie - dommage
            self.dommages.remove(dommage)

        ## for i in self.dommageOverTime:
        ##    for j in self.dommageOverTime:
        ##        self.vie = self.vie
        ##        dommageOver[0][1] -= 1
        ##        if(dommageOver[0][1]<=0):
        ##            self.dommageOverTime.remove(dommageOver[0])

        if (self.vie <= 0):
            self.CreepMort()


    def CreepMort(self):
        self.vivant = False







