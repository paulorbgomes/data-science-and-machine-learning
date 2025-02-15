'''
Escreva uma função que retorne o maior valor considerando um
número qualquer de parâmetros de entrada.
'''
print("")

def imprime_maior(*args):
    for i in range(0, len(args)):
        if i == 0:
            maior = args[i]
        else:
            if args[i] > maior:
                maior = args[i]
    return maior
            
print(imprime_maior(5, 4, 3, 1))
print(imprime_maior(*[1, 7, 9]))
