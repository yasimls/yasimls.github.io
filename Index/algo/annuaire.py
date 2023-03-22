def cherche (annuaire:list[tuple[str,int]],clef:str)->int:
	for elt in annuaire:
		if elt[0]== clef: 
			return elt[1]
	return 0