vet = [1,2,3,4,5,6,7,8,9,10]

def menor(vet):
    
    menor = vet[0]
    for i in range (len(vet)) :
        if vet[i] < menor:
            menor = vet[i]
    
    return menor
    
print(menor([-51,5,7,10,3,-100]))
print(menor(vet))