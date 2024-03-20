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
        self.upgrade_frame = None
        #self.root.geometry(f"{self.modele.tailleMaxX}x{int(self.modele.tailleMaxY)}")
        self.police_label = tkinter.font.Font(family="Terminal", size=14, weight="normal")
        self.police_bouton = tkinter.font.Font(family="Terminal", size=12, weight="normal")
        self.typeTour = None
        self.mes_frames = {"intro": self.creer_intro_frame(),
                           "parent": self.creer_parent_frame(),
                           "gameover": self.creer_game_over()}
        self.frame_active = None
        self.changer_frame("intro")

        self.id_tour_selectionne = None

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

    def afficher_upgrade(self):
        self.creer_upgrade_frame()
        self.upgrade_frame.pack(pady=10)

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
        self.canevasGame.bind("<Button-1>", self.ameliorer_tour)

        # Frame pour le menu interactif
        self.menu_frame = Frame(self.jeu_frame)
        self.menu_frame.pack()

        # Frame pour la vague et le chronomètre
        self.vc_frame = Frame(self.menu_frame, highlightbackground="black", highlightthickness=1)
        self.niv_vague = Label(self.vc_frame, textvariable=self.niv_wave_text
                               , font=self.police_label)
        self.timer = Label(self.vc_frame, textvariable=self.chrono_text
                           , font=self.police_label)
        self.timer.pack()
        self.niv_vague.pack(padx=100)
        self.vc_frame.pack(side=LEFT, padx=100, pady=10)

        # Frame pour acheter une tour
        self.tour_frame_choisi = "Achat"
        self.tour_frame = Frame(self.menu_frame)
        self.tour_frame.pack(side=LEFT, padx=150, pady=10)

        # Boutons pour acheter tours
        self.proj_bouton = Button(self.tour_frame, text="Tour projectile 3$", command=self.acheter_tour_proj
                                  , font=self.police_bouton)
        self.eclair_bouton = Button(self.tour_frame, text="Tour éclair 2$", command=self.acheter_tour_eclair
                                    , font=self.police_bouton)
        self.poison_bouton = Button(self.tour_frame, text="Tour poison 5$", command=self.acheter_tour_poison
                                    , font=self.police_bouton)
        self.poison_bouton.pack()
        self.eclair_bouton.pack()
        self.proj_bouton.pack()
        #self.changer_tour_frame("Achat")

        # Frame pour la vie et l'argent
        self.va_frame = Frame(self.menu_frame, highlightbackground="black", highlightthickness=1)
        self.cmp_nb_vies = Label(self.va_frame, textvariable=self.nb_vies
                                 , font=self.police_label)
        self.cmp_argent = Label(self.va_frame, textvariable=self.qte_argent
                                , font=self.police_label)
        self.cmp_argent.pack()
        self.cmp_nb_vies.pack()
        self.va_frame.pack(side=LEFT, padx=150, pady=10)

        return self.parent_frame

    def creer_upgrade_frame(self):
        if self.upgrade_frame is not None:
            self.upgrade_frame.pack_forget()

        self.upgrade_frame = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.force_upgrade = Label(self.upgrade_frame, textvariable=self.force_upgrade_text,
                                    font=self.police_label)
        self.etendu_upgrade = Label(self.upgrade_frame, textvariable=self.etendu_upgrade_text, font=self.police_label)
        self.nom_tour = Label(self.upgrade_frame, textvariable=self.nom_tour_text, font=self.police_label)
        self.upgrade_bouton = Button(self.upgrade_frame, textvariable=self.cout_upgrade_text, command=self.ameliorer_tour,
                                     font=self.police_bouton)
        self.upgrade_quit = Button(self.upgrade_frame, text="X", bg="red", font=self.police_bouton, command=self.quitter_upgrade)
        self.upgrade_quit.pack()
        self.nom_tour.pack(side=LEFT)
        self.force_upgrade.pack(side=LEFT, padx=50, pady=10)
        self.etendu_upgrade.pack(side=LEFT, padx=50)
        self.upgrade_bouton.pack()

    def acheter_tour_proj(self):
        self.acheter_tour()
        self.typeTour = "tProjectile"

    def acheter_tour_eclair(self):
        self.acheter_tour()
        self.typeTour = "tEclair"

    def acheter_tour_poison(self):
        self.acheter_tour()
        self.typeTour = "tPoison"

    def quitter_upgrade(self):
        self.upgrade_frame.pack_forget()

    def checkOverlap(self, event):
        overlaps = self.find_overlapping(self.canevasGame, event.x - self.modele.variableTaille, event.y - self.modele.variableTaille, event.x + self.modele.variableTaille, event.y + self.modele.variableTaille)
        overlap_route_ou_tour = False
        for item_id in overlaps:
            tags = self.canevasGame.gettags(item_id)
            if "NoOverlap" in tags:
                overlap_route_ou_tour = True
                break
        if not overlap_route_ou_tour:
            self.parent.creer_tour(self.typeTour, event.x, event.y)
            self.canevasGame.unbind("<Button-1>")
            self.canevasGame.bind("<Button-1>", self.ameliorer_tour_frame)

    def acheter_tour(self):
        self.canevasGame.unbind("<Button-1>")
        self.canevasGame.bind("<Button-1>", self.checkOverlap)

    def ameliorer_tour_frame(self, event):
        x, y = event.x, event.y
        items = self.canevasGame.find_overlapping(x, y, x, y)
        for item in items:
            tags = self.canevasGame.gettags(item)
            for tag in tags:
                if tag.startswith("tour"):
                    tour_id = int(tag[4:])
                    self.id_tour_selectionne = tour_id
                    self.update_tour_info(tour_id)
                    self.afficher_upgrade()

    def ameliorer_tour(self):
        self.parent.ameliorer_tour(self.id_tour_selectionne)
        self.update_tour_info(self.id_tour_selectionne)

    def creer_game_over(self):
        self.gameover_frame = Frame(self.root)
        self.titre_gameover = Label(self.gameover_frame, text="Game over", font=self.police_label)
        self.info_score = Label(self.gameover_frame, textvariable=self.info_score, font=self.police_label)
        self.recommencer = Button(self.gameover_frame, text="Recommencer", command=self.afficher_parent,
                                  font=self.police_bouton)

        self.titre_gameover.pack()
        self.info_score.pack()
        self.recommencer.pack()

        return self.gameover_frame

    def afficher_all(self):
        self.canevasGame.delete("all")

        for i in self.modele.routes:
            self.canevasGame.create_line(i.posX, i.posY,
                                         i.posX2, i.posY2,
                                         width=self.modele.variableTaille + 6,
                                         fill="khaki1",capstyle=ROUND, joinstyle=ROUND, tags=("route", "NoOverlap"))

        for i in self.modele.creepActif:
            self.canevasGame.create_oval(i.posX - i.rayon,i.posY - i.rayon,
                                         i.posX + i.rayon,i.posY + i.rayon,
                                         fill="PaleGreen3", tags="creep")

        for i in self.modele.tours:
            if i.type == "tProjectile":
                self.canevasGame.create_oval(i.posX - i.rayon,i.posY - i.rayon,
                                             i.posX + i.rayon,i.posY + i.rayon,
                                             fill=i.couleur, tags=(f"tour{str(i.id)}", "NoOverlap", "Projectile"))
            elif i.type == "tEclair":
                self.canevasGame.create_oval(i.posX - i.rayon,i.posY - i.rayon,
                                             i.posX + i.rayon,i.posY + i.rayon,
                                             fill=i.couleur, tags=(f"tour{str(i.id)}", "NoOverlap", "Eclair"))
            if i.type == "tPoison":
                self.canevasGame.create_oval(i.posX - i.rayon,i.posY - i.rayon,
                                             i.posX + i.rayon,i.posY + i.rayon,
                                             fill=i.couleur, tags=(f"tour{str(i.id)}", "NoOverlap", "Poison"))

        for i in self.modele.projActif:
            if i.parent.type == "tProjectile":
                self.canevasGame.create_oval(i.posX - i.rayon, i.posY - i.rayon,
                                             i.posX + i.rayon, i.posY + i.rayon,
                                             fill="gold", tags="proj")
            if i.parent.type == "tEclair":
                if i.cibleX and i.cibleY is not None:
                    self.canevasGame.create_line(i.parent.posX, i.parent.posY, i.cibleX, i.cibleY,
                                             fill="deep sky blue", tags="proj", width=5)
            if i.parent.type == "tPoison":
                self.canevasGame.create_oval(i.posX - i.rayon, i.posY - i.rayon,
                                             i.posX + i.rayon, i.posY + i.rayon,
                                             fill="gold", tags="proj")

        for i in self.modele.positionsChateau:
            self.canevasGame.create_rectangle(i.posX, i.posY,
                                             i.posX2, i.posY2,
                                             width=self.modele.variableTaille + 6,
                                             fill="royal blue", tags=("Chateau", "NoOverlap"))



    def find_overlapping(self,canvas, x1, y1, x2, y2):
        overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
        return overlapping_items

    def update_text(self):
        self.niv_wave_text.set("Vague: " + str(self.modele.niveauVague))
        self.chrono_text.set("Chrono: " + str(round(self.modele.timeTotal, 2)))
        self.nb_vies.set("Vie: " + str(self.modele.vie))
        self.qte_argent.set("Argent: " + str(self.modele.argent) + "$")

    def update_tour_info(self, id_tour):
        nom_tour = ""
        for i in self.modele.tours:
            if i.type == "tProjectile":
                nom_tour = "Tour de projectiles"
                self.cout_upgrade_text.set("Coût: " + str(self.modele.tours[id_tour].cout * 2))
            elif i.type == "tEclair":
                nom_tour = "Tour d'éclairs"
                self.cout_upgrade_text.set("Coût: " + str(self.modele.tours[id_tour].cout * 1.5))
            elif i.type == "tPoison":
                nom_tour = "Tour de poison"
                self.cout_upgrade_text.set("Coût: " + str(self.modele.tours[id_tour].cout * 1.75))

            self.force_upgrade_text.set("Force: " + str(self.modele.tours[id_tour].niveauForce + 1))
            self.etendu_upgrade_text.set("Étendu: " + str(self.modele.tours[id_tour].etendu + 5))
            self.nom_tour_text.set("Tour: " + nom_tour)
            self.force_tour_text.set("Force: " + str(self.modele.tours[id_tour].niveauForce))
            self.etendu_tour_text.set("Étendu: " + str(self.modele.tours[id_tour].etendu))



