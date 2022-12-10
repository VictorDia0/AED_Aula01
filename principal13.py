vetor = [1,2,3,4,5]

def soma_corrida(vetor):
    soma = 0
    lista_final = []
    for i in range (len(vetor)):
        soma = soma + vetor[i]
        lista_final.append(soma)

    return lista_final


print(soma_corrida(vetor))