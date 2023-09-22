import pygame as pg
from game import Puissance4
from maxmin import *
import asyncio

class Graphique:

    def __init__(self):
        pg.init()
        self.p = Puissance4(1)

        self.click_souris = False
        self.partie_fini = False

        self.size = 100
        Tplateau = self.p.getY()*self.size+self.size//10, self.p.getX()*self.size+self.size//10

        self.window = pg.display.set_mode(Tplateau)
        pg.display.set_caption('Puissance 4')
        self.clock = pg.time.Clock()


    #méthode qui permet de dessiner/afficher l'image à l'écran
    def draw(self):
        self.window.fill("black")
        for x in range(self.p.getX()):
            for y in range(self.p.getY()):
                if self.p.get_tab()[x, y] == 0:
                    if self.size//10+y*self.size < pg.mouse.get_pos()[0] <= (self.size//10+y*self.size)+(self.size-self.size//10):
                        if not self.partie_fini:
                            lig = 0
                            while lig + 1 < self.p.getX() and self.p.get_tab()[lig + 1, y] == 0:
                                lig += 1
                            if lig != x:
                                color = "grey"
                            else:
                                if self.p.get_joueurTour() == 1:
                                    color = (250,128,114)
                                else:
                                    color = (240,230,140)
                        else:
                            color = "grey"
                    else:
                        color = "grey"
                elif self.p.get_tab()[x, y] == 1:
                    color = "red"
                else:
                    color = "yellow"
                pg.draw.rect(self.window, (105,105,105), (self.size//10+y*self.size, self.size//10+x*self.size, self.size-self.size//10, self.size-self.size//10))
                pg.draw.circle(self.window, color, (self.size//2+self.size//20+(y*self.size), self.size//2+self.size//20+(x*self.size)), self.size//2.5)

    #méthode qui permet de récupérer les colonnes vides
    def recupere_colonne(self):
        for y in range(self.p.getY()):
            if self.size // 10 + y * self.size < pg.mouse.get_pos()[0] <= (self.size // 10 + y * self.size) + (self.size - self.size // 10):
                return y

    #méthode qui permet de poser un pion avec les coordonnées et input de la souris en appelant la méthode pour poser un pion de la classe puissance4
    def poser_pion(self):
        if self.click_souris:
            if self.recupere_colonne() in self.p.colonnes_vides():
                if self.p.poser_pion(self.recupere_colonne()):
                    return True
        return False

    # boucle principale qui gère tout le programme (garder ouvert la fenetre etc) et ou toutes les méthodes sont appelé
    async def mainloop(self):

        run = True
        while run:

            for event in pg.event.get():
                # fermer la fenetre si on clique sur la croix
                if event.type == pg.QUIT:
                    run = False

                # vérifie si on clique sur la souris (bouton 1) et si on laisse pas enfoncé
                if event.type == pg.MOUSEBUTTONDOWN and not self.click_souris:
                    if event.button == 1:
                        self.click_souris = True

                        # si c au tour du joueur 1 et qu'on a cliqué et que la partie n'est pas fini on pose le pion
                        if self.p.get_joueurTour() in (1, 2):
                            if not self.partie_fini:
                                if self.poser_pion():
                                    if self.p.partie_fini():
                                        self.partie_fini = True
                                    else:
                                        self.p.changer_joueur()

                # vérifie si on a relaché la souris
                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click_souris = False

            """
            # si le joueur est le joueur 2 l'ia joue
            # choix_ia() est l'appel à ton programme
            if self.p.get_joueurTour() == 2:
                if not self.partie_fini:
                    if self.p.poser_pion(choix_ia(4, self.p.get_tab())):
                        if self.p.partie_fini():
                            self.partie_fini = True
                        else:
                            self.p.changer_joueur()"""

            # permet d'afficher l'image avec la methode draw, de mettre à jour l'affichage, et les fait touné le
            # programme à 60 fps si je dis pas de betise
            self.draw()
            pg.display.update()
            self.clock.tick(60)

            await asyncio.sleep(0)

