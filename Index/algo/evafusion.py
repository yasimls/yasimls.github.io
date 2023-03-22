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


def fusion(liste1:list[int], liste2:list[int])->list[int]:
	# prend en entrée 2 listes de type list
	i1=0 #variable de liste1
	i2=0 #variable liste2
	resultat=[]

	while i1<len(liste1) and i2<len(liste2): # tant que i1 est inférieur à la longueur de la liste 1 et pareil pour i2
		if liste1[i1]<liste2[i2]:
			resultat=resultat+[liste1[i1]] # l'ajouter à la liste finale
			i1=i1+1 # ensuite, on fait bouger le curseur à l'élement d'après
		else:
			resultat=resultat+[liste2[i2]] # l'ajouter à la liste finale
			i2=i2+1

	while i2<len(liste2):
		resultat=resultat+[liste2[i2]]
		i2=i2+1

	while i1<len(liste1):
		resultat=resultat+[liste1[i1]]
		i1=i1+1

	return resultat


def fusioninsertion(liste:list[int])-> list[int]:
	# première étape : diviser le tableau en 2 parties
    gauche=[]
    droite=[]
    milieu=len(liste)//2
    if milieu == 0:
        return liste

    for i in range(0,milieu):
        gauche=gauche+[liste[i]]
    
    for i in range(milieu,len(liste)):
        droite=droite+[liste[i]]

	# deuxième étape : faire un tri insertion pour les 2 tableaux
	# on a simplement repris la fonction triInsertion cf. supra
    gauche=fusioninsertion(gauche)
    droit=fusioninsertion(droite)

	#troisième étape : fusioner les 2 tableaux triés
	# on a simplement repris la fonction fusion cf. supra
    return fusion(gauche,droite)