from tkinter import *
from tkinter import ttk

import MAPGENERATOR
from MAPGENERATOR import *
class Vue:
    def __init__(self, parent, model):
        self.parent = parent
        self.model = model
        self.root = Tk()
        self.simroot = None


    def accueil(self):
        self.root.title("Accueil")
        self.root.geometry("1400x700")
        self.root.resizable(False, False)
        self.root.config(background="#561C24")
        self.Frame_Preview_show_map = Frame(self.root, bg="#C7B7A3")

        Frame_global = Frame(self.root, bg="#C7B7A3")
        Frame_global.pack(fill=BOTH, expand=True, side=LEFT)


        self.Frame_Preview_show_map.pack( side=RIGHT)

        # Div du titre
        frame_title = Frame(Frame_global, bg="#C7B7A3")
        frame_title.pack(pady=10, padx=30, fill=BOTH)
        label_title = Label(frame_title, text="Simulation", font=("Arial", 50), bg="#C7B7A3", fg="Black")
        label_title.pack()

        # Div des boutons
        frame_buttons = Frame(Frame_global, bg="#C7B7A3")
        frame_buttons.pack(padx=30, fill=BOTH, expand=True)


        settings_frame = Frame(frame_buttons, bg="white")
        settings_frame.pack(pady=10, padx=30, fill=X)
        label_settings = Label(settings_frame, text="Settings", font=("Arial", 20), bg="white", fg="Black", height=1)
        label_settings.pack(padx=10)


        groupeboutton = Frame(frame_buttons, bg="#C7B7A3")
        groupeboutton.pack(pady=10, padx=30, fill=BOTH, expand=True)

        buttons_frame = Frame(groupeboutton, bg="#C7B7A3")
        buttons_frame.pack()

        # center les buttons
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        for i in range(4):
            for j in range(5):
                entry = Entry(buttons_frame, font=("Arial", 20), bg="#C7B7A3",
                                fg="Black", width=9)
                entry.grid(row=i, column=j, padx=3, pady=20)

        # DIV start
        start_frame = Frame(Frame_global, bg="#C7B7A3")
        start_frame.pack(fill=X, pady=10, padx=30)

        start_preview = Button(start_frame, text="Preview", font=("Arial", 20), bg="#C7B7A3", fg="Black", command=self.new_window_preview)
        start_button = Button(start_frame, text="Start", font=("Arial", 20), bg="#C7B7A3", fg="Black", command=self.new_window_start_sim)

        start_preview.grid(row=0, column=0, columnspan=1, sticky="nsew")
        start_button.grid(row=0, column=1, columnspan=1, sticky="nsew")


    def new_window_start_sim(self):
        self.root.destroy()
        self.simroot = Tk()
        self.simroot.title("Accueil")
        self.simroot.geometry("900x700")
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
        Frame_simulation = Frame(self.simroot, bg="red")
        Frame_simulation.pack(pady=5, padx=5, fill=BOTH, expand=True)
        canva_frame = Canvas(Frame_simulation, bg="blue")
        canva_frame.pack(pady=5, padx=5, fill=BOTH, expand=True)
        Text = Label(canva_frame, text="Simulation", font=("Arial", 20), bg="green", fg="Black")
        Text.pack(fill=BOTH, expand=True)


    def new_window_preview(self):

        vue = MAPGENERATOR.Vue(500, self.Frame_Preview_show_map)

        seed = MAPGENERATOR.Seed()
        seed.generate_map()
        vue.generate_square(seed.diamond_square.heightmapWidth, seed.diamond_square.heightmap)

        vue.root.mainloop()

    def simulation(self):
        pass