vet = [1,2,3,4,5,6,7,8,9,10]

def media(vet):
    soma = 0
    cont = 0
    for i in range(len(vet)):
        soma = soma + vet[i]
        cont = cont + 1
    media = soma / cont
    return media

print(media(vet))


'''
def media(vetor):
    soma = 0
    for valor in vetor:
        soma = soma + valor
    
    return soma / len(vetor)'''