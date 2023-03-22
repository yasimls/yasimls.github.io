def bonjour(bjr:str)->str:
    N=len(bjr)
    resultat=''
    for i in range (1,N+1):
        resultat=resultat + bjr[N-i] 
    return resultat
    