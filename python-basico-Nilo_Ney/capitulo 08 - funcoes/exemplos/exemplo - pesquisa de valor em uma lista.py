'''
Declarar uma função que pesquisa um valor em uma lista e retorna
sua posição.
'''
print("")

def pesquise(L, valor):
    cont = 0
    for i in range(0, len(L)):
        if L[i] == valor:
            cont = cont + 1
            return i
    if cont == 0:
        return None

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
