'''
Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de
caracteres. Retorne verdadeiro se o tamanho da string estiver
entre os valores de máximo e mínimo, e falso, caso contrário.
'''
print("")

def valida_string(string, minimo, maximo):
    if minimo <= len(string) <= maximo:
        return True
    else:
        return False

# Programa principal
string = str(input("Digite uma string: ")).strip()
print(valida_string(string, minimo=10, maximo=30))
