from tkinter import *
import MAPGENERATOR
from MAPGENERATOR import *
import Modele

class Vue:
    def __init__(self, parent):
        self.parent = parent
        self.root = Tk()
        self.simroot = None
        self.seed = None
        self.startButton = None
        self.canva_frame_general = None
        self.squares = []
        self.res = 0
        self.submap = None      #ZOOM DE LA MAP
        self.bool = False
        self.currSectionView = None
        self.canva_frame_zoom = None

#       ANIMAUX
        self.Loup = 0
        self.Lievre = 0
        self.Raton = 0
        self.Cerf = 0
        self.Lynx = 0
        self.Renard = 0
        self.Orignial = 0
        self.Ours = 0
        self.Castor = 0
        self.Ecureille = 0

        #ENVIRONNEMENT
        self.hey = None
        self.biomes_frame = None

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
            self.startButton['state'] = DISABLED

            # SET LE NOMBRE ANIMAUX VOULUT DANS LES VARIABLES
            self.Ours = nbrOurs.get()
            self.Ecureille = nbrEcureille.get()
            self.Cerf = nbrCerf.get()
            self.Lievre = nbrLievre.get()
            self.Castor = nbrCastor.get()
            self.Renard = nbrRenard.get()
            self.Lynx = nbrLynx.get()
            self.Loup = nbrLoup.get()
            self.Orignial = nbrOrignial.get()
            self.Raton = nbrRaton.get()

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
        nbrOurs = Entry(frameOurs, width=10)
        nbrOurs.insert(0, 0)
        label = Label(frameOurs, text="Ours : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrOurs.pack(side = RIGHT)
        label.pack(side = LEFT)

        frameCerf = Frame(frame_animaux, bg="#292929", pady = 5)
        frameCerf.pack(anchor=W)
        nbrCerf = Entry(frameCerf, width=10)
        nbrCerf.insert(0, 0)
        label = Label(frameCerf, text="Cerf : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrCerf.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLoup = Frame(frame_animaux, bg="#292929", pady = 5)
        frameLoup.pack(anchor=W)
        nbrLoup = Entry(frameLoup, width=10)
        nbrLoup.insert(0, 0)
        label = Label(frameLoup, text="Loup : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLoup.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameRaton = Frame(frame_animaux, bg="#292929", pady=5)
        frameRaton.pack(anchor=W)
        nbrRaton = Entry(frameRaton, width=10)
        nbrRaton.insert(0, 0)
        label = Label(frameRaton, text="Raton : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrRaton.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameEcureille = Frame(frame_animaux, bg="#292929", pady=5)
        frameEcureille.pack(anchor=W)
        nbrEcureille = Entry(frameEcureille, width=10)
        nbrEcureille.insert(0, 0)
        label = Label(frameEcureille, text="Ecureille : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrEcureille.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameCastor = Frame(frame_animaux, bg="#292929", pady=5)
        frameCastor.pack(anchor=W)
        nbrCastor = Entry(frameCastor, width=10)
        nbrCastor.insert(0, 0)
        label = Label(frameCastor, text="Castor : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrCastor.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameRenard = Frame(frame_animaux, bg="#292929", pady=5)
        frameRenard.pack(anchor=W)
        nbrRenard = Entry(frameRenard, width=10)
        nbrRenard.insert(0, 0)
        label = Label(frameRenard, text="Renard : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrRenard.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameOrignial = Frame(frame_animaux, bg="#292929", pady=5)
        frameOrignial.pack(anchor=W)
        nbrOrignial = Entry(frameOrignial, width=10)
        nbrOrignial.insert(0, 0)
        label = Label(frameOrignial, text="Orignial : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrOrignial.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLievre = Frame(frame_animaux, bg="#292929", pady=5)
        frameLievre.pack(anchor=W)
        nbrLievre = Entry(frameLievre, width=10)
        nbrLievre.insert(0, 0)
        label = Label(frameLievre, text="Lievre : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLievre.pack(side=RIGHT)
        label.pack(side=LEFT)

        frameLynx = Frame(frame_animaux, bg="#292929", pady=5)
        frameLynx.pack(anchor=W)
        nbrLynx = Entry(frameLynx, width=10)
        nbrLynx.insert(0, 0)
        label = Label(frameLynx, text="Lynx : ", bg="#292929", fg="WHITE", font=("Arial", 10), width=15)
        nbrLynx.pack(side=RIGHT)
        label.pack(side=LEFT)

        # DIV PARAMETRE ENVIRONEMNT
        frame_environnement = Frame(Frame_global, bg="red", height=50, width=20)
        frame_environnement.pack(padx=30, side=LEFT, anchor=N)

        labelPrincipal3 = Label(frame_environnement, text="Parametre environnement", bg="#292929", fg="WHITE", font=("Arial", 20))
        labelPrincipal3.pack(anchor=W)


        # DIV start
        start_frame = Frame(frame_buttons, bg="#292929")
        start_frame.pack(fill=X, side=BOTTOM, anchor=W)

        start_preview = Button(start_frame, text="Aperçu", font=("Arial", 20), bg="#292929", fg="gray", command=self.new_window_preview)
        self.startButton = Button(start_frame, text="Commencer", font=("Arial", 20), bg="#292929", fg="gray", command=self.new_window_start_sim, state=DISABLED)

        start_preview.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.startButton.grid(row=0, column=1, columnspan=1, sticky="nsew")


    def new_window_start_sim(self):
        self.root.destroy()
        self.simroot = Tk()
        self.simroot.title("Accueil")
        self.simroot.geometry("1600x900")
        self.simroot.resizable(False, False)
        self.simroot.config(background="#292929")
        self.mapGeneral = 800
        self.carre = 0

        # frame pour les conditions météo et heure
        conditions_frame = Frame(self.simroot, bg="#292929")
        conditions_frame.pack(pady=5, padx=5, fill=X)

        self.biomes_frame = Frame(conditions_frame, bg="gray50")
        self.biomes_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.biomes_frame, text="Biomes: ").pack(side=LEFT)
        self.biomes_value_label = Label(self.biomes_frame, text=str(self.parent.model.env.biome))
        self.biomes_value_label.pack(side=LEFT)

        self.saison_frame = Frame(conditions_frame, bg="gray50")
        self.saison_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.saison_frame, text="Saison: ").pack(side=LEFT)
        self.saison_value_label = Label(self.saison_frame, text=str(self.parent.model.env.saison))
        self.saison_value_label.pack(side=LEFT)

        self.dates_frame = Frame(conditions_frame, bg="gray50")
        self.dates_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.dates_frame, text="Dates: ").pack(side=LEFT)
        self.dates_value_label = Label(self.dates_frame, text=str(self.parent.model.env.dateHeure.get_date()))
        self.dates_value_label.pack(side=LEFT)

        self.heure_frame = Frame(conditions_frame, bg="gray50")
        self.heure_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.heure_frame, text="Heure: ").pack(side=LEFT)
        self.heure_value_label = Label(self.heure_frame, text=str(self.parent.model.env.dateHeure.date.time()))
        self.heure_value_label.pack(side=LEFT)

        self.temp_frame = Frame(conditions_frame, bg="gray50")
        self.temp_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.temp_frame, text="Température: ").pack(side=LEFT)
        self.temp_value_label = Label(self.temp_frame, text=str(self.parent.model.env.temperatureActuel))
        self.temp_value_label.pack(side=LEFT)

        self.humidite_frame = Frame(conditions_frame, bg="gray50")
        self.humidite_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.humidite_frame, text="Humidité: ").pack(side=LEFT)
        self.humidite_value_label = Label(self.humidite_frame, text=str(self.parent.model.env.humiditeActuel * 100))
        self.humidite_value_label.pack(side=LEFT)

        self.solei_max_frame = Frame(conditions_frame, bg="gray50")
        self.solei_max_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.solei_max_frame, text="Soleil max: ").pack(side=LEFT)
        self.solei_max = Label(self.solei_max_frame, text=str(self.parent.model.env.ensoleillementMax * 100))
        self.solei_max.pack(side=LEFT)

        self.solei_actuel_frame = Frame(conditions_frame, bg="gray50")
        self.solei_actuel_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.solei_actuel_frame, text="Ensoillement actuel: ").pack(side=LEFT)
        self.solei_actuel = Label(self.solei_actuel_frame,
                                  text=f"{round(self.parent.model.env.ensoleillementActuel * 100, 3)}" + " %")
        self.solei_actuel.pack(side=LEFT)

        self.leve_solei_frame = Frame(conditions_frame, bg="gray50")
        self.leve_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.leve_solei_frame, text="Levé du soleil: ").pack(side=LEFT)
        self.leve_solei = Label(self.leve_solei_frame, text=str(self.parent.model.env.leveeDuSoleil))
        self.leve_solei.pack(side=LEFT)

        self.heure_coucher_solei_frame = Frame(conditions_frame, bg="gray50")
        self.heure_coucher_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.heure_coucher_solei_frame, text="Coucher du soleil: ").pack(side=LEFT)
        self.coucher_solei = Label(self.heure_coucher_solei_frame, text=str(self.parent.model.env.coucherDuSoleil))
        self.coucher_solei.pack(side=LEFT)

        self.apogee_solei_frame = Frame(conditions_frame, bg="gray50")
        self.apogee_solei_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.apogee_solei_frame, text="Apogée solaire: ").pack(side=LEFT)
        self.apogee_solei_value_label = Label(self.apogee_solei_frame, text=str(self.parent.model.env.apogeeSolaire))
        self.apogee_solei_value_label.pack(side=LEFT)

        self.solei_info_frame = Frame(conditions_frame, bg="gray50")
        self.solei_info_frame.pack(side=LEFT, padx=5, pady=5)
        Label(self.solei_info_frame, text="Information Soleil: ").pack(side=LEFT)
        self.solei_info_label = Label(self.solei_info_frame, text="Levé" if self.parent.model.env.soleil else "Couché")
        self.solei_info_label.pack(side=LEFT)



        labelSize = Label(text="Grosseur de la carte : "+str(self.res * 400)+" x "+str(self.res * 400)+" mètres.", bg="gray50")
        labelSize.pack()

        def show(event):
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
            labelCellSelect.config(text="Cellule choisie : " + str(self.carre))
            self.currSectionView = self.submap.ALL[self.carre -1]
            zoomView = MAPGENERATOR.Vue(self.canva_frame_zoom)
            zoomView.generate_square(len(self.submap.ALL[self.carre - 1]), self.currSectionView, self.seed.biomeOrder, self.mapGeneral, False)

        # frame pour la simulation
        labelCellSelect = Label(self.simroot, font=("Arial", 30), fg="white", bg="#292929")
        labelCellSelect.pack(padx=20, expand=True)

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



        self.parent.model.creer_animaux()
        self.parent.model.boucler_simulation()

    def update(self):

        # Configurer les labels avec les valeurs actuelles
        self.biomes_value_label.config(text=str(self.parent.model.env.biome))
        self.saison_value_label.config(text=str(self.parent.model.env.saison))
        self.dates_value_label.config(text=str(self.parent.model.env.dateHeure.get_date()))
        self.heure_value_label.config(text=str(self.parent.model.env.dateHeure.date.time()))
        self.temp_value_label.config(text=str(self.parent.model.env.temperatureActuel))
        self.humidite_value_label.config(text=str(self.parent.model.env.humiditeActuel * 100))
        self.solei_max.config(text=str(self.parent.model.env.ensoleillementMax * 100))
        self.solei_actuel.config(text=f"{round(self.parent.model.env.ensoleillementActuel * 100, 3)}" + " %")
        self.leve_solei.config(text=str(self.parent.model.env.leveeDuSoleil))
        self.coucher_solei.config(text=str(self.parent.model.env.coucherDuSoleil))
        self.apogee_solei_value_label.config(text=str(self.parent.model.env.apogeeSolaire))
        self.solei_info_label.config(text="Levé" if self.parent.model.env.soleil else "Couché")

        self.root.update()
        self.root.after(300, self.update)

    def on_click(self, event):
        print("salut")

    def generate_map_on_canvas(self, canvas, new, grosseur):
        vue = MAPGENERATOR.Vue(canvas)
        if(new):
            self.seed.generate_map()

        vue.generate_square(self.seed.diamond_square.heightmapWidth, self.seed.diamond_square.heightmap, self.seed.biomeOrder, grosseur, True)

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
        for i in self.parent.model.animaux:
            self.canva_frame_zoom.create_image(i.x, i.y, image=i.photo, anchor=tk.CENTER)

        self.update()

