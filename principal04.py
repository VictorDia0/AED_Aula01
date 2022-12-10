vet = [1,2,3,4,5,6,7,8,9,10]

def maior(vet):
    
    maior = vet[0]
    for i in range (len(vet)) :
        if vet[i] > maior:
            maior = vet[i]
    
    return maior
    
print(maior([1,5,7]))
print(maior(vet))