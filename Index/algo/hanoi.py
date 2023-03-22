def affiche(anneaux:int, depart:int,arrivee:int) -> None :
    print("On déplace l'anneau,", arrivee,"du piquet",depart,"au piquet",arrivee)

def piquet_en_plus(depart:int,arrivee:int) -> int:
    return 6 - depart-arrivee

def hanoi(anneaux:int)->int:
    if anneaux == 1:
        affiche(1,depart,arriv)
        return 1
    else:

