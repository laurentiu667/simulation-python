import tkinter as tk

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Image de loup avec Tkinter")
canevas = tk.Canvas(root, width=100,height=100,bg="green")
canevas.pack()
mon_ours = tk.PhotoImage(file="bear.png")
canevas.create_image(80,80,anchor="center", image=mon_ours)

# Lancer la boucle principale de tkinter
root.mainloop()
