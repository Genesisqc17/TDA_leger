

class PoisonProjectile:
    def __init__(self, parent, posX, posY, cibleX, cibleY, niveauTourParent):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.niveauTourParent = niveauTourParent
        self.vitesse = None
        self.vitesseX = None
        self.vitesseY = None
        self.dommage = None
        self.duree = None
        self.dommageOvertime = []
        self.rayon = None
        self.angle = None
        self.entenduCollision = None
        self.update_niveau()

    def update_niveau(self):
        if self.niveauTourParent == 1:
            self.dommage = 1
            self.duree = 3
        elif self.niveauTourParent == 2:
            self.dommage = 1.5
            self.duree = 3.5
        elif self.niveauTourParent == 3:
            self.dommage = 2
            self.duree = 4
        self.dommageOvertime = [self.dommage, self.duree]


    def mouvement(self):
        pass

    def collision(self):
        pass
