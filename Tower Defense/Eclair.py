from helper import Helper as hp

class Eclair:
    def __init__(self, parent, posX, posY, niveauTour):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = None
        self.cibleY =None
        self.niveauTour = niveauTour
        self.dommage = None
        self.rayon = 5
        self.etendu = parent.etendu
        self.cible = None
        self.collided = False
        self.dommage_niveau()
        self.trouver_cible()

    def dommage_niveau(self):
        if self.niveauTour == 1:
            self.dommage = 0.008

        elif self.niveauTour == 2:
            self.dommage = 0.4

        elif self.niveauTour == 3:
            self.dommage = 1

    def mouvement(self):
        if not self.cible or self.cible.vie <= 0:
            self.trouver_cible()
        if self.cible:
            self.posX = self.cible.posX
            self.cibleX = self.posX
            self.posY = self.cible.posY
            self.cibleY = self.posY
            distance = hp.calcDistance(self.posX, self.posY, self.cible.posX, self.cible.posY)
            if distance <= self.etendu:
                self.cible.vie -= self.dommage
                if self.cible.vie <= 0:
                    self.collided = True

    def trouver_cible(self):
        for creep in self.parent.parent.creepActif:
            distance = hp.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
            if distance <= self.etendu:
                self.cible = creep
                break






















