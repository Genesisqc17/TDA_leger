import numpy as np
import random
from helper import Helper as hp
class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.tailleX = 320 ##32 colonnes x10 en pixel
        self.tailleY = 240
        self.box_tailleX = self.tailleX
        self.box_tailleY = self.tailleY/3
        self.vie = 20
        self.argent = 0
        self.creepActif = []
        self.creepInactif = []
        self.projActif = []
        self.tours = []
        self.routes = []
        self.positionsChateau = []
        self.isVague = False
        self.creerRoutes()
        self.creerChateau()

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


    def CreepCible(self):
        self.cibleX = random.randrange(self.parent.largeur)
        self.cibleY = random.randrange(self.parent.hauteur)
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

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

        for dommageOver in self.dommageOverTime:
            self.vie = self.vie - dommageOver[0][0]
            dommageOver[0][1] -= 1
            if(dommageOver[0][1]<=0):
                self.dommageOverTime.remove(dommageOver[0])

        if (self.vie <= 0):
            self.CreepMort()


    def CreepMort(self):
        self.vivant = False


    def finParcours(self):
        pass



