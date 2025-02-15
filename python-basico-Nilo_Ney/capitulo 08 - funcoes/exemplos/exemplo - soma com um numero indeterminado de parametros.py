'''
Escreva uma função que some um número indeterminado de valores.
'''
print("")

def soma(*args):
    soma = 0
    for i in args:
        soma = soma + i
    return soma

print(soma(1, 2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma(9, 10, 20, 30, 40))
