matriz = [[1,2,3],[4,5,6],[7,8,9]]

def soma_diagonal (matriz):
    soma = 0

    for i  in range (len(matriz)):
        for j in range (len(matriz) + 1):
            if i == j:
                soma = soma + matriz[i][j]
    return soma

print(soma_diagonal(matriz))