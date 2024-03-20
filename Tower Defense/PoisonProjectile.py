from helper import Helper as hp


class PoisonProjectile:
    def __init__(self, parent, posX, posY, cibleX, cibleY, niveauTourParent):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.cibleX = cibleX
        self.cibleY = cibleY
        self.niveauTourParent = niveauTourParent
        self.vitesse = None
        #self.vitesseX = None
        #self.vitesseY = None
        self.dommage = None
        self.duree = None
        #self.dommageOvertime = []
        self.rayon = 4
        self.angle = None
        self.etenduCollision = 1
        self.update_niveau()
        self.trouver_cible()

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
        #self.dommageOvertime = [self.dommage, self.duree]

    def trouver_cible(self):
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def mouvement(self):
        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        if dist <= self.vitesse:
            self.checkCollision()

    def checkCollision(self):
        zone_collision = (self.posX - self.rayon) - self.etenduCollision, (
                    self.posY - self.rayon) - self.etenduCollision, (self.posX + self.rayon) + self.etenduCollision, (
                                     self.posY + self.rayon) + self.etenduCollision
        for creep in self.parent.parent.creepActif:
            zone_creep = (creep.collisionX1, creep.collisionY1, creep.collisionX2, creep.collisionY2)

            if not (zone_collision[2] < zone_creep[0] or
                    zone_collision[0] > zone_creep[2] or
                    zone_collision[3] < zone_creep[1] or
                    zone_collision[1] > zone_creep[3]):
                creep.dommages.append(self.dommage)

        self.collided = True
