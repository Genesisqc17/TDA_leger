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
        self.nextIdTour = 0
        self.isVague = False
        self.creerRoutes()
        self.creerChateau()

    def creerRoutes(self):
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
