'''
Escreva um programa em que o computador sorteie um número de
1 a 10. O usuário deverá tentar advinhar o número sorteado
mostrando a mensagem Você acertou! e caso de acerto e Você errou!
em caso de erro.
'''
print("")

from random import randint
comp = randint(1, 10)
while True:
    usu = int(input("Digite um número inteiro de 1 a 10: "))
    if 1 < usu > 10:
        print("Valor inválido! Tente novamente ...")
    else:
        break
if usu == comp:
    print("Você acertou!")
else:
    print("Você errou!")
