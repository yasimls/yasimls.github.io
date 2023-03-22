def prixkm(distance:int) -> float: #fonction qui prend en entrée un chiffre entier int et en sortie un nombre à , float 
    a:float=0 
    b:float=0 #on définit a et b comme étant des nombre à , . a et b sont les coeff de notre calcule
    if distance >=1 and distance < 16:
        a=0.7781 
        b=0.1944
    #else if / else if /else 
    return a + distance*b 