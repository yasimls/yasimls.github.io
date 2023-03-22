# Recherche dichotomique — Cours d'Algorithmique et Programmation
# Luc Pellissier 2022
# CC0
def arrondi_decime(x: float) -> float: #float = nombre à, en entré on a à nombre à, et 
        """Fonction qui qui calcule l’arrondi au décime supérieur d’un nombre à virgule """
        return round(x, 1) #round arrondi # on a mis 1 pour 1 chiffre après la virgule 


assert arrondi_decime(10.72) == 10,7 #test assertion 

#print(arrondi_decime(45.76)) #on affiche le résultat avec  

def prixkm(distance:int) -> float: #ex2 #fonction qui prend en entrée un chiffre entier int et en sortie un nombre à , float 
    a:float=0 
    b:float=0 #on définit a et b comme étant des nombre à , . a et b sont les coeff de notre calcule
    if distance >=1 and distance < 16:
        a=0.7781 
        b=0.1944
    #else if / else if /else 
    return arrondi_decime(a + distance*b) #on retourne le calcule donné a+distancexb en décimal d'ou arrondi décim 


def prixkm1ere(distance:int) -> float: #meme chose que là hait #ex3
       return arrondi_decime(prixkm(distance) * 1.5)

def prix_speciaux_max(distance:int) -> float: 
        return arrondi_decime(prixkm(distance) * 2.1) # ce qui va s'afficher ici c'est le max pour chaque distance

