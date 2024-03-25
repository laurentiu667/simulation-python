from tkinter import *
import MAPGENERATOR
from MAPGENERATOR import *

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
        self.submap = MAPGENERATOR.Sub_Section_Generator()


    def accueil(self):
        self.root.title("Accueil")
        self.root.geometry("1300x700")
        self.root.resizable(False, False)
        self.root.config(background="#292929")
        self.Frame_Preview_show_map = None

        Frame_global = Frame(self.root, bg="#292929")
        Frame_global.pack(fill=BOTH, expand=True, side=LEFT)

        # Div du titre
        frame_title = Frame(Frame_global, bg="#292929")
        frame_title.pack(pady=10, padx=30, fill=BOTH)
        label_title = Label(frame_title, text="Simulation", font=("Arial", 50), bg="#292929", fg="gray")
        label_title.pack()

        # Div des Configurations
        frame_buttons = Frame(Frame_global, bg="#292929")
        frame_buttons.pack(padx=30, anchor=W)

        # Confirmer les changement et les appliquées
        def valider():
            label.config(text=clicked.get())
            label2.config(text=clicked2.get())

            self.res = (mapSize[clicked.get()])
            water = waterPerc[clicked2.get()]

            self.seed = self.MAPGENERATOR.Seed(water)  #SEED GENERATES HERE!!!!!!!!
            self.startButton['state'] = DISABLED

        # SCROLL DOWN MENU
        mapSize = {"200x200" : 200, "400x400" : 400 , "600x600" : 600, "800x800" : 800, "1000x1000" : 1000, "1200x1200" : 1200, "1400x1400" : 1400}
        clicked = StringVar()
        clicked.set("200x200")
        drop = OptionMenu(frame_buttons, clicked, *mapSize, )
        drop.config(bg="#292929", fg="WHITE")
        labelMapDetail = Label(frame_buttons, text="Grosseur de la Carte", bg="#292929", fg="WHITE", font=("Arial", 15))
        label = Label(frame_buttons, text="", bg="#292929", font=("Arial", 15), fg="WHITE")
        labelMapDetail.pack(anchor=W)
        drop.pack(anchor=W)
        label.pack(anchor=W, ipady=20)

        waterPerc = {"5%": 5, "10%": 10, "15%": 15, "20%": 20, "25%": 25, "30%": 30, "35%": 35}
        clicked2 = StringVar()
        clicked2.set("10%")
        drop2 = OptionMenu(frame_buttons, clicked2, *waterPerc)
        drop2.config(bg="#292929", fg="WHITE")
        labelWater = Label(frame_buttons, text="Pourcentage d'eau", bg="#292929", fg="WHITE", font=("Arial", 15))
        label2 = Label(frame_buttons, text="", bg="#292929", font=("Arial", 15), fg="WHITE")
        labelWater.pack(anchor=W)
        drop2.pack(anchor=W)
        label2.pack(anchor=W, ipady=20)

        button = Button(frame_buttons, text="Valider", command=valider, bg="#292929", fg="WHITE", font=("Arial", 15))
        button.pack(anchor=W, pady=20)

        # DIV start
        start_frame = Frame(Frame_global, bg="#292929")
        start_frame.pack(fill=X, pady=10, padx=30)

        start_preview = Button(start_frame, text="Aperçu", font=("Arial", 20), bg="#292929", fg="gray", command=self.new_window_preview)
        self.startButton = Button(start_frame, text="Commencer", font=("Arial", 20), bg="#292929", fg="gray", command=self.new_window_start_sim, state=DISABLED)

        start_preview.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.startButton.grid(row=0, column=1, columnspan=1, sticky="nsew")


    def new_window_start_sim(self):
        self.root.destroy()
        self.simroot = Tk()
        self.simroot.title("Accueil")
        self.simroot.geometry("1500x800")
        self.simroot.resizable(False, False)
        self.simroot.config(background="#292929")
        self.mapGeneral = 600
        self.carre = 0

        # frame pour les conditions meteo et heure
        conditions_frame = Frame(self.simroot, bg="#292929", height=50)
        conditions_frame.pack(pady=5, padx=5,fill=X)

        # frame pour les conditions meteo
        conditions_heures_frame = Frame(conditions_frame, bg="gray50", height=40)
        conditions_heures_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        conditions_meteo_frame = Frame(conditions_frame, bg="gray50")
        conditions_meteo_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        conditions_precipitation_frame = Frame(conditions_frame, bg="gray50")
        conditions_precipitation_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_pause_frame = Frame(conditions_frame, bg="gray50")
        button_pause_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_arrêter_frame = Frame(conditions_frame, bg="gray50")
        button_arrêter_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_fastforward_frame = Frame(conditions_frame, bg="gray50")
        button_fastforward_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        def show(event):
            if 0 < event.x < 199 and 0 < event.y < 199:
                self.carre = 1
            elif 199 < event.x < 399 and 0 < event.y < 199:
                self.carre = 2
            elif 399 < event.x < 599 and 0 < event.y < 199:
                self.carre = 3
            elif 0 < event.x < 199 and 199 < event.y < 399:
                self.carre = 4
            elif 199 < event.x < 399 and 199 < event.y < 399:
                self.carre = 5
            elif 399 < event.x < 599 and 199 < event.y < 399:
                self.carre = 6
            elif 0 < event.x < 199 and 399 < event.y < 599:
                self.carre = 7
            elif 199 < event.x < 399 and 399 < event.y < 599:
                self.carre = 8
            elif 399 < event.x < 599 and 399 < event.y < 599:
                self.carre = 9
            labelCellSelect.config(text="Cellule choisie : " + str(self.carre))

        # frame pour la simulation
        labelCellSelect = Label(self.simroot, font=("Arial", 30), fg="white", bg="#292929")
        labelCellSelect.pack(padx=20, expand=True, anchor=W)

        self.canva_frame_general = Canvas(self.simroot, bg="#292929", width=self.mapGeneral, height=self.mapGeneral)
        self.canva_frame_general.pack(padx=20,expand=True, anchor=W)
        self.generate_map_on_canvas(self.canva_frame_general, False, self.mapGeneral)
        self.canva_frame_general.bind("<Button-1>", show)

        self.submap.create_whole_map(self.res, self.mapGeneral, self.seed.diamond_square.heightmap)

    def on_click(self, event):
        print("salut")

    def generate_map_on_canvas(self, canvas, new, grosseur):
        vue = MAPGENERATOR.Vue(canvas)
        if(new):
            self.seed.generate_map()


        vue.generate_square(self.seed.diamond_square.heightmapWidth, self.seed.diamond_square.heightmap, self.seed.biomeOrder, grosseur)

    def new_window_preview(self):
        self.startButton['state'] = NORMAL

        if(self.Frame_Preview_show_map):
            self.Frame_Preview_show_map.destroy()

        self.Frame_Preview_show_map = Frame(self.root, bg="#292929", borderwidth=10)
        label_title = Label(self.Frame_Preview_show_map, text="Map qui sera généré :", font=("Arial", 25), bg="#292929", fg="White")
        label_title.pack()
        self.Frame_Preview_show_map.pack(side=RIGHT)
        canva = Canvas(self.Frame_Preview_show_map, width=400, height=400)
        self.generate_map_on_canvas(canva, True, 400)

    def simulation(self):
        pass
