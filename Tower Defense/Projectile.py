from helper import Helper as hp

class Projectile:
    def __init__(self, parent, posX, posY, cibleX, cibleY, niveauTour):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.niveauTour = niveauTour
        self.vitesse = 1
        self.dommage = None
        self.rayon = 4
        self.angle = None
        self.etenduCollision = 1
        self.calculDommageVitesse()
        self.trouver_cible()

    def calculDommageVitesse(self):
        if self.niveauTour == 1:
            self.dommage = 3
            self.vitesse = 2
        elif self.niveauTour == 2:
            self.dommage = 1
            self.vitesse = 3
        else:
            self.dommage = 5
            self.vitesse = 1

    def trouver_cible(self):
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def checkCollision(self):
        zone_collision = (self.posX - self.rayon) - self.etenduCollision, (self.posY - self.rayon) - self.etenduCollision, (self.posX + self.rayon) + self.etenduCollision, (self.posY + self.rayon) + self.etenduCollision
        for creep in self.parent.parent.creepActif:
            zone_creep = (creep.collisionX1,creep.collisionY1,creep.collisionX2,creep.collisionY2)

            if not (zone_collision[2] < zone_creep[0] or
                    zone_collision[0] > zone_creep[2] or
                    zone_collision[3] < zone_creep[1] or
                    zone_collision[1] > zone_creep[3]):
                creep.dommages.append(self.dommage)
                print("collide")


    def mouvement(self):

        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        if dist <= self.vitesse:
            self.checkCollision()

