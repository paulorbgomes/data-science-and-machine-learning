'''
Escreva uma função que retorne o fatorial de um número.
'''
print("")

def fatorial(n):
    fat = n
    cont = 1
    if n == 0:
        return 1
    else:
        while cont < n:
            fat = fat * cont
            cont = cont + 1
        return fat
        
print(fatorial(5))
