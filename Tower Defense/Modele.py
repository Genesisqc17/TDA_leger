from Route import Route
from creep import Creep
from Tour import Tour
from Chateau import Chateau
import time

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
        self.tailleMaxX = self.tailleX
        self.tailleMaxY = self.tailleY + self.box_tailleY
        self.vie = 20
        self.argent = 10
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
        self.intervalSpawnCreep = 1

    def gameOver(self):
        self.vie = 20
        self.argent = 10
        self.niveauVague = 0
        self.creepActif = []
        self.creepInactif = []
        self.projActif = []
        self.tours = []
        self.nextIdTour = 0


    def ajouter_tour(self, posX, posY, type):
        nouvelleTour = Tour(self,posX,posY,type,self.nextIdTour)
        if(self.argent >= nouvelleTour.cout):
            self.argent -= nouvelleTour.cout
            self.tours.append(nouvelleTour)
            #self.tours.append(Tour(self, posX, posY, type, self.nextIdTour))
            self.nextIdTour += 1


    def ameliorer_tour(self,id_tour):
        for i in self.tours:
            if i.id == id_tour:
                if self.argent >= i.cout:
                    self.argent -= i.cout
                    i.ameliorer()


    def debut_vague(self):
        self.niveauVague += 1
        self.intervalSpawnCreep = 1
        self.initCreepInactif()
        for i in self.creepInactif:
            i.CreepCible()

        self.isVague = True
        self.timeDebut = time.time()
        self.timeFin = time.time()

    def mouvement_jeu(self):
        self.timeFin = time.time()
        self.timeTotal = self.timeFin - self.timeDebut
        elapsed_seconds = int (self.timeTotal)

        if len(self.creepInactif) == 0:
            if len(self.creepActif) == 0:
                self.fin_vague()

        if self.timeTotal >= self.intervalSpawnCreep and len(self.creepInactif) != 0:
            self.creepActif.append(self.creepInactif[-1])
            self.creepInactif = self.creepInactif[:-1]
            self.intervalSpawnCreep += 5


        ## Trouver cible de tour
        if len(self.creepActif) != 0:
            for i in self.tours:
                i.trouverCible()
            ## tirer
            for i in self.tours:
                if i.cibleX != None:
                    i.tirer()

            ## Trouve les creeps mort
            creepsMort = []
            for i in self.creepActif:
                if i.vivant == False:
                    creepsMort.append(i)
            ## Enleve les creeps mort de creepActif
            for i in creepsMort:
                self.creepActif.remove(i)
                self.argent += 2 * self.niveauVague


        ## Trouve les projectiles qui ont collided
        if len(self.projActif) != 0:
            collidedProjectiles = []
            for i in self.projActif:
                if i.parent.type == "tProjectile":
                    if i.collided == True:
                        collidedProjectiles.append(i)

            for i in collidedProjectiles:
                self.projActif.remove(i)

        ##Mouvement de tout les objets
        for i in self.creepActif:
            i.Mouvement()
        if len(self.projActif) != 0:
            for i in self.projActif:
                i.mouvement()
            
        ##verif valeur dmg
        if len(self.creepActif) != 0:
            for i in self.creepActif:
                i.CreepVie()

    def fin_vague(self):
        self.projActif.clear()
        self.argent = self.argent + self.niveauVague * 50
        self.isVague = False

        ##verif valeur dmg
        for i in self.creepActif:
            i.CreepVie()

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
        pos1 = Chateau(self, 29, 15, 29, 14)
        pos2 = Chateau(self, 30, 15, 30, 14)
        pos3 = Chateau(self, 28, 13, 31, 12)

        self.positionsChateau.append(pos1)
        self.positionsChateau.append(pos2)
        self.positionsChateau.append(pos3)