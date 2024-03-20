import math
from Projectile import Projectile
from Eclair import Eclair
class Tour():
    def __init__(self, parent, posX, posY, type, id):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.type = type
        self.id = id
        self.cibleX = None
        self.cibleY = None
        self.niveauForce = 1
        self.rayon = self.parent.variableTaille / 2
        self.cout = None
        self.etendu = self.parent.variableTaille * 3
        self.couleur = None
        self.frequenceTirs = None
        self.initDifTour()

    def initDifTour(self):
        if self.type == "tProjectile":
            self.cout = 5
            self.frequenceTirs = 3
            self.couleur = "RED"

        elif self.type == "tEclair":
            self.cout = 2
            self.frequenceTirs = 1
            self.couleur = "BLUE"

        elif self.type == "tPoison":
            self.cout = 3
            self.frequenceTirs = 2
            self.couleur = "GREEN"

    def tirer(self):
        self.trouverCible()
        print(self.parent.timeTotal)
        if self.type == "tProjectile" and int(self.parent.timeTotal) % self.frequenceTirs == 0:
           self.parent.projActif.append(Projectile(self,self.posX,self.posY,self.cibleX,self.cibleY,self.niveauForce))
           print("tirer proj")
        elif self.type == "tEclair" and self.parent.timeTotal % self.frequenceTirs == 0:
           self.parent.projActif.append(Eclair(self,self.posX,self.posY,self.niveauForce))
           print("tirer eclair")
        elif self.type == "tPoison" and self.parent.timeTotal % self.frequenceTirs == 0:
            ## self.parent.projActif.append(Poison)
            pass

    def trouverCible(self):
        for i in self.parent.creepActif:
            if math.sqrt(math.pow((i.posX - self.posX), 2) + math.pow((i.posY-self.posY), 2)) < self.etendu:
                self.cibleX = i.posX
                self.cibleY = i.posY



    def ameliorer(self, prix):
        if self.parent.argent > self.cout and self.niveauForce < 3:

            self.niveauForce = self.niveauForce + 1

            if self.type == "tProjectile":
                self.cout = self.cout * 2

            elif self.type == "tEclair":
                self.cout = self.cout * 1.5

            elif self.type == "tPoison":
                self.cout = self.cout * 1.75

    def idTourSelect(self):
        return self.id

