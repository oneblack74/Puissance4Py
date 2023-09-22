import numpy as np
import random
from qTable import *


class QLearningAgent:

    def __init__(self, alpha, gamma, epsilon):
        """
        Initialise le Q-learning Agent avec les taux d'apprentissage, de décroissance et d'exploration donnés
        """
        self.alpha = alpha # taux d'apprentissage
        self.gamma = gamma # taux de décroissance de l'exploration
        self.epsilon = epsilon # taux d'exploration initial

    def get_action(self, state, colones_vide):
        """
        Choisit une action en fonction de l'état actuel et des colonnes vides restantes
        """
        if random.random() <= self.epsilon:
            # exploration : choisir une action aléatoire
            print("random1")
            return random.choice(colones_vide)
        else:
            # exploitation : choisir l'action avec la plus grande valeur Q pour l'état actuel
            values = QTABLE[state[0], :, state[1], :]
            action = np.argmax(values)
            # s'assurer que l'action est possible en vérifiant que la colonne correspondante est vide
            print(action)
            if action in colones_vide:
                return action
            else:
                # si l'action n'est pas possible, choisir une action aléatoire
                print("random2")
                return random.choice(colones_vide)

    def update_q(self, state, action, new_state, reward):
        """
        Met à jour la valeur Q pour l'état actuel et l'action choisie en fonction de la récompense reçue et de la valeur Q du prochain état
        """
        current_q = QTABLE[state[0], action, state[1], :]
        next_max_q = np.max(QTABLE[new_state[0], :, new_state[1], :])
        new_q = current_q + self.alpha * (reward + self.gamma * next_max_q - current_q)
        QTABLE[state[0], action, state[1], :] = new_q

    def get_reward(self, etat_parti, joueur):
        """
        Calcule la récompense en fonction de l'état de la partie et du joueur
        """
        if etat_parti == -1:
            # partie nulle
            return 0
        else:
            if etat_parti == joueur:
                # joueur a gagné
                return 1
            else:
                # joueur a perdu
                return -1
