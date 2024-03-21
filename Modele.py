import Environnement
import Time

class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.environnement= None
        self.date=None
        
    def debuterTemps(self):
        self.date = Time() #class codé en sorte qu'il n'y ai qu'un seul repre temporelle