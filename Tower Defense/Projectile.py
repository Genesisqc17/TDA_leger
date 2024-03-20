import math

from helper import Helper as hp

class Projectile:
    def __init__(self, parent, posX, posY, cibleX, cibleY, niveauTour, cible):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.cible = cible
        self.collided = False
        self.niveauTour = niveauTour
        self.vitesse = None
        self.dommage = None
        self.rayon = 4
        self.angle = None
        self.etenduCollision = 20
        self.calculDommageVitesse()
        self.trouver_cible()

    def calculDommageVitesse(self):
        if self.niveauTour == 1:
            self.dommage = 3
            self.vitesse = 15
        elif self.niveauTour == 2:
            self.dommage = 4
            self.vitesse = 20
        else:
            self.dommage = 5
            self.vitesse = 40

    def trouver_cible(self):
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def checkCollision(self):
        self.collided = True
        if math.sqrt(math.pow((self.cible.posX - self.posX), 2) + math.pow((self.cible.posY-self.posY), 2)) <= self.etenduCollision:
            self.cible.dommages.append(self.dommage)


    def mouvement(self):

        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        if dist <= self.vitesse:
            self.checkCollision()

