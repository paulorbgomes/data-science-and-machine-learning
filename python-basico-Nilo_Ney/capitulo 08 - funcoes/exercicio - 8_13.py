'''
Escreva uma função que receba uma string com as opções válidas
a aceitar (cada opção é uma letra). Converta as opções válidas
para letras minúsculas. Utilize input para ler uma opção, converter
o valor para letras minúsculas e cerificar se a opção é válida.
Em caso de opção inválida, a função deve pedir ao usuário que
digite novamente outra opção.
'''
print("")

def validacao(frase, opcoes):
    opcoes = opcoes.lower()
    while True:
        resp = str(input(frase)).strip().lower()
        if resp in opcoes:
            print("Opção válida! Resposta registrada!")
            break
        else:
            print("Opção inválida!")
    
# Programa principal
frase = "Digite sua escolha: "
opcoes = "ABCDE"
validacao(frase, opcoes)
