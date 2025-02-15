'''
Escreva uma função que pesquise um valor em uma lista e retorne
sua posição. Utilize os métodos de pesquisa em listas.
'''
print("")

def pesquise(L, valor):
    return L.index(valor)

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
