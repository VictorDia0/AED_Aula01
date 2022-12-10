contas = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

def mais_rico(contas):
    soma = 0
    maior = 0
    x = 0
    for i in range (len(contas)):
        x = i
        for j in range (len(contas) + 2):
            soma = soma + contas[x][j]
            if maior < soma:
                maior = soma 
        soma = 0
    return maior


print(mais_rico(contas))
print(len(contas))
# 65