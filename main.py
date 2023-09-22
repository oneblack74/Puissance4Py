from graphique import Graphique
import asyncio

# la classe puissance4 dans game s'occupe de tout l'aspect technique
# par exemple poser un pion, vérifier si la partie est fini, géré la matrice, etc

# la classe graphique s'occupe de l'aspect visuel et gestion des entrées clavier souris

# maxmin c'est ton programme


if __name__ == "__main__":
    play = Graphique()
    asyncio.run(play.mainloop())