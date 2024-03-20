class Chateau:
    def __init__(self, parent, posX, posY, posX2, posY2, couleur):
        self.parent = parent
        self.posX = posX * self.parent.variableTaille
        self.posY = posY * self.parent.variableTaille
        self.posX2 = posX2 * self.parent.variableTaille
        self.posY2 = posY2 * self.parent.variableTaille
        self.couleur = couleur