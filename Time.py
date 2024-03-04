import time
from datetime import datetime

# Classe pour suivre le temps écoulé et effectuer toute manipulation le concernant
# pourrait inclure la gestion  d'actualisation de l'ecran (fps)

class Time:
    def __init__(self):
        self.start_time = None

    def set_start_time(self, time=None):
        """Définit le temps de départ. Si aucun temps n'est fourni, utilise l'heure actuelle."""
        if time is None:
            self.start_time = datetime.now()
        else:
            self.start_time = time

    def time_elapsed(self, end_time=None):
        """Calcule le temps écoulé depuis le temps de départ jusqu'à l'heure actuelle ou un temps donné."""
        if self.start_time is None:
            raise ValueError("Le temps de départ n'a pas été défini.")
        
        if end_time is None:
            end_time = datetime.now()
        
        elapsed = end_time - self.start_time
        return elapsed

# Exemple d'utilisation
time_tracker = Time()

# Définit le temps de départ à maintenant
time_tracker.set_start_time()

# Calcul et affichage du temps écoulé après un certain délai (par exemple, après quelques secondes)
time.sleep(5)  # Attend 5 secondes

elapsed_time = time_tracker.time_elapsed()
print(f"Temps écoulé: {elapsed_time}")
