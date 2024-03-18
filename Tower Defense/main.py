import Modele as mod
import Vue as vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.mainloop()

    def initialiser_jeu(self):
        self.boucle_jeu()

    def creer_tour(self,type, posX, posY):
        self.modele.ajouter_tour(posX,posY,type)


    def boucle_jeu(self):
        self.vue.afficher_all()
       # self.vue.update_text()
        if not self.modele.isVague:
            self.modele.debut_vague()
        if self.modele.isVague:
            self.modele.mouvement_jeu()
        #if not:
        #    self.modele.fin_vague()
        self.vue.root.after(50, self.boucle_jeu)


if (__name__ == "__main__"):
    c = Controleur()

