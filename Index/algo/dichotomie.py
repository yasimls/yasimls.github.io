def dichotomie (annuaire:list[tuple[str,int]], clef:str)-> int:
	debut = 0
	fin=len(annuaire)-1
	while debut != fin:
		milieu=(debut+fin)/2
		if annuaire [milieu][0] == clef:
			return annuaire [milieu][1]
		elif annuaire [milieu][0] > clef:
			fin = milieu
		else:
			debut = milieu