from helper import Helper as hp

class Eclair:
    def __init__(self, parent, posX, posY, niveauTour):
        self.parent = parent
        self.posX = posX
        self.posY = posY
        self.niveauTour = niveauTour
        self.dommage = None
        self.rayon = 5
        self.etendu = parent.etendu
        self.cible = None
        self.dommage_niveau()
        self.trouver_cible()
        # self.cibleX = cibleX
        # self.cibleY = cibleY
        # self.vitesse = None
        # self.angle = None

    def dommage_niveau(self):
        if self.niveauTour == 1:
            self.dommage = 1
            # self.vitesse = 20


        elif self.niveauTour == 2:
            self.dommage = 0.4


        elif self.niveauTour == 3:
            self.dommage = 1

    def mouvement(self):
        if not self.cible or self.cible.vie <= 0:
            self.trouverCible()

        if self.cible:
            self.posX = self.cible.posX
            self.posY = self.cible.posY
            distance = hp.calcDistance(self.posX, self.posY, self.cible.posX, self.cible.posY)
            if distance <= self.etendu:
                self.cible.vie -= self.dommage

    def trouver_cible(self):
        for creep in self.parent.creepActif:
            distance = hp.calcDistance(self.posX, self.posY, creep.posX, creep.posY)
            if distance <= self.etendu:
                self.cible = creep
                break














    # def trouver_cible(self):
    #     self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)


    # def mouvement(self):
    #     if self.niveauTour == 1:
    #         self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
    #         dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
    #         if dist <= self.vitesse:
    #             self.checkCollision()
    #
    #     else: self.checkCollision()
    #
    # def checkCollision(self):
    #     zone_collision = (self.posX - self.rayon) - self.etenduCollision, (self.posY - self.rayon) - self.etenduCollision, (self.posX + self.rayon) + self.etenduCollision, (self.posY + self.rayon) + self.etenduCollision
    #
    #     # implementer une facon pour voir si creep est a l'interieur du range de la tour
    #     for creep in self.parent.creepActif:
    #         if self.niveauTour == 1:
    #             creep[0].dommageOverTime.append(self.dommage_niveau()) #faire en dommage normal vu que manque de temps pour damageOverTime
    #
    #         elif self.niveauTour == 2 or self.niveauTour == 3:
    #             creep[0].dommages.append(self.dommage_niveau())







