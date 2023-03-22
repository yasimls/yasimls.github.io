def fusion (liste1: list[int],liste2:list[int])->list[int]:
    i1=0
    i2=0
    resultat=[]
    while i1 < len(liste1) and i2 < len(liste2):
        if  liste1[i1]<liste2[i2]:
            resultat=resultat+[liste1[i1]]
            i1=i1+1
        else:
            resultat=resultat+[liste2[i2]]
            i2=i2+1
    while i2<len(liste2):
       resultat=resultat+[liste2[i2]]
       i2=i2+1
    while i1<len(liste1):
       resultat=resultat+[liste1[i1]]
       i1=i1+1
    return resultat

def triInsertion(elements:list[int]) -> list[int]:
    """Réalise un tri par insertion de nombres entiers"""

    N = len(elements) # On calcule la longueur de la liste

    for i in range(0,N): # Pour chaque position de la liste
        j = i
        #  On fait reculer l'élément à la position i jusqu'à ce qu'il soit à sa place

        while j > 0 and elements[j-1] > elements[j]:
            # Les trois lignes suivantes inversent elements[j-1] et elements[j]
            # en utilisant une variable temporaire tmp
            tmp = elements[j-1]
            elements[j-1] = elements[j]
            elements[j] = tmp

            j = j-1

    return elements


def tri     (liste:list[int])->list[int]:
    gauche=[]
    droite=[]
    milieu=len(list)//2
    for i in range(0,milieu):
        gauche=gauche+[liste[i]]
    for i in range(milieu,len(list)):
        droite=droite+[liste[i]]
    gauche=triInsertion(gauche)
    droite=triInsertion(droite)
    return fusion(gauche,droite)    





    