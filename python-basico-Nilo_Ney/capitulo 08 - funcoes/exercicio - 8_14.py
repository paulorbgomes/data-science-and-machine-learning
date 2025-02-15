'''
Altere o programa 8.20 (na página 184) de forma que o usuário
tenha três chances de acertar o número. O programa termina se o
usuário acertar ou errar três vezes.
'''
print("")

from random import randint
cont_vit = 0
cont_der = 0
while True:
    comp = randint(1, 10)
    while True:
        usu = int(input("Digite um número inteiro entre 1 e 10: "))
        if 1 <= usu <= 10:
            break
        else:
            print("Valor inválido! Tente novamente ...")
    if usu == comp:
        cont_vit = cont_vit + 1
        #print("Você acertou!", end=" ")
        if cont_vit != 3:
            print(f"ACERTOU! Você precisa acertar mais {3 - cont_vit} vez(es) para vencer.")
        elif cont_vit == 3:
            print("ACERTOU! Você acertou três vezes! Você venceu, parabéns!")
            break
    else:
        cont_der = cont_der + 1
        #print("Você errou!", end=" ")
        if cont_der != 3:
            print(f"ERROU! Você ainda pode errar {3 - cont_der} vez(es).")
        elif cont_der == 3:
            print("ERROU! Você errou três vezes! Infelizmente você perdeu.")
            break

        
