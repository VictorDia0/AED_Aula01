vetor = [1,2,3,5,4,3,2,1,4]
vetor.sort()

def unico(vetor):
    vet = []
    s = []
    for i in range(0,len(vetor)):
        if vetor[i] not in vet:
            vet.append(vetor[i])
        else :
            s.append(vetor[i])
    
    for i in range(0,len(vet)):
        if vet[i] not in s:
            return vet[i]


print(unico(vetor))