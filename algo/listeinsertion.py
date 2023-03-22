# Algorithmique et Programmation — Master Droit & Informatique 
# IMOULLAS Yasmine 
# 28/09


from typing import List, Any 

def      (liste):

    """On remplit une liste vide des éléments pairs  sur deux de la liste l"""
    resultat=[] 
    #resultat vide au début 
    for nombre in liste:
        if nombre % 2 == 0: 
            resultat = resultat + [nombre]

    return resultat
