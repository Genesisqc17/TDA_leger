import math


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
        self.rayon = None
        self.cout = None
        self.etendu = None
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
        if self.type == "tProjectile" and self.parent.temps % self.frequenceTirs == 0:
           ## self.parent.projActif.append(Projectile)
            pass
        elif self.type == "tEclair" and self.parent.temps % self.frequenceTirs == 0:
            ## self.parent.projActif.append(Eclair)
            pass
        elif self.type == "tPoison" and self.parent.temps % self.frequenceTirs == 0:
            ## self.parent.projActif.append(Poison)
            pass

    def trouverCible(self):
        for i in self.parent.creepActif:
            if math.sqrt(math.pow((i.posX - self.posX)) + math.pow((i.posY-self.posY))) < self.etendu:
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

