import tkinter as tk
import MAPGENERATOR
from MAPGENERATOR import *
from tkinter import *

from Timer import Timer
class Vue:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Tk()
        self.simroot = None
        self.seed = None
        self.startButton = None
        self.canva_frame_general = None
        self.squares = []
        self.res = 0
        self.respawnTres = False

        # ZOOM DE LA MAP
        self.submap = None
        self.bool = False
        self.currSectionView = None
        self.canva_frame_zoom = None
        self.carre = 10
        self.reasignImageID = False

        def on_write(var): #sert de verification au entrés # pour l'intant j'ai mis que aucun ne peut etre egal a zero mais a voir
            try:
                if var.get() < 1:
                    var.set(1)
                elif self.mois.get() > 12:
                    self.mois.set(12)
                elif self.jour.get() > Timer.nombreDeJoursDumois(self.annee.get(),self.mois.get()):
                    self.jour.set(Timer.nombreDeJoursDumois(self.annee.get(),self.mois.get()))
                    
            except TclError:
                    pass
        
#       ANIMAUX
        self.Loup = IntVar(value=5)
        self.Loup.trace_add("write", lambda *args: on_write(self.Loup))
        
        self.Lievre = IntVar(value=5)
        self.Lievre.trace_add("write", lambda *args: on_write(self.Lievre))
        
        self.Sapin = IntVar(value=5)
        self.Sapin.trace_add("write", lambda *args: on_write(self.Sapin))
        
        self.Cerf = IntVar(value=5)
        self.Cerf.trace_add("write", lambda *args: on_write(self.Cerf))
        
        self.Lynx = IntVar(value=5)
        self.Lynx.trace_add("write", lambda *args: on_write(self.Lynx))
        
        self.Renard = IntVar(value=5)
        self.Renard.trace_add("write", lambda *args: on_write(self.Renard))
        
        self.Orignial = IntVar(value=5)
        self.Orignial.trace_add("write", lambda *args: on_write(self.Orignial))
        
        self.Ours = IntVar(value=5)
        self.Ours.trace_add("write", lambda *args: on_write(self.Ours))
        
        self.Castor = IntVar(value=5)
        self.Castor.trace_add("write", lambda *args: on_write(self.Castor))
        
        self.Ecureille = IntVar(value=5)
        self.Ecureille.trace_add("write", lambda *args: on_write(self.Ecureille))
        
        self.Raton = IntVar(value=5)
        self.Raton.trace_add("write", lambda *args: on_write(self.Raton))

        #VEGETAUX
        self.biomes_frame = None
        
        self.Sapin = IntVar(value=10)
        self.Sapin.trace_add("write", lambda *args: on_write(self.Sapin))
        
        self.Bouleau = IntVar(value=15)
        self.Bouleau.trace_add("write", lambda *args: on_write(self.Bouleau))
        
        self.Pissenlit = IntVar(value=150)
        self.Pissenlit.trace_add("write", lambda *args: on_write(self.Pissenlit))
        
        self.Bleuet = IntVar(value=25)
        self.Bleuet.trace_add("write", lambda *args: on_write(self.Bleuet))
        
        self.Pomier = IntVar(value=15)
        self.Pomier.trace_add("write", lambda *args: on_write(self.Pomier))
        
        self.Erable = IntVar(value=15)
        self.Erable.trace_add("write", lambda *args: on_write(self.Erable))

        #TEMPS(ENVIRONNEMENT)
        self.jour = IntVar(value=1)
        self.jour.trace_add("write", lambda *args: on_write(self.jour))
        
        
        self.mois = IntVar(value=1)
        self.mois.trace_add("write", lambda *args: on_write(self.mois))
        
        self.annee = IntVar(value=2015)
        self.annee.trace_add("write", lambda *args: on_write(self.annee))

        #METEO
        self.saison_frame = None
        self.dates_frame = None
        self.heure_frame = None
        self.temp_frame = None
        self.humidite_frame = None
        self.solei_max_frame = None
        self.solei_actuel_frame = None
        self.leve_solei_frame = None
        self.heure_coucher_solei = None
        self.apogee_solei = None
        self.solei_info = None

        self.saisonBase = None


    def accueil(self):
        self.root.title("Accueil")
        self.root.geometry("1500x500")
        self.root.resizable(False, False)
        self.root.config(background="#292929")
        self.Frame_Preview_show_map = None

        Frame_global = Frame(self.root, bg="#292929")
        Frame_global.pack(fill=BOTH, expand=True, side=LEFT)

        # Div du titre
        frame_title = Frame(Frame_global, bg="#292929")
        frame_title.pack(pady=10, padx=30, fill=BOTH)
        label_title = Label(frame_title, text="Simulation Environnement Naturel Du Quebec", font=("Arial", 25), bg="#292929", fg="gray")
        label_title.pack()

        # Div des Configurations
        frame_buttons = Frame(Frame_global, bg="#292929",  height=50)
        frame_buttons.pack(padx=30, side=LEFT, anchor=N)

        # Confirmer les changement et les appliquées
        def valider():
            label3.config(text=clicked.get())
            label2.config(text=clicked2.get())

            self.res = (mapSize[clicked.get()])
            water = waterPerc[clicked2.get()]

            self.seed = MAPGENERATOR.Seed(water)  #SEED GENERATES HERE!!!!!!!!
            
            start_preview['state'] = NORMAL
            self.startButton['state'] = DISABLED
            
            self.parent.model.env.baseValider(self.annee.get(), self.mois.get(), self.jour.get())
            
        
        # n'autorise que les chiffres dans les entry auquel il est assigné
        def validate_digit(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
            """Valide si l'entrée est un chiffre."""
            if action == '1':  # action 1 est pour insertion
                if text.isdigit():
                    return True
                else:
                    return False
            return True
        vcmd = (self.root.register(validate_digit), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        def on_exit(event,var):  # Fonction à exécuter lorsque vous quittez l'Entry
            try:
                var.get() 
            except TclError:
                var.set(1)

        # SCROLL DOWN MENU
        labelPrincipal1 = Label(frame_buttons, text="Parametre de la carte", bg="#292929", fg="WHITE", font=("Arial", 20))
        labelPrincipal1.pack()

        mapSize = {"x1" : 1 , "x2" : 2, "x3" : 3, "x4" : 4}
        clicked = StringVar()
        clicked.set("x1")
        drop = OptionMenu(frame_buttons, clicked, *mapSize, )
        drop.config(bg="#292929", fg="WHITE")
        labelMapDetail = Label(frame_buttons, text="Grosseur de la Carte", bg="#292929", fg="WHITE", font=("Arial", 10))
        label3 = Label(frame_buttons, text="", bg="#292929", font=("Arial", 15), fg="WHITE")
        labelMapDetail.pack(anchor=W)
        drop.pack(anchor=W)
        label3.pack(anchor=W, ipady=20)

        waterPerc = {"5%": 5, "10%": 10, "15%": 15, "20%": 20, "25%": 25, "30%": 30, "35%": 35}
        clicked2 = StringVar()
        clicked2.set("10%")
        drop2 = OptionMenu(frame_buttons, clicked2, *waterPerc)
        drop2.config(bg="#292929", fg="WHITE")
        labelWater = Label(frame_buttons, text="Pourcentage d'eau", bg="#292929", fg="WHITE", font=("Arial", 10))
        label2 = Label(frame_buttons, text="", bg="#292929", font=("Arial", 15), fg="WHITE")
        labelWater.pack(anchor=W)
        drop2.pack(anchor=W)
        label2.pack(anchor=W, ipady=20)

        button = Button(frame_buttons, text="Valider", command=valider, bg="#292929", fg="WHITE", font=("Arial", 15))
        button.pack(anchor=W, pady=20)


        #DIV PARAMETRE ANIMAUX
        frame_animaux = Frame(Frame_global, bg="#292929", height=50)
        frame_animaux.pack(padx=30, side=LEFT, anchor=N)

        labelPrincipal2 = Label(frame_animaux, text="Parametre des animaux", bg="#292929", fg="WHITE", font=("Arial", 20))
        labelPrincipal2.pack(anchor=W)

        frameOurs = Frame(frame_animaux, bg="#292929", pady = 5)
        frameOurs.pack(anchor=W)
        nbrOurs = Entry(frameOurs, textvariable=self.Ours, width=10, validate="key", validatecommand=vcmd)
        nbrOurs.bind("<FocusOut>", lambda event: on_exit(event, self.Ours))
        label = Label(frameOurs, text="Ours : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrOurs.pack(side = RIGHT)
        label.pack(side = LEFT)

        frameCerf = Frame(frame_animaux, bg="#292929", pady = 5)
        frameCerf.pack(anchor=W)
        nbrCerf = Entry(frameCerf, textvariable=self.Cerf, width=10, validate="key", validatecommand=vcmd)
        nbrCerf.bind("<FocusOut>", lambda event: on_exit(event, self.Cerf))
        label = Label(frameCerf, text="Cerf : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrCerf.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLoup = Frame(frame_animaux, bg="#292929", pady = 5)
        frameLoup.pack(anchor=W)
        nbrLoup = Entry(frameLoup, textvariable=self.Loup, width=10, validate="key", validatecommand=vcmd)
        nbrLoup.bind("<FocusOut>", lambda event: on_exit(event, self.Loup))
        label = Label(frameLoup, text="Loup : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLoup.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameRaton = Frame(frame_animaux, bg="#292929", pady=5)
        frameRaton.pack(anchor=W)
        nbrRaton = Entry(frameRaton, textvariable=self.Raton, width=10, validate="key", validatecommand=vcmd)
        nbrRaton.bind("<FocusOut>", lambda event: on_exit(event, self.Raton))
        label = Label(frameRaton, text="Raton : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrRaton.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameEcureille = Frame(frame_animaux, bg="#292929", pady=5)
        frameEcureille.pack(anchor=W)
        nbrEcureille = Entry(frameEcureille, textvariable=self.Ecureille, width=10, validate="key", validatecommand=vcmd)
        nbrEcureille.bind("<FocusOut>", lambda event: on_exit(event, self.Ecureille))
        label = Label(frameEcureille, text="Ecureille : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrEcureille.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameCastor = Frame(frame_animaux, bg="#292929", pady=5)
        frameCastor.pack(anchor=W)
        nbrCastor = Entry(frameCastor,textvariable=self.Castor, width=10, validate="key", validatecommand=vcmd)
        nbrCastor.bind("<FocusOut>", lambda event: on_exit(event, self.Castor))
        label = Label(frameCastor, text="Castor : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrCastor.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameRenard = Frame(frame_animaux, bg="#292929", pady=5)
        frameRenard.pack(anchor=W)
        nbrRenard = Entry(frameRenard, textvariable=self.Renard, width=10, validate="key", validatecommand=vcmd)
        nbrRenard.bind("<FocusOut>", lambda event: on_exit(event, self.Renard))
        label = Label(frameRenard, text="Renard : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrRenard.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameOrignial = Frame(frame_animaux, bg="#292929", pady=5)
        frameOrignial.pack(anchor=W)
        nbrOrignial = Entry(frameOrignial, textvariable=self.Orignial, width=10, validate="key", validatecommand=vcmd)
        nbrOrignial.bind("<FocusOut>", lambda event: on_exit(event, self.Orignial))
        label = Label(frameOrignial, text="Orignial : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrOrignial.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLievre = Frame(frame_animaux, bg="#292929", pady=5)
        frameLievre.pack(anchor=W)
        nbrLievre = Entry(frameLievre,textvariable=self.Lievre, width=10, validate="key", validatecommand=vcmd)
        nbrLievre.bind("<FocusOut>", lambda event: on_exit(event, self.Lievre))
        label = Label(frameLievre, text="Lievre : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLievre.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLynx = Frame(frame_animaux, bg="#292929", pady=5)
        frameLynx.pack(anchor=W)
        nbrLynx = Entry(frameLynx, textvariable=self.Lynx, width=10, validate="key", validatecommand=vcmd)
        nbrLynx.bind("<FocusOut>", lambda event: on_exit(event, self.Lynx))
        label = Label(frameLynx, text="Lynx : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLynx.pack(side=RIGHT)
        label.pack(side=LEFT)

        # DIV PARAMETRE VEGETAUX
        frame_environnement = Frame(Frame_global, bg="#292929", height=50, width=20)
        frame_environnement.pack(padx=30, side=LEFT, anchor=N)

        labelPrincipal3 = Label(frame_environnement, text="Parametre végétaux", bg="#292929", fg="WHITE", font=("Arial", 20))
        labelPrincipal3.pack(anchor=W)

        frameSapin = Frame(frame_environnement, bg="#292929", pady=5)
        frameSapin.pack(anchor=W)
        nbrSapin = Entry(frameSapin,textvariable=self.Sapin, width=10, validate="key", validatecommand=vcmd)
        nbrSapin.bind("<FocusOut>", lambda event: on_exit(event, self.Sapin))
        label = Label(frameSapin, text="Sapin : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrSapin.pack(side=RIGHT)
        label.pack(side=LEFT)

        framBleuet = Frame(frame_environnement, bg="#292929", pady=5)
        framBleuet.pack(anchor=W)
        nbrBleuet = Entry(framBleuet, textvariable=self.Bleuet, width=10, validate="key", validatecommand=vcmd)
        nbrBleuet.bind("<FocusOut>", lambda event: on_exit(event, self.Bleuet))
        label = Label(framBleuet, text="Bleuet : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrBleuet.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameBouleau = Frame(frame_environnement, bg="#292929", pady=5)
        frameBouleau.pack(anchor=W)
        nbrBouleau = Entry(frameBouleau, textvariable=self.Bouleau, width=10, validate="key", validatecommand=vcmd)
        nbrBouleau.bind("<FocusOut>", lambda event: on_exit(event, self.Bouleau))
        label = Label(frameBouleau, text="Bouleau : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrBouleau.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameErable = Frame(frame_environnement, bg="#292929", pady=5)
        frameErable.pack(anchor=W)
        nbrErable = Entry(frameErable, textvariable=self.Erable, width=10, validate="key", validatecommand=vcmd)
        nbrErable.bind("<FocusOut>", lambda event: on_exit(event, self.Erable))
        label = Label(frameErable, text="Erable : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrErable.pack(side=RIGHT)
        label.pack(side=LEFT)

        framePissenlit = Frame(frame_environnement, bg="#292929", pady=5)
        framePissenlit.pack(anchor=W)
        nbrPissenlit = Entry(framePissenlit, textvariable=self.Pissenlit, width=10, validate="key", validatecommand=vcmd)
        nbrPissenlit.bind("<FocusOut>", lambda event: on_exit(event, self.Pissenlit))
        label = Label(framePissenlit, text="Pissenlit : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrPissenlit.pack(side=RIGHT)
        label.pack(side=LEFT)

        framePomier = Frame(frame_environnement, bg="#292929", pady=5)
        framePomier.pack(anchor=W)
        nbrPomier = Entry(framePomier, textvariable=self.Pomier, width=10, validate="key", validatecommand=vcmd)
        nbrPomier.bind("<FocusOut>", lambda event: on_exit(event, self.Pomier))
        label = Label(framePomier, text="Pomier : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrPomier.pack(side=RIGHT)
        label.pack(side=LEFT)

        # DIV PARAMETRE TEMPS(ENVIRONNEMENT)
        labelPrincipal4 = Label(frame_environnement, text="Parametre temporel", bg="#292929", fg="WHITE", font=("Arial", 20))
        labelPrincipal4.pack(anchor=W)

        frameJour = Frame(frame_environnement, bg="#292929", pady=5)
        frameJour.pack(anchor=W)
        jourMois = Entry(frameJour, textvariable=self.jour, width=10, validate="key", validatecommand=vcmd)
        jourMois.bind("<FocusOut>", lambda event: on_exit(event, self.jour))
        label = Label(frameJour, text="Jour du mois : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        jourMois.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameMois = Frame(frame_environnement, bg="#292929", pady=5)
        frameMois.pack(anchor=W)
        moisAnnee = Entry(frameMois, textvariable=self.mois, width=10, validate="key", validatecommand=vcmd)
        moisAnnee.bind("<FocusOut>", lambda event: on_exit(event, self.mois))
        label = Label(frameMois, text="Mois de l'année : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        moisAnnee.pack(side=RIGHT)
        label.pack(side=LEFT)


        annee = Frame(frame_environnement, bg="#292929", pady=5)
        annee.pack(anchor=W)
        qteAnnee = Entry(annee,textvariable=self.annee, width=10, validate="key", validatecommand=vcmd)
        qteAnnee.bind("<FocusOut>", lambda event: on_exit(event, self.annee))
        qteAnnee.pack(side=RIGHT)
        label = Label(annee, text="Année de départ : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        label.pack(side=LEFT)


        # DIV start
        start_frame = Frame(frame_buttons, bg="#292929")
        start_frame.pack(fill=X, side=BOTTOM, anchor=W)

        start_preview = Button(start_frame, text="Aperçu", font=("Arial", 20), bg="#292929", fg="WHITE", command=self.new_window_preview,   state=DISABLED)
        self.startButton = Button(start_frame, text="Commencer", font=("Arial", 20), bg="#292929", fg="WHITE", command=self.new_window_start_sim, state=DISABLED)

        start_preview.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.startButton.grid(row=0, column=1, columnspan=1, sticky="nsew")


    def new_window_start_sim(self):
        self.root.destroy()
        self.simroot = Tk()
        self.simroot.title("Accueil")
        self.simroot.geometry("1600x950")
        self.simroot.resizable(False, False)
        self.simroot.config(background="#292929")
        self.mapGeneral = 800
        self.saisonBase = self.parent.model.env.saison
        self.imageIDs = []

        # frame pour les conditions météo et heure
        conditions_frame = Frame(self.simroot, bg="Gray50")
        conditions_frame.pack(pady=5, padx=5, fill=X)

        self.saison_frame = Frame(conditions_frame, bg="#292929")
        self.saison_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.saison_frame, text="Saison: ", bg="gray25", fg="white").pack(side=LEFT)
        self.saison_value_label = Label(self.saison_frame, text=str(self.parent.model.env.saison.nom), bg="gray25", fg="white")
        self.saison_value_label.pack(side=LEFT)

        self.dates_frame = Frame(conditions_frame, bg="#292929")
        self.dates_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.dates_frame, text="Dates: ", bg="gray25", fg="white").pack(side=LEFT)
        self.dates_value_label = Label(self.dates_frame, text=str(self.parent.model.env.dateHeure.get_date()), bg="gray25", fg="white")
        self.dates_value_label.pack(side=LEFT)

        self.heure_frame = Frame(conditions_frame, bg="#292929")
        self.heure_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.heure_frame, text="Heure: ", bg="gray25", fg="white").pack(side=LEFT)
        self.heure_value_label = Label(self.heure_frame, text=str(self.parent.model.env.dateHeure.date.time()), bg="gray25", fg="white")
        self.heure_value_label.pack(side=LEFT)

        self.leve_solei_frame = Frame(conditions_frame, bg="#292929")
        self.leve_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.leve_solei_frame, text="Levé du soleil: ", bg="gray25", fg="white").pack(side=LEFT)
        self.leve_solei = Label(self.leve_solei_frame, text=str(self.parent.model.env.leveeDuSoleil), bg="gray25", fg="white")
        self.leve_solei.pack(side=LEFT)

        self.heure_coucher_solei_frame = Frame(conditions_frame, bg="#292929")
        self.heure_coucher_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.heure_coucher_solei_frame, text="Coucher du soleil: ", bg="gray25", fg="white").pack(side=LEFT)
        self.coucher_solei = Label(self.heure_coucher_solei_frame, text=str(self.parent.model.env.coucherDuSoleil), bg="gray25", fg="white")
        self.coucher_solei.pack(side=LEFT)

        self.apogee_solei_frame = Frame(conditions_frame, bg="#292929")
        self.apogee_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.apogee_solei_frame, text="Apogée solaire: ", bg="gray25", fg="white").pack(side=LEFT)
        self.apogee_solei_value_label = Label(self.apogee_solei_frame, text=str(self.parent.model.env.apogeeSolaire), bg="gray25", fg="white")
        self.apogee_solei_value_label.pack(side=LEFT)

        self.solei_info_frame = Frame(conditions_frame, bg="#292929")
        self.solei_info_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.solei_info_frame, text="Information Soleil: ", bg="gray25", fg="white").pack(side=LEFT)
        self.solei_info_label = Label(self.solei_info_frame, text="Levé" if self.parent.model.env.soleil else "Couché", bg="gray25", fg="white")
        self.solei_info_label.pack(side=LEFT)

        # STATS FRAME
        StatsFrame = Frame(self.simroot, bg="Gray50")
        StatsFrame.pack(pady=5, padx=5, fill=X)

        cardAspect = Frame(StatsFrame, bg="Gray50")
        cardAspect.pack(side=LEFT)

        labelSize = Label(cardAspect, text="Grosseur de la carte : "+str(self.res * 400)+" x "+str(self.res * 400)+" mètres.", bg="gray50", font=('Arial', 13))
        labelSize.pack(anchor=W)

        def show(event):
            self.canva_frame_zoom.delete(ALL) #RESET CANVA

            if 0 < event.x < 266 and 0 < event.y < 266:
                self.carre = 1
            elif 266 < event.x < 532 and 0 < event.y < 266:
                self.carre = 2
            elif 532 < event.x < 800 and 0 < event.y < 266:
                self.carre = 3
            elif 0 < event.x < 266 and 266 < event.y < 532:
                self.carre = 4
            elif 266 < event.x < 532 and 266 < event.y < 532:
                self.carre = 5
            elif 532 < event.x < 800 and 266 < event.y < 532:
                self.carre = 6
            elif 0 < event.x < 266 and 532 < event.y < 800:
                self.carre = 7
            elif 266 < event.x < 532 and 532 < event.y < 800:
                self.carre = 8
            elif 532 < event.x < 800 and 532 < event.y < 800:
                self.carre = 9

            self.respawnTres = True
            labelCellSelect.config(text="Cellule choisie : " + str(self.carre))
            self.currSectionView = self.submap.ALL[self.carre -1]
            zoomView = MAPGENERATOR.Vue(self.canva_frame_zoom)
            zoomView.generate_square(len(self.submap.ALL[self.carre - 1]), self.currSectionView, self.seed.biomeOrder, self.mapGeneral, False)

        # frame pour la simulation
        labelCellSelect = Label(cardAspect, font=("Arial", 30), fg="black", bg="gray50")
        labelCellSelect.pack(anchor=W)

        #INFO POPULATION ANIMAL
        animalAspect = Frame(StatsFrame, bg="Gray50")
        animalAspect.pack(side=RIGHT)

        Label(animalAspect, text="test").pack()

        # GROSSE MAP
        self.canva_frame_general = Canvas(self.simroot, bg="#292929", width=self.mapGeneral, height=self.mapGeneral)
        self.canva_frame_general.pack(side=LEFT, padx=10)
        self.generate_map_on_canvas(self.canva_frame_general, False, self.mapGeneral)
        self.canva_frame_general.bind("<Button-1>", show)
    
        # ZOOM CANVAS
        self.submap = MAPGENERATOR.Sub_Section_Generator(self.res, self.seed.diamond_square.heightmap)
        self.submap.create_whole_map()
        self.submap.sub_divide()
        self.canva_frame_zoom = Canvas(self.simroot, bg="#292929", width=self.mapGeneral, height=self.mapGeneral)
        self.canva_frame_zoom.pack(side=LEFT, padx=10)

        
        self.parent.model.env.dateHeure.Start_Time()
        self.parent.model.env.assignerBiomes(self.seed.biomeOrder)
        self.parent.model.creer_animaux()
        self.parent.model.creer_vegetaux()
        self.parent.model.boucler_simulation()
        

    def update(self):

        # Configurer les labels avec les valeurs actuelles
        self.saison_value_label.config(text=str(self.parent.model.env.saison.nom))
        self.dates_value_label.config(text=str(self.parent.model.env.dateHeure.get_date()))
        self.heure_value_label.config(text=str(self.parent.model.env.dateHeure.date.time()))
        self.leve_solei.config(text=str(self.parent.model.env.leveeDuSoleil))
        self.coucher_solei.config(text=str(self.parent.model.env.coucherDuSoleil))
        self.apogee_solei_value_label.config(text=str(self.parent.model.env.apogeeSolaire))
        self.solei_info_label.config(text="Levé" if self.parent.model.env.soleil else "Couché")

        #self.root.update()
        #self.root.after(300, self.update)


    def on_click(self, event):
        print("salut")


    def generate_map_on_canvas(self, canvas, new, grosseur):
        vue = MAPGENERATOR.Vue(canvas)
        if(new):
            self.seed.generate_map()

        if self.parent.model.env.saison.nom == "été" or self.parent.model.env.saison.nom == "printemps":
            vue.generate_square(self.seed.diamond_square.heightmapWidth, self.seed.diamond_square.heightmap, self.seed.biomeOrder, grosseur, True)
        elif self.parent.model.env.saison.nom == "hiver":
            vue.generate_square_winter(self.seed.diamond_square.heightmapWidth, self.seed.diamond_square.heightmap, self.seed.biomeOrder, grosseur, True)
        elif self.parent.model.env.saison.nom == "automne":
            vue.generate_square_autumn(self.seed.diamond_square.heightmapWidth, self.seed.diamond_square.heightmap, self.seed.biomeOrder, grosseur, True)


    def new_window_preview(self):
        self.startButton['state'] = NORMAL

        if(self.Frame_Preview_show_map):
            self.Frame_Preview_show_map.destroy()

        self.Frame_Preview_show_map = Frame(self.root, bg="#292929", borderwidth=10, width=200)
        label_title = Label(self.Frame_Preview_show_map, text="Map qui sera généré :", font=("Arial", 25), bg="#292929", fg="White")
        label_title.pack()
        self.Frame_Preview_show_map.pack(side=RIGHT)
        canva = Canvas(self.Frame_Preview_show_map, width=400, height=400)
        self.generate_map_on_canvas(canva, True, 400)


    def simulation(self):
        #SPAWN TREES
        if(self.respawnTres):
            self.respawnTres = False
            for i in self.parent.model.vegetaux:
                if (i.region == self.carre):
                    self.canva_frame_zoom.create_image(i.x, i.y, image=i.photo, anchor=tk.CENTER)

        # DELETE PREVIOUS
        if self.imageIDs:
            for i in self.imageIDs:
                self.canva_frame_zoom.delete(i)

        # RESPAWN AT NEW POS
        self.imageIDs.clear()
        for i in self.parent.model.animaux:
            if (i.region == self.carre):
                self.parent.model.deplacer(i)
                self.imageIDs.append(self.canva_frame_zoom.create_image(i.x, i.y, image=i.photo, anchor=tk.CENTER))

        # UPDATE ENVIRONEMENT
        self.update()