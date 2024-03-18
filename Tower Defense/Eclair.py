from helper import Helper as hp

class Eclair:
    def __init__(self, parent, posX, posY, cibleX, cibleY, niveauTour):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.niveauTour = niveauTour
        self.dommage = None
        self.vitesse = None
        self.rayon = 5
        self.angle = None
        self.etenduCollision = 1

    def trouver_cible(self):
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def dommage_niveau(self):
        if self.niveauTour == 1:
            self.dommage = 1
            self.vitesse = 20
            return self.dommage

        elif self.niveauTour == 2:
            self.dommage = 0.4
            return self.dommage

        elif self.niveauTour == 3:
            self.dommage = 1
            return self.dommage

    def mouvement(self):
        if self.niveauTour == 1:
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
            dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
            if dist <= self.vitesse:
                self.checkCollision()

        else: self.checkCollision()

    def checkCollision(self):
        zone_collision = (self.posX - self.rayon) - self.etenduCollision, (self.posY - self.rayon) - self.etenduCollision, (self.posX + self.rayon) + self.etenduCollision, (self.posY + self.rayon) + self.etenduCollision

        # implementer une facon pour voir si creep est a l'interieur du range de la tour
        for creep in self.parent.creepActif:
            if self.niveauTour == 1:
                creep[0].dommageOverTime.append(self.dommage_niveau())

            elif self.niveauTour == 2 or self.niveauTour == 3:
                creep[0].dommages.append(self.dommage_niveau())







