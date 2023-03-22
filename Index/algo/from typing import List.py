from typing import List

def plusGrand(noms:list[str], tailles:list[int]) -> str:
    """Renvoie le nom de la personne ayant la plus grande taille"""
    mini = tailles[0]
    personne = noms[0]
    longueur = len(noms)

    for i in range(1,longueur):
        if tailles[i] < mini:
            mini = tailles[i]
            personne = noms[i]