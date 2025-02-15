'''
Escreva uma função que retorne a soma dos valores de uma lista.
'''
print("")

def soma(L):
    soma = 0
    for i in L:
        soma = soma + i
    return soma

L = [1, 7, 2, 9, 15]
print(soma(L))
L = [7, 9, 12, 3, 100, 20, 4]
print(soma(L))
