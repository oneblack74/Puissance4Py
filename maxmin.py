import numpy as np

def est_gagnant(A,joueur):
    n,p = np.shape(A)
    for i in range(n):
        for j in range(p-3):
            if A[i,j] == joueur and A[i,j+1] == joueur and A[i,j+2] == joueur and A[i,j+3] == joueur:
                return True

    for j in range(p):
        for i in range(n-3):
            if A[i,j] == joueur and A[i+1,j] == joueur and A[i+2,j] == joueur and A[i+3,j] == joueur:
                return True

    for i in range(n-3):
        for j in range(p-3):
            if A[i,j] == joueur and A[i+1,j+1] == joueur and A[i+2,j+2] == joueur and A[i+3,j+3] == joueur:
                return True

    for i in range(n-3):
        for j in range(3,p):
            if A[i,j] == joueur and A[i+1,j-1] == joueur and A[i+2,j-2] == joueur and A[i+3,j-3] == joueur:
                return True

    return False

def colonnes_vides(A):
    return [j for j in range(np.shape(A)[1]) if A[0,j]==0]

def heuristique(A):
    if est_gagnant(A,1): return np.inf
    if est_gagnant(A,2): return -np.inf

    J = np.array([
        [3,4,5,7,5,4,3],
        [4,6,8,10,8,6,4],
        [5,8,11,13,11,8,5],
        [5,8,11,13,11,8,5],
        [4,6,8,10,8,6,4],
        [3,4,5,7,5,4,3]])

    heu = 0
    for i in range(6):
        for j in range(7):
            if A[i,j] == 1:
                heu+=J[i,j]
            if A[i,j] == 2:
                heu-=J[i,j]
    return heu


def successeur(A,joueur):
    listeColonnes = colonnes_vides(A)
    successeur = []
    for j in listeColonnes:
        i = 5
        while A[i,j] != 0:
            i-=1
        successeur.append((i,j))

    return successeur

def jouer_coup(A,joueur,colonne):
    A1 = np.copy(A)
    for i  in range(6):
        if A[5-i,colonne] == 0:
            A1[5-i,colonne] = joueur
            return A1
    return A1

def minimax(A,n):
    if n == 0 or successeur(A,2) == []:
        return heuristique(A)
    mini = np.inf
    for pk in successeur(A,2):
        s = maximin(jouer_coup(A,2,pk[1]),n-1)
        if s<mini: mini = s

    return mini


def maximin(A,n):
    if n == 0 or successeur(A,1) == []:
        return heuristique(A)
    maxi = -np.inf
    for pk in successeur(A,1):
        s = minimax(jouer_coup(A,1,pk[1]),n-1)
        if s>maxi: maxi = s

    return maxi


def choix_ia(n, A):
    min = np.inf
    pos_min = (0, 0)
    succ = successeur(A, 2)
    for pk in succ:
        a = maximin(jouer_coup(A,2,pk[1]),n)
        if a < min:
            min = a
            pos_min = pk

    return pos_min[1]

