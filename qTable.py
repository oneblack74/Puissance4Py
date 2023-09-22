import pickle
import numpy as np




# Sauvegarde la Q-table dans un fichier
def sauvegarder_q_table(q_table, filename):
    with open(filename, 'wb') as f:
        pickle.dump(q_table, f)

# Charge la Q-table depuis un fichier
def charger_q_table(filename):
    with open(filename, 'rb') as f:
        q_table = pickle.load(f)
    return q_table

QTABLE = charger_q_table("qTableSave")
#QTABLE = np.zeros((6, 7, 2, 8))


victoire_j1 = 1
victoire_j2 = 1


