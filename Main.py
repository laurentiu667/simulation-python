
from Vue import Vue
from Modele import Modele

#main
class Controller:

    def __init__(self):
        self.model = Modele(self)
        self.view = Vue(self, self.model)
        self.view.accueil()

        self.view.root.mainloop()


if __name__ == "__main__":
    c = Controller()
