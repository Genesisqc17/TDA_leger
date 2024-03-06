from helper import Helper as hp

class Projectile:
    def __init__(self, parent, PosX, PosY, CibleX, CibleY, niveauTour):
        self.parent = parent
        self.posX = PosX
        self.posY = PosY
        self.cibleX = CibleX
        self.cibleY = CibleY
        self.niveauTour = niveauTour
        self.vitesse = 1
        self.dommage = None
        self.rayon = 2
        self.angle = None
        self.entenduCollision = 1

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
        zone_collision = self.posX - self.rayon, self.posY - self.rayon, self.posX + self.rayon, self.posY + self.rayon
        for creep in self.parent.creepActif[]:
            zone_creep = (creep.CollisionX1,creep.CollisionY1,creep.CollisionX2,creep.CollisionY2)

            if not (zone_collision[2] < zone_creep[0] or
                    zone_collision[0] > zone_creep[2] or
                    zone_collision[3] < zone_creep[1] or
                    zone_collision[1] > zone_creep[3]):
                zone_creep.dommages.append(self.dommage)

    def mouvement(self):
        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        if dist <= self.vitesse:
            self.checkCollision()

