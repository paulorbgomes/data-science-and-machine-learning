'''
Exemplo:
Definir uma função que retorne verdadeiro ou falso, dependendo se
o número é par ou ímpar.
'''
print("")

def ePar(a):
    if a % 2 == 0:
        return True
    else:
        return False

def eImpar(a):
    if a % 2 != 0:
        return True
    else:
        return False
    
print(ePar(2))
print(ePar(3))
print(ePar(10))

print(eImpar(2))
print(eImpar(3))
print(eImpar(10))

