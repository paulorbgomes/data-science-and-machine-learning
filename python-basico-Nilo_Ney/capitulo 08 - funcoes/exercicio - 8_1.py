'''
Escreva uma função que retorne o maior de dois números.
'''
print("")

def máximo(a, b):
    lista = [a, b]
    for i in range(0, len(lista)):
        if i == 0:
            menor = lista[0]
            maior = lista[0]
        else:
            if lista[i] < menor:
                menor = lista[i]
            if lista[i] > maior:
                maior = lista[i]
    return maior

print(máximo(5, 6))
print(máximo(2, 1))
print(máximo(7, 7))
