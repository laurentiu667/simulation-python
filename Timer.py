from datetime import datetime, timedelta, time
import threading
import time as T
import calendar

class Timer:
    LOCK = threading.Lock()  # Verrou autorise un seul thread à la fois à accéder
    _instance = None

    def __new__(cls, *args, **kwargs):
        with cls.LOCK:
            if not cls._instance:
                cls._instance = super(Timer, cls).__new__(cls)
        return cls._instance

    def __init__(self, e = None, annee = 1, mois = 1, jour = 1, heure = 0, minute = 0, seconde = 0):
        if not hasattr(self, 'initialized'):  # Eviter l'initialisation multiple(vérifie si l'objet Timer a déjà été initialisé)
            self.environnement = e
            self.date_initiale = datetime(annee,mois,jour,heure,minute,seconde)
            self.date = self.date_initiale
            
            self.thread = None
            self.running = False
            self.initialized = True
    
    
    def Start_Time(self):
        
        def update_timer():
            while self.running:
                with Timer.LOCK:
                    self.date += timedelta(seconds=3600)
                T.sleep(1)
            
        if self.thread is None:
            self.thread = threading.Thread(target=update_timer)
            self.running = True
            self.thread.start()
            
    def stopperTemps(self):
        self.running = False  # stopper la mise a jour du repere temporelle pour pouvoir en creer un autre plus tard
        self.thread.join()  # Attendre que le thread se termine proprement
            
    @classmethod
    def reset_instance(cls):
        with cls.LOCK:
            if cls._instance is not None:
                cls._instance.running = False
                cls._instance = None
        
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

    def __str__(self):  # permet de print(self.var(stock la classe Timer)) directment le temps
        return self.date.strftime("%d/%m/%Y %H:%M:%S")

    def get_date(self):
        return self.date.strftime("%d/%m/%Y")

    def get_time(self, time=None):
        if time is not None:
            return time.strftime("%H:%M:%S")
        return self.date.strftime("%H:%M:%S")
    
    @staticmethod
    def nombreDeJoursDumois(year,month):
        return calendar.monthrange(year, month)[1]

    def nombreDeJoursDeLaSaison(self, saison=None):
        if saison is not None:
            return sum([calendar.monthrange(self.date.year, month)[1] for month in saison.mois])

        return sum([calendar.monthrange(self.date.year, month)[1] for month in self.environnement.saison.mois])

    def joursDepuisDebutSaison(self):
        from Saison import Hiver  # import ici pour eviter les import circulaire
        if isinstance(self.environnement.saison, Hiver):
            if self.date.year == 1:
                date_debut_saison = self.date_initiale
            else:
                date_debut_saison = datetime(self.date.year - 1, self.environnement.saison.mois[0], 1)
        else:
            date_debut_saison = datetime(self.date.year, self.environnement.saison.mois[0],
                                         1)  # Assumons que la saison commence le premier jour du premier mois de la saison
        jours_ecoules = (self.date - date_debut_saison).days
        return 1 if jours_ecoules == 0 else jours_ecoules

    def total_seconds(self, timeObj=None):  # par default renvoie le nombre de seconde de la journée en cours
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

if __name__ == "__main__":
    
    t = Timer()
    t.Start_Time()
    t1 = None
    t.Start_Time()
    while True:
        print(t.get_time())
        if t1 is not None:
            print(t1.get_time())
        T.sleep(1)
        if t.date.hour > 10:
            if t1 is None:
                t1 = Timer()
            
