from datetime import datetime, timedelta
import threading
import time

class Timer:
    LOCK = threading.Lock() # Verrou  n'autorise qu'un seul repre temporelle 
    def __init__(self):
        self.date_initiale = self.date = datetime(1, 1, 1, 0, 0, 0)
        self.thread = threading.Thread(target=self.update_timer).start()  # Démarre le thread de mise à jour du timer

    def update_timer(self):
        """Avance le temps d'une seconde."""
        with Timer.LOCK:  # Acquiert le verrou
            while True:
                self.date += timedelta(seconds=36000000)
                time.sleep(1)
    
    def get_date(self):
        return self.date.strftime("%d/%m/%Y")
    
    def get_time(self):
        return self.date.strftime("%H:%M %S")    
    
    def temps_ecoule(self, format='secondes'):
        """Retourne le temps total écoulé depuis l'initialisation de l'objet."""
        temps_ecoule = self.date - self.date_initiale
        total_seconds = temps_ecoule.total_seconds()

        if format == 'secondes':
            return total_seconds
        elif format == 'minutes':
            return total_seconds / 60
        elif format == 'heures':
            return total_seconds / 3600
        elif format == 'jours':
            return total_seconds / (24 * 3600)
        elif format == 'mois':
            return total_seconds / (30 * 24 * 3600)
        elif format == 'annees':
            return total_seconds / (365 * 24 * 3600)
        else:
            return "Format non reconnu"

    def __str__(self): # permet de print(self.temps) directment le temps
        return self.date.strftime("%d/%m/%Y %H:%M:%S")