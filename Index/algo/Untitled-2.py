def petitGens(gens:list[tuple[str,int]]) -> tuple[int,list[str]]:
	mini = gens [0] [1]
	petits = [gens [0][0]]
	for pers in gens:
		if pers [1] < mini: 
			mini = pers [1]
			petits = [pers [0]]
		elif pers[1] == mini:
			petits = petits + [pers[0]]
	return (mini, petits)