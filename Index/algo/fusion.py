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
