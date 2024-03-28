from datetime import datetime, timedelta, time
import threading
import time as T
import calendar


class Timer:
    LOCK = threading.Lock() # Verrou  n'autorise qu'un seul repre temporelle 
    def __init__(self, e):
        self.e = e
        self.date_initiale = self.date = datetime(1, 1, 1, 0, 0, 0)
        self.thread = threading.Thread(target=self.update_timer).start()  # Démarre le thread de mise à jour du timer
    
    
    @staticmethod
    def obtenirUneHeure(heure=0, minute=0, seconde=0):
        return time(heure, minute, seconde)
    
    @staticmethod
    def convertirSecondeEnDuree(secondes):
        return timedelta(seconds=secondes)
    
    @staticmethod
    def addTime(timeObj, delta):
        """Ajoute un timedelta à un objet time et retourne un nouvel objet time."""
        # Convertit time en datetime (date arbitraire)
        datetime_obj = datetime(1, 1, 1, timeObj.hour, timeObj.minute, timeObj.second)
        
        # Ajoute le timedelta
        new_datetime_obj = datetime_obj + delta
        
        # Retourne un nouvel objet time
        return new_datetime_obj.time()
       
       
    def __str__(self): # permet de print(self.temps) directment le temps
        return self.date.strftime("%d/%m/%Y %H:%M:%S")


    def update_timer(self):
        """Avance le temps d'une seconde."""
        with Timer.LOCK:  # Acquiert le verrou
            while True:
                self.date += timedelta(seconds=1800)
                T.sleep(1) # peut etre penser a synchro l'affichage et le temps si on veut tout voir en temps reel
    
    
    def get_date(self):
        return self.date.strftime("%d/%m/%Y")
    
    def get_time(self, time = None):
        if time is not None:
            return time.strftime("%H:%M:%S")
        return self.date.strftime("%H:%M:%S")
        
    
    def nombreDeJoursDumois(self, month = None):
        if month is not None:
            return calendar.monthrange(self.date.year, month)[1]
        return calendar.monthrange(self.date.year, self.date.month)[1]
    
    
    def nombreDeJoursDeLaSaison(self, saison = None):
        if saison is not None:
            return sum([calendar.monthrange(self.date.year, month)[1] for month in saison.mois])

        return  sum([calendar.monthrange(self.date.year, month)[1] for month in self.e.saison.mois])

    def joursDepuisDebutSaison(self):
        from Saison import Hiver # import ici pour eviter les import circulaire
        if isinstance(self.e.saison, Hiver):
            if self.date.year == 1:
                date_debut_saison = self.date_initiale
            else:
                date_debut_saison = datetime(self.date.year - 1, self.e.saison.mois[0], 1)
        else:
            date_debut_saison = datetime(self.date.year, self.e.saison.mois[0], 1)  # Assumons que la saison commence le premier jour du premier mois de la saison
        jours_ecoules = (self.date - date_debut_saison).days
        return 1 if jours_ecoules == 0 else jours_ecoules
    
    def total_seconds(self, timeObj = None): # par default renvoie le nombre de seconde de la journée en cours 
        if timeObj is None:
            timeObj = self.date
        return (timeObj.hour * 3600) + (timeObj.minute * 60) + timeObj.second
    
    
    def tempsEcouleTotal(self, format='secondes'):
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

    