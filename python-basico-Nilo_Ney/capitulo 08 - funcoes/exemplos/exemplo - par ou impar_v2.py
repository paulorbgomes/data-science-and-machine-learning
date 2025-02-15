'''
Exemplo:
Definir uma função que retorne a palavra par ou ímpar.
'''
print("")

def par_ou_impar(a):
    if a % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar(4))
print(par_ou_impar(5))
