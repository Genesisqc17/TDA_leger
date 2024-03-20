import math
from Projectile import Projectile
from Eclair import Eclair
from PoisonProjectile import PoisonProjectile as Poison
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
        self.nextShotTime = self.parent.timeTotal
        self.initDifTour()
        self.tick = 0
        self.cible = None

    def initDifTour(self):
        if self.type == "tProjectile":
            self.cout = 3
            self.couleur = "RED"

        elif self.type == "tEclair":
            self.cout = 2
            self.couleur = "BLUE"

        elif self.type == "tPoison":
            self.cout = 5
            self.nextShotTime = 2
            self.couleur = "GREEN"

    def tirer(self):
        self.trouverCible()

        if self.type == "tProjectile":
            if self.tick >= self.nextShotTime:
                self.parent.projActif.append(Projectile(self,self.posX,self.posY,self.cibleX,self.cibleY,self.niveauForce, self.cible))
                self.nextShotTime = self.tick + 35

        elif self.type == "tEclair":
            if self.tick >= self.nextShotTime:
                self.parent.projActif.append(Eclair(self,self.posX,self.posY,self.niveauForce))


        self.tick += 1
        self.cibleX = None
        self.cibleY = None
       ## elif self.type == "tPoison":
         ##       if self.parent.timeTotal % self.nextShotTime == 0:
           ##         pass
            ##pass


    def trouverCible(self):
        for i in reversed(self.parent.creepActif):
            if math.sqrt(math.pow((i.posX - self.posX), 2) + math.pow((i.posY-self.posY), 2)) < self.etendu:
                self.cibleX = i.posX
                self.cibleY = i.posY
                self.cible = i



    def ameliorer(self):
        if self.parent.argent > self.cout and self.niveauForce < 3:

            self.niveauForce = self.niveauForce + 1

            if self.type == "tProjectile":
                self.cout = self.cout * 2
                self.etendu += 25

            elif self.type == "tEclair":
                self.cout = self.cout * 1.5
                self.etendu += 20

            elif self.type == "tPoison":
                self.cout = self.cout * 1.75
                self.etendu += 10

    def idTourSelect(self):
        return self.id

