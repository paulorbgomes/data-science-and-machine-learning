'''
Escreva uma função que receba dois números e retorne True se o
primeiro número for múltiplo do segundo.
'''
print("")

def múltiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(múltiplo(8, 4))
print(múltiplo(7, 3))
print(múltiplo(5, 5))
