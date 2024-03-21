import Environnement
import Time

class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.environnement= None
        self.date=None
        #self.debuterTemps() #initialisation du temps seulement si c'est le model final
        
    def debuterTemps(self):
        self.date = Time() #class codé en sorte qu'il n'y ai qu'un seul repere temporelle
        
    def stopperTemps(self):
        self.date.thread.stop() #stopper la mise a jour du repere temporelle pour pouvoir en creer un autre plus tard
        self.date.thread.join()  # Attendre que le thread se termine proprement

        