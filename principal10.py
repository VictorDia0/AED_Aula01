matriz = [[1,2,3,1],[4,5,6,2],[7,8,9,3]]

def soma_matriz (matriz):
    soma = 0

    for i  in range (len(matriz)):
        for j in range (len(matriz) + 1):
            soma = soma + matriz[i][j]
    return soma

print(soma_matriz(matriz))