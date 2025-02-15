'''
Escreva um programa que exiba uma lista de opções (menu):
adição, subtração, divisão, multiplicação e sair. Imprima
a tabuada da operação escolhida. Repita até que a opção saída
seja escolhida.
'''
print("")

from time import sleep
while True:
    print(20 * "=")
    print(f"{'MENU':^20}")
    print(20 * "=")
    print("[1] SOMA")
    print("[2] SUBTRAÇÃO")
    print("[3] DIVISÃO")
    print("[4] MULTIPLICAÇÃO")
    print("[0] SAIR")
    print(20 * "=")
    op = str(input("Escolha uma opção: ")).strip()
    while op not in "12340":
        op = str(input("Opção inválida! Digite uma opção válida: ")).strip()
    if op == "0":
        print("Finalizando o programa ...")
        sleep(1)
        break
    if op == "1":
        print("Tabuada de Somar ... ")
        for i in range(1,11):
            for j in range(1,11):
                print(f"{i} + {j} = {j + i}")
            print(20 * "-")
    if op == "2":
        print("Tabuada de Subtrair ... ")
        for i in range(1,11):
            for j in range(i+1,11+i):
                print(f"{j} - {i} = {j - i}")
            print(20 * "-")
    if op == "3":
        print("Tabuada de Multiplicar ... ")
        for i in range(1,11):
            for j in range(1,11):
                print(f"{i} * {j} = {j * i}")
            print(20 * "-")
    if op == "4":
        l = 0
        print("Tabuada de Dividir ... ")
        for i in range(1,11):
            for j in range(1,11):
                l = i*j
                print(f"{l} / {i} = {int(l/i)}")
            print(20 * "-")
print("Volte sempre!")

    
