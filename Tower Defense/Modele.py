from Route import Route
from creep import Creep

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.variableTaille = 40
        self.nbColonneWindow = 32
        self.nbLignesWindow = 24
        self.nbColonnesJeu = self.nbColonneWindow
        self.nbLignesJeu = self.nbLignesWindow/3 * 2
        self.tailleX = self.nbColonnesJeu * self.variableTaille
        self.tailleY = self.nbLignesJeu * self.variableTaille
        self.box_tailleX = self.tailleX
        self.box_tailleY = self.tailleY/3
        self.vie = 20
        self.argent = 0
        self.niveauVague = 0
        self.creepActif = []
        self.creepInactif = []
        self.projActif = []
        self.tours = []
        self.routes = []
        self.positionsChateau = []
        self.nextIdTour = 0
        self.isVague = False
        self.creerRoutes()
        self.creerChateau()
        self.timeDebut = 0
        self.timeFin = 0
        self.timeTotal = 0

    def ajouter_tour(self,posX, posY, type):
        pass


    def debut_vague(self):
        self.niveauVague += 1
        self.initCreepInactif()
        for i in self.creepInactif:
            self.creepActif.append(i)

        self.creepInactif.clear()
        for i in self.creepActif:
            i.CreepCible()
        self.isVague = True
        self.timeFin = time.time()
        self.timeFin = time.time()

    def mouvement_jeu(self):
        for i in self.creepActif:
            i.Mouvement()
        self.timeFin = time.time()
        self.timeTotal = self.timeFin - self.timeDebut

    def fin_vague(self):
        self.projActif.clear()
        self.argent = self.argent + self.niveauVague * 50
        self.isVague = False

    def initialiser_jeu(self):
        pass

    def initCreepInactif(self):
        for x in range(20):
            self.creepInactif.append(Creep(self, 5 * self.variableTaille, 0 * self.variableTaille))


    def creerRoutes(self):
        r1 = Route(self, 5, 0, 5, 15)
        r2 = Route(self, 5, 15, 11, 15)
        r3 = Route(self, 11, 15, 11, 4)
        r4 = Route(self, 11, 4, 28, 4)
        r5 = Route(self, 28, 4, 28, 9)
        r6 = Route(self, 28, 9, 19, 9)
        r7 = Route(self, 19, 9, 19, 15)
        r8 = Route(self, 19, 15, 28, 15)

        self.routes.append(r1)
        self.routes.append(r2)
        self.routes.append(r3)
        self.routes.append(r4)
        self.routes.append(r5)
        self.routes.append(r6)
        self.routes.append(r7)
        self.routes.append(r8)

        pass

    def creerChateau(self):
        ## posX1
        ## posY1
        ## posX2
        ## posY2
        ## posX3
        ## posY3
        ## posX4
        ## posY4
        ## posX5
        ## posY5
        pass
