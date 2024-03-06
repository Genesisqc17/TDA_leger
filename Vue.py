import sys
import tkinter.font
from tkinter import *


class Vue():
    def __init__(self):
        self.canevas = None
        self.parent = parent
        self.modele = modele
        self.niv_wave_text = StringVar()
        self.chrono_text = StringVar()
        self.nb_vies = StringVar()
        self.qte_argent = StringVar()
        self.cout_upgrade_text = StringVar()
        self.force_upgrade_text = StringVar()
        self.etendu_upgrade_text = StringVar()
        self.nom_tour_text = StringVar()
        self.force_tour_text = StringVar()
        self.etendu_tour_text = StringVar()
        self.force_tour_text = StringVar()
        self.root = Tk()
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
        self.commencer_partie_bouton = Button(self.intro_frame, text="Commencer!", command=self.afficher_parent,
                                              font=self.police_bouton)
        self.regles.pack()
        self.champ_nom.pack()
        self.intro_frame.pack()

        return self.intro_frame

    def creer_parent_frame(self):
        # Frame pour l'affichage complet
        self.parent_frame = Frame(self.root)
        self.parent_frame.pack()

        # Frame pour la surface de jeu
        self.jeu_frame = Frame(self.parent_frame)
        self.jeu_frame.pack()

        # Frame pour le menu interactif
        self.menu_frame = Frame(self.jeu_frame)
        self.menu_frame.pack()

        # Frame pour la vague et le chronomètre
        self.vc_frame = Frame(self.menu_frame)
        self.niv_vague = Label(self.vc_frame, textvariable=self.niv_wave_text, font=self.police_label)
        self.timer = Label(self.vc_frame, textvariable=self.chrono_text, font=self.police_label)
        self.timer.pack()
        self.niv_vague.pack()
        self.vc_frame.pack()

        # Frame pour acheter une tour
        self.tour_frame = Frame(self.menu_frame)
        self.tour_frame.pack()

        # Boutons pour acheter tours
        self.proj_bouton = Button(self.tour_frame, text="Tour projectile", command=self.acheter_tour,
                                  font=self.police_bouton)
        self.eclair_bouton = Button(self.tour_frame, text="Tour éclair", command=self.acheter_tour,
                                    font=self.police_bouton)
        self.poison_bouton = Button(self.tour_frame, text="Tour poison", command=self.acheter_tour,
                                    font=self.police_bouton)
        self.laser_bouton = Button(self.tour_frame, text="Tour laser", command=self.acheter_tour,
                                   font=self.police_bouton)
        self.laser_bouton.pack()
        self.poison_bouton.pack()
        self.eclair_bouton.pack()
        self.proj_bouton.pack()

        # Frame pour la vie et l'argent
        self.va_frame = Frame(self.menu_frame)
        self.cmp_nb_vies = Label(self.va_frame, textvariable=self.nb_vies, font=self.police_label)
        self.cmp_argent = Label(self.va_frame, textvariable=self.qte_argent, font=self.police_label)
        self.cmp_argent.pack()
        self.cmp_nb_vies.pack()
        self.va_frame.pack()

        return self.parent_frame

    def creer_upgrade_frame(self):
        # Frame pour améliorer une tour
        self.upgrade_frame = Frame(self.menu_frame)
        self.upgrade_frame.pack()

        # Frame pour l'info d'une amélioration
        self.info_upgrade_frame = Frame(self.upgrade_frame)
        self.cout_upgrade = Label(self.info_upgrade_frame, textvariable=self.cout_upgrade_text,
                                  font=self.police_label)
        self.upgrade_force = Label(self.info_upgrade_frame, textvariable=self.force_upgrade_text,
                                   font=self.police_label)
        self.upgrade_etendu = Label(self.info_upgrade_frame, textvariable=self.etendu_upgrade_text,
                                    font=self.police_label)

        # Bouton pour améliorer une tour
        self.upgrade_bouton = Button(self.upgrade_frame, text="Améliorer", command=self.ameliorer_tour,
                                     font=self.police_bouton)

        # Frame pour l'info d'une tour
        self.info_tour = Frame(self.upgrade_frame)
        self.nom_tour = Label(self.info_tour, textvariable=self.nom_tour_text,
                              font=self.police_label)
        self.force_tour = Label(self.info_tour, textvariable=self.force_tour_text,
                                font=self.police_label)
        self.etendu_tour = Label(self.info_tour, textvariable=self.etendu_tour_text,
                                 font=self.police_label)

    def creer_game_over(self):
        return self.gameover_frame
