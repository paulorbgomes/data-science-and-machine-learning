'''
Implemente um função que calcule e retorne a média dos valores
de uma lista.
'''
print("")

def media(L):
    soma = 0
    for i in L:
        soma = soma + i
    return soma / len(L)


L = [10, 20, 25, 30]
print(media(L))
