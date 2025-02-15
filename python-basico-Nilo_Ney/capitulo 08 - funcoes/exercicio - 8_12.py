'''
Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também
passada como parâmetro. Retorne verdadeiro se a string for encontrada
dentro da lista, e falso, caso contrário.
'''
print("")

def comparacao(string, lista):
    if string in lista:
        return True
    else:
        return False

print(comparacao("Paulo", ["Gustavo", "Pedro", "Flávia", "Paulo"]))
