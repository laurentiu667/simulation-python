from tkinter import *
import MAPGENERATOR
from MAPGENERATOR import *

class Vue:
    def __init__(self, parent, model):
        self.parent = parent
        self.model = model
        self.root = Tk()
        self.simroot = None
        self.seed = None
        self.startButton = None
        self.canva_frame = None
        self.squares = []
        self.res = 0


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
        frame_buttons.pack(padx=30, fill=BOTH)

        def valider():
            label.config(text=clicked.get())
            label2.config(text=clicked2.get())
            self.res = (mapSize[clicked.get()])
            water = waterPerc[clicked2.get()]

            self.seed = MAPGENERATOR.Seed(water)
            self.startButton['state'] = DISABLED

        mapSize = {"150x150" : 150, "300x300" : 300 , "600x600" : 600, "900x900" : 900, "1200x1200" : 1200, "1500x1500" : 1500, "1800x1800" : 1800}
        clicked = StringVar()
        clicked.set("300x300")
        drop = OptionMenu(frame_buttons, clicked, *mapSize)
        labelMapDetail = Label(frame_buttons, text="Grosseur de la Carte")
        label = Label(frame_buttons, text="")
        labelMapDetail.pack()
        drop.pack()
        label.pack()

        waterPerc = {"5%": 5, "10%": 10, "15%": 15, "20%": 20, "25%": 25, "30%": 30, "35%": 35}
        clicked2 = StringVar()
        clicked2.set("10%")
        drop2 = OptionMenu(frame_buttons, clicked2, *waterPerc)
        labelWater = Label(frame_buttons, text="Pourcentage d'eau")
        label2 = Label(frame_buttons, text="")
        labelWater.pack()
        drop2.pack()
        label2.pack()

        button = Button(frame_buttons, text="Valider", command=valider)
        button.pack()

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
        self.simroot.geometry("1000x1700")
        self.simroot.resizable(False, False)
        self.simroot.config(background="#561C24")

        # frame pour les conditions meteo et heure
        conditions_frame = Frame(self.simroot, bg="white", height=50)
        conditions_frame.pack(pady=5, padx=5,fill=X)

        # frame pour les conditions meteo
        conditions_heures_frame = Frame(conditions_frame, bg="blue", height=40)
        conditions_heures_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        conditions_meteo_frame = Frame(conditions_frame, bg="blue")
        conditions_meteo_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        conditions_precipitation_frame = Frame(conditions_frame, bg="blue")
        conditions_precipitation_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_pause_frame = Frame(conditions_frame, bg="blue")
        button_pause_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_arrêter_frame = Frame(conditions_frame, bg="blue")
        button_arrêter_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        button_fastforward_frame = Frame(conditions_frame, bg="blue")
        button_fastforward_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        # frame pour la simulation
        Frame_simulation = Frame(self.simroot, bg="gray50")
        Frame_simulation.pack(pady=5, padx=5, fill=BOTH, expand=True)
        self.canva_frame = Canvas(Frame_simulation, bg="gray")
        self.canva_frame.pack(pady=5, padx=5, fill=BOTH, expand=True)
        self.generate_map_on_canvas(self.canva_frame, False, 600)

        res = self.res/3
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
               self.canva_frame.create_rectangle(res*i, res*i, res*(j+1), res*(j+1), fill="", outline="", tags=str(i * j))


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

        self.Frame_Preview_show_map = Frame(self.root, bg="#292929")
        label_title = Label(self.Frame_Preview_show_map, text="Map qui sera généré :", font=("Arial", 25), bg="#292929", fg="White")
        label_title.pack()
        self.Frame_Preview_show_map.pack(side=RIGHT)
        canva = Canvas(self.Frame_Preview_show_map, width=400, height=400)
        self.generate_map_on_canvas(canva, True, 400)

    def simulation(self):
        pass
