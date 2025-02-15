'''
Desenvolva três funções: soma, máximo e mínimo que retornem os
respectivos valores em uma lista. Em seguida, compare os
resultados obtidos com os das funções sum, max e min do python.
'''
print("")

def minimo(L):
    for i in range(0, len(L)):
        if i == 0:
            minimo = L[i]
        else:
            if L[i] < minimo:
                minimo = L[i]
    return minimo

def maximo(L):
    for i in range(0, len(L)):
        if i == 0:
            maximo = L[i]
        else:
            if L[i] > maximo:
                maximo = L[i]
    return maximo

def soma(L):
    soma = 0
    for i in L:
        soma = soma + i
    return soma

L = [7, 9, 12, 3, 100, 20, 4]
print(f"Meu resultado: {minimo(L)} | Resultado Python: {min(L)}")
print(f"Meu resultado: {maximo(L)} | Resultado Python: {max(L)}")
print(f"Meu resultado: {soma(L)} | Resultado Python: {sum(L)}")
