# Projet — Cours d'Algorithmique et Programmation
# Yasmine IMOULLAS 2022

# Exercice 1 

def arrondi_decime(x: float) -> float: #float = nombre à virgule en entré on a à nombre à virgule ne sortie  
        """Fonction qui qui calcule l’arrondi au décime supérieur d’un nombre à virgule"""
        return round(x, 1) #round est utilisé pour arrondir # on a mis 1 pour arrondir à un 1 chiffre après la virgule comme demandé dans l'énoncé.  

assert arrondi_decime(10.72) == 10,7 #test assertion, on a mis == pour dire égale car = veut dire attribuer. Avec le test d'assertion, on veut tester la véracité de notre fonction

# Exercice 2 

def prixkm(distance:int) -> float:  #fonction qui prend en entrée un chiffre entier avec le type int et en sortie un nombre à virgule avec le type float 
    """Fonction qui qui calcule le prix en euros d'un trajet en TER en seconde classe"""
    a:float=0 
    b:float=0 #on définit a et b comme étant des nombre à virgule. a et b sont les coeff de notre calcule
    if distance >=1 and distance < 16: # on utilise if pour poser sous condition, en fonction de la distance qu'on aura choisit, le tarif en euro de la distance choisi. on se base sur les informations données par le tablea. on commence donc à 1 et on va jusqu'à 16
        a=0.7781 
        b=0.1944
    elif distance >=17 and distance < 32: # elif : sinon, si on est pas dans le premier cadre de 1 et 16 on sera dans le cadre 17 et 32. on va faire celà jusqu'à plus de 800km  
        a=0.2503
        b=0.2165
    elif distance >=33 and distance < 64:
        a=2.0706 # on utilise des points pas des, car les points veulent dire, comment on l'entend dans le sens courant or les , veulent dire séparation 
        b=0.1597
    elif distance >=65 and distance < 109:
        a=2.8891
        b=0.1489
    elif distance >=110 and distance < 149:
        a=4.0864
        b=0.1425
    elif distance >=150 and distance < 199:
        a=8.0871
        b=0.1193
    elif distance >=200 and distance < 300:
        a=7.7577
        b=0.1209
    elif distance >=301 and distance < 499:
        a=13.6514
        b=0.1030
    elif distance >=500 and distance < 799:
        a=18.4449
        b=0.0921
    else :
        distance < 799
        a=18.4449
        b=0.0921
    return arrondi_decime(a + distance*b) #on retourne le calcule donné a+distancexb en décimal. on met donc notre calcule entre ( ) de arrondi_decim pour l'arrondir 

assert arrondi_decime(0.7781+15*0.1944) == 3,7 # on se base sur les informations de la premier ligne de notre tableau. on prend donc a vaut 0.7781 à qui on additionne 15 en le multipliant à 0.1944 mais la multiplication se fait avant l'addition
# Exercie 3 

def prixkm1ere(distance:int) -> float: #fonction qui prend en entrée un chiffre entier avec le type int et en sortie un nombre à virgule avec le type float 
       """Fonction qui qui calcule le prix en euros d'un trajet en TER en premiere classe"""
       return arrondi_decime(prixkm(distance) * 1.5) 
       # on veut retounré le résultat de distance, notre entier, en le mutlipliant par 1,5 le tarif de 2nd classe pour avoir le tarrif en 1er classe. le calcul est mis en tre () de arrondi_decim pour avoir le résultat arrondi
       # la distance doit etre un nombre entier. 

assert arrondi_decime(prixkm(15) * 1.5) == 5,5 # on utilise notre premier exemple avec le résultat de l'exercice 3,5 auquel on multiplie 1.5 pour avoir notre résultat 

# Exercice 4 

def prix_speciaux_max(distance:int) -> float: #fonction qui prend en entrée un chiffre entier avec le type int et en sortie un nombre à virgule avec le type float 
        """Fonction qui qui calcule le prix maximum en euros d'un trajet en TER"""
        return arrondi_decime(prixkm(distance) * 2.1) # on prend donc la fonction prixkm qui est la fonction qui nous permet de calculer le prix en  € du km 
        # et on le multiplie avec 2,1 pour avoir le prix maximum pour chaque distance

assert arrondi_decime(prixkm(15) * 2.1) == 7,8 # on reprend notre exemple de l'exercice 1 auquel on multiplie 2,1 


# Exercice 5 

# le but de l'exercice est de recupérer les valeurs de distance.csv et les mettre dans un dictionnaire pour faciliter l'utilisation et l'exploitation du fichier 
with open("./distances.csv", mode="r", errors='ignore') as file: # on ouvre le fichier en lecture (mode r = lecture) en l'appeleant file. error=ignore : il y a des carractères spéciaux, comme ca python contourne ces erreures. 
    for line in file: #il faut mettre les : après file mais si je l'ai mets sans mettre la suite que je ne sais pas programmer, le fichier verra une erreur donc je préfère ne pas le mettre # pour chaque ligne du fichier #
       # je veux dire que pour chaque ligne du fichier il faut faire une recherche mais je ne sais pas comment programmer cela. 
        print # i

def information(gare1: str, gare2: str): # on a que des information en sortie pour les gare1 qui sera la gare de départ et la gare 
    dictionnaire:str = gare1 + gare2 #dictionnaire nous faire à faire la liaison entre la gare une et la gare deux. 
   if dictionnaire # si le nom de la gare existe, je ne sais pas comment le programmer  
        print("De " + gare1 + " à " + gare2 + ", il y a " + # le programme qui permet de rechercher les deux gares + "km\n") # afficher gare 1 et gare 2 et la distance 
        print(" + Le prix de ce voyage est de " + prixkm(dictionnaire))  # afficher le prix de ce trajet avec dictionnaire qui permet de savoir si la gare recherchée existe
        print(" + Le prix de ce voyage en 1ere classe est de " + prixkm1ere(dictionnaire)) # afficher le prix en premier classe de ce trajet 
        print(" + Le prix de ce voyage dans un cas spécial, ne peut exceder " + prix_speciaux_max(dictionnaire)) #prix max en cas d'intercité de nuit par exemple qui est fixé par décret 
    # dans les 4 cas au dessus je veux utiliser les fonctions qui sont nécessaires pour calculer les prix avec le dictionnaire qui fait la recherhce à chaque fois mais je n'arrive pas à le faire  
    else:
         print("L'une ou les 2 gares renseignées n'existent pas. Distance : " + "-1") # esle : sinon : afficher l'un des gare n'existe pas + -1 s'il y a une erreure comme demandé dans l'énnoncé