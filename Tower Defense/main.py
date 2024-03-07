import Modele as mod
import Vue as vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.mainloop()

    def initialiser_jeu(self):
        self.modele.initialiser_jeu()
        self.vue.afficher_interface()

    def debut_jeu(self):
        self.modele.debut_vague()

    def boucle_jeu(self):
        self.vue.afficher_jeu()
        # if :
        #    self.modele.fin_vague()
        self.vue.root.after(50, self.boucle_jeu)


if (__name__ == "__main__"):
    c = Controleur()

