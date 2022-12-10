carac = 'abacate'

def vogais(carac):

    cont = 0
    for i in range (len(carac)):
        if carac[i] in ['a','e','i','o','u','A','E','I','O','U'] :
            cont = cont + 1

    return cont

print(vogais(carac)) # 4
print(vogais('uva')) # 2
print(vogais('relogio')) # 4