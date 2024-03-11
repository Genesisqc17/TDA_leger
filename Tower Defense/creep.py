import random

class Creep():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.vivant = True
        self.vie = 10  * self.parent.niveau
        self.cibleX = None
        self.cibleY = None
        self.angle = None
        self.vitesse = 3 * self.parent.niveau
        self.rayon = 3
        self.collisionX1 = posX - self.rayon
        self.collisionY1 = posY - self.rayon
        self.collisionX2 = posX + self.rayon
        self.collisionY2 = posX + self.rayon
        self.couleur = "red"
        self.valeurArgent = 10 * self.parent.niveau
        self.dommageOverTime = []
        self.dommages = []
        self.currentRoute = None

    def CreepCible(self):
        if(self.currentRoute == None):
            self.currentRoute = 0
        else: self.currentRoute += 1

        if(self.currentRoute < self.parent.routes.size()):
            self.cibleX = random.randrange(self.parent.routes[self.currentRoute].PosX2, self.parent.routes[self.currentRoute].PosXZoneCible)
            self.cibleY = random.randrange(self.parent.routes[self.currentRoute].PosY2, self.parent.routes[self.currentRoute].PosYZoneCible)
            self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

        else:
            self.parent.vie -= 1
            self.vie = 0



    def Mouvement(self):
        if self.cibleX:
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse,
                                                     self.posX, self.posY)

            dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)

            if dist <= self.vitesse:
                self.CreepCible()

        else:
            self.CreepCible()

    def CreepVie(self):
        for dommage in self.dommages:
            self.vie = self.vie - dommage
            self.dommages.remove(dommage)

        for i in self.dommageOverTime:
            for j in self.dommageOverTime:
                self.vie = self.vie
                dommageOver[0][1] -= 1
                if(dommageOver[0][1]<=0):
                    self.dommageOverTime.remove(dommageOver[0])

        if (self.vie <= 0):
            self.CreepMort()


    def CreepMort(self):
        self.vivant = False







