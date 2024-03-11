import sys
import tkinter.font
from tkinter import *


class Vue():
    def __init__(self, parent, modele):
        self.canevas = None
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.niv_wave_text = StringVar()
        self.niv_wave_text.set("Vague:")
        self.chrono_text = StringVar()
        self.chrono_text.set("Temps: ")
        self.nb_vies = StringVar()
        self.nb_vies.set("Vie: ")
        self.qte_argent = StringVar()
        self.qte_argent.set("Argent: ")
        self.cout_upgrade_text = StringVar()
        self.cout_upgrade_text.set("Coût: ")
        self.force_upgrade_text = StringVar()
        self.force_upgrade_text.set("Force: ")
        self.etendu_upgrade_text = StringVar()
        self.etendu_upgrade_text.set("Étendu: ")
        self.nom_tour_text = StringVar()
        self.nom_tour_text.set("Tour: ")
        self.force_tour_text = StringVar()
        self.force_tour_text.set("Force: ")
        self.etendu_tour_text = StringVar()
        self.etendu_tour_text.set("Étendu: ")
        self.force_tour_text = StringVar()
        self.force_tour_text.set("Force: ")
        self.info_score = StringVar()
        self.info_score.set("Score: ")
        self.root.title("Super Tower Defence 64")
        self.police_label = tkinter.font.Font(family="Terminal", size=14, weight="normal")
        self.police_bouton = tkinter.font.Font(family="Terminal", size=12, weight="normal")

        self.mes_frames = {"intro": self.creer_intro_frame(),
                           "parent": self.creer_parent_frame(),
                           "gameover": self.creer_game_over()}
        self.frame_active = None
        self.changer_frame("intro")

    def changer_frame(self, cle):
        if self.frame_active:
            self.frame_active.pack_forget()
        self.frame_active = self.mes_frames[cle]
        self.frame_active.pack()

    def commencer_partie(self):
        self.afficher_parent()
        self.parent.initialiser_jeu()

    def afficher_intro(self):
        self.changer_frame("intro")

    def afficher_parent(self):
        self.changer_frame("parent")

    def afficher_gameover(self):
        self.changer_frame("gameover")

    def creer_intro_frame(self):
        # Frame pour la page d'introduction
        self.intro_frame = Frame(self.root)
        self.regles = Label(self.intro_frame,
                            text="Défendez le château des Creeps envahisseurs en placant vos tours stratégiquement!",
                            font=self.police_label)
        self.login = Label(self.intro_frame, text="Entrez votre nom:", font=self.police_label)
        self.champ_nom = Entry(self.intro_frame)
        self.commencer_partie_bouton = Button(self.intro_frame, text="Commencer!", command=self.commencer_partie,
                                              font=self.police_bouton)
        self.regles.pack()
        self.login.pack()
        self.champ_nom.pack()
        self.commencer_partie_bouton.pack()

        return self.intro_frame

    def creer_parent_frame(self):
        # Frame pour l'affichage complet
        self.parent_frame = Frame(self.root)

        # Frame pour la surface de jeu
        self.jeu_frame = Frame(self.parent_frame)
        self.jeu_frame.pack()
        self.canevasGame = Canvas(self.jeu_frame, width=self.modele.tailleX, height=self.modele.tailleY,
                                  bg="green3")
        self.canevasGame.place(x=0, y=0)
        self.canevasGame.pack()

        # Frame pour le menu interactif
        self.menu_frame = Frame(self.jeu_frame)
        self.menu_frame.pack()

        # Frame pour la vague et le chronomètre
        self.vc_frame = Frame(self.menu_frame)
        self.niv_vague = Label(self.vc_frame, textvariable=self.niv_wave_text
                               , font=self.police_label)
        self.timer = Label(self.vc_frame, textvariable=self.chrono_text
                           , font=self.police_label)
        self.timer.pack()
        self.niv_vague.pack()
        self.vc_frame.pack(side=LEFT)

        # Frame pour acheter une tour
        self.tour_frame = Frame(self.menu_frame)
        self.tour_frame.pack(side=LEFT)

        # Boutons pour acheter tours
        self.proj_bouton = Button(self.tour_frame, text="Tour projectile", command=self.acheter_tour
                                  , font=self.police_bouton)
        self.eclair_bouton = Button(self.tour_frame, text="Tour éclair", command=self.acheter_tour
                                    , font=self.police_bouton)
        self.poison_bouton = Button(self.tour_frame, text="Tour poison", command=self.acheter_tour
                                    , font=self.police_bouton)
        self.poison_bouton.pack(side=LEFT)
        self.eclair_bouton.pack(side=LEFT)
        self.proj_bouton.pack(side=LEFT)

        # Frame pour la vie et l'argent
        self.va_frame = Frame(self.menu_frame)
        self.cmp_nb_vies = Label(self.va_frame, textvariable=self.nb_vies
                                 , font=self.police_label)
        self.cmp_argent = Label(self.va_frame, textvariable=self.qte_argent
                                , font=self.police_label)
        self.cmp_argent.pack()
        self.cmp_nb_vies.pack()
        self.va_frame.pack(side=LEFT)

        return self.parent_frame

    def creer_upgrade_frame(self):
        # Frame pour améliorer une tour
        self.upgrade_frame = Frame(self.menu_frame)

        # Frame pour l'info d'une amélioration
        self.info_upgrade_frame = Frame(self.upgrade_frame)
        self.cout_upgrade = Label(self.info_upgrade_frame, textvariable=self.cout_upgrade_text
                                  , font=self.police_label)
        self.upgrade_force = Label(self.info_upgrade_frame, textvariable=self.force_upgrade_text
                                   , font=self.police_label)
        self.upgrade_etendu = Label(self.info_upgrade_frame, textvariable=self.etendu_upgrade_text
                                    , font=self.police_label)

        # Bouton pour améliorer une tour
        self.upgrade_bouton = Button(self.upgrade_frame, text="Améliorer", command=self.ameliorer_tour
                                     , font=self.police_bouton)

        # Frame pour l'info d'une tour
        self.info_tour = Frame(self.upgrade_frame)
        self.nom_tour = Label(self.info_tour, textvariable=self.nom_tour_text
                              , font=self.police_label)
        self.force_tour = Label(self.info_tour, textvariable=self.force_tour_text
                                , font=self.police_label)
        self.etendu_tour = Label(self.info_tour, textvariable=self.etendu_tour_text
                                 , font=self.police_label)

        return self.upgrade_frame

    def acheter_tour(self):
        self.parent.acheter_tour()

    def ameliorer_tour(self):
        self.parent.ameliorer_tour()

    def creer_game_over(self):
        self.gameover_frame = Frame(self.root)
        self.titre_gameover = Label(self.gameover_frame, text="Game over", font=self.police_label)
        self.info_score = Label(self.gameover_frame, textvariable=self.info_score, font=self.police_label)
        self.recommencer = Button(self.gameover_frame, text="Recommencer", command=self.afficher_parent,
                                  font=self.police_bouton)

        return self.gameover_frame

    def afficher_all(self):
        self.canevasGame.delete("all")

        for i in self.modele.routes:
            self.canevasGame.create_line(i.posX, i.posY, i.posX2, i.posY2, width=self.modele.variableTaille + 6,
                                         fill="khaki1",capstyle=ROUND, joinstyle=ROUND, tags="route")

        for i in self.modele.creepActif:
            self.canevasGame.create_oval(i.posX,i.posY,i.posX + i.rayon,i.posY + i.rayon, fill="PaleGreen3", tags="creep")

'''
    def update_text(self):
        self.niv_wave_text.set("Vague: " + self.modele.niv_wave)
        self.chrono_text.set("Chrono: " + self.modele.chrono)
        self.nb_vies.set("Vie: " + self.modele.vie)
        self.qte_argent.set("Argent: " + self.modele.argent)
        self.cout_upgrade_text.set("Coût: " + self.modele.cost_tour)
        self.force_upgrade_text.set("Force: " + self.modele.force_upgrade)
        self.etendu_upgrade_text.set("Étendu: " + self.modele.etendu_upgrade)
        self.nom_tour_text.set("Tour: " + self.modele.type_tour)
        self.force_tour_text.set("Force: " + self.modele.force_tour)
        self.etendu_tour_text.set("Étendu: " + self.modele.etendu_tour)
        self.force_tour_text.set("Force: " + self.modele.force_tour)
        '''