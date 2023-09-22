import numpy as np

class Puissance4:

    def __init__(self, j_start):

        self.x = 6
        self.y = 7

        self.nb_aligne = 4


        self.tab = np.full((self.x, self.y), 0)

        self.j_start = j_start
        self.joueurTour = j_start

        self.dernier_coup = (-1, -1)

    # permet de récupérer le joueur qui joue
    def get_joueurTour(self):
        return self.joueurTour

    # permet de récuper la matrice (je crois qu'on peut utiliser un truc comme copy mais pas sur)
    def get_tab(self):
        return self.tab[:]

    # permet de récupérer la taille x
    def getX(self):
        return self.x

    #permet de récupérer la taille y
    def getY(self):
        return self.y

    # permet de réinitialiser la partie mais pas utiliser pour le moment
    def reinit(self):
        self.tab = np.full((self.x, self.y), 0)
        self.dernier_coup = (-1, -1)
        self.joueurTour = self.j_start

    # dit si la partie est fini
    def partie_fini(self):
        if self.test_aligne():
            print(f"Partie Fini, le joueur {self.joueurTour} à Gagné.")
            return True
        if len(self.colonnes_vides()) == 0:
            print("Partie Fini, Match nul.")
            return True
        return False

    #récupère les colonnes vides
    def colonnes_vides(self):
        return [i for i in range(np.shape(self.tab)[1]) if self.tab[0, i] == 0]

    # appelle la compte_aligne qui compte le nombre de pion aligné en fonction d'un axe
    def test_aligne(self):
        """if self.dernier_coup != (-1, -1):
            for dir in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                if self.compte_aligne(dir[0], dir[1]) >= self.nb_aligne:
                    print(dir[0], dir[1], self.nb_aligne)
                    return True
        return False"""
        n, p = np.shape(self.tab)
        for i in range(n):
            for j in range(p - 3):
                if self.tab[i, j] == self.joueurTour and self.tab[i, j + 1] == self.joueurTour and self.tab[i, j + 2] == self.joueurTour and self.tab[i, j + 3] == self.joueurTour:
                    return True

        for j in range(p):
            for i in range(n - 3):
                if self.tab[i, j] == self.joueurTour and self.tab[i + 1, j] == self.joueurTour and self.tab[i + 2, j] == self.joueurTour and self.tab[i + 3, j] == self.joueurTour:
                    return True

        for i in range(n - 3):
            for j in range(p - 3):
                if self.tab[i, j] == self.joueurTour and self.tab[i + 1, j + 1] == self.joueurTour and self.tab[i + 2, j + 2] == self.joueurTour and self.tab[i + 3, j + 3] == self.joueurTour:
                    return True

        for i in range(n - 3):
            for j in range(3, p):
                if self.tab[i, j] == self.joueurTour and self.tab[i + 1, j - 1] == self.joueurTour and self.tab[i + 2, j - 2] == self.joueurTour and self.tab[i + 3, j - 3] == self.joueurTour:
                    return True

        return False

    # compte le nombre de pion aligné en fonction d'un axe x, y
    def compte_aligne(self, x, y):
        nb = 1
        cpt_x = x
        cpt_y = y
        for i in range(2):
            while (self.y > self.dernier_coup[1]+cpt_y >= 0) and (self.x > self.dernier_coup[0]+cpt_x >= 0) and (self.tab[self.dernier_coup[0]+cpt_x, self.dernier_coup[1]+cpt_y] == self.joueurTour):
                nb += 1
                if cpt_x >= 0:
                    cpt_x += x
                else:
                    cpt_x -= x

                if cpt_y >= 0:
                    cpt_y += y
                else:
                    cpt_y -= y

            cpt_x = x * -1
            cpt_y = y * -1

        return nb

    # permet de poser un pion
    def poser_pion(self, y):
        x = 0
        if y in self.colonnes_vides():
            while x+1 < self.x and self.tab[x+1, y] == 0:
                x += 1
            self.tab[x, y] = self.joueurTour
            self.dernier_coup = (x, y)
            return True
        return False

    # passe au joueur d'après
    def changer_joueur(self):
        self.joueurTour = self.joueurTour%2 + 1

    # permet d'afficher en console plus jolie
    def affiche_plateau(self):
        res = ""

        for i in range(self.y):
            res += "  " + str(i) + " "
        res += " \n"

        for i in range(self.y):
            res += "===="
        res += "=\n"

        for x in range(self.x):
            for y in range(self.y):
                if self.tab[x, y] == -1:
                    res += "|   "
                else:
                    res += "| " + str(self.tab[x, y]) + " "
            res += "|\n"
            for i in range(self.y):
                res += "===="
            res += "=\n"

        print(res)