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
