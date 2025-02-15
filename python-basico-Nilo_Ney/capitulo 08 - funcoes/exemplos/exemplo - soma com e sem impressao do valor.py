'''
Escreva uma funçao quse some dois valores a e b. Sua função deve
ter um parâmetro opcional chamado imprime. Caso imprime seja
False, a soma não é mostrada na tela. Caso imprime seja True,
a soma é mostrada na tela. Em ambos os casos a função retorna o
resultado.
'''
print("")

def soma(a, b, imprime=False):
    s = a + b
    if imprime == True:
        print(f"A soma entre {a} e {b} vale {s}.")
    return s

soma(2, 3)
soma(2, 3, True)
soma(5, 8, False)
