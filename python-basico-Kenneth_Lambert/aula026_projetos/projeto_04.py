'''
O matematico alemao Gottfried Leibniz desenvolveu o seguinte metodo para aproximar o valor de pi:
pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Escreva um programa que permita ao usuario especificar o numero de iteracoes usadas nessa aproximacao e exibir o valor resultante.
'''

from math import pi

def aproximaPi(numIteracoes):
    denominadores = []
    for i in range(1, numIteracoes + 1, 1):
        if i == 1:
            denominadores.append(1)
        else:
            denominadores.append(denominadores[i - 2] + 2)
    #print(denominadores)

    resultado = 0
    for index, value in enumerate(denominadores):
        if index % 2 == 0:
            resultado = resultado + (1 / denominadores[index]) 
        else:
            resultado = resultado - (1 / denominadores[index])
    return resultado

if __name__ == "__main__":
    numIteracoes = int(input("Especifique o numero de iteracoes: "))
    resposta = aproximaPi(numIteracoes)
    erro = pi - (4 * resposta)
    print(f"Erro de aproximação em {numIteracoes} iteracoes: {erro}")